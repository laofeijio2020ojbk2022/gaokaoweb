from django import forms
from django.shortcuts import render, HttpResponse, redirect
import io
import os
from app01.utils.bootstrap import BootStrapForm,BootStrapModelForm

# import models
class LoginForm(BootStrapForm):
    p_name = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    p_password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("p_password")
        return pwd

# def login(request):
#     if request.method == "GET":
#         return render(request, "login.html")
#
#     print(request.POST)
#     username = request.POST.get("user")
#     password = request.POST.get("pwd")
#
#     if username == 'root' and password == '123':
#         # return HttpResponse("登陆成功")
#         return redirect("")
#
#     return render(request, "login.html", {'error_msg': '用户名或密码错误'})
from app01.models import People
def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        admin_object = People.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("p_password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        request.session["info"] = {'nid': admin_object.p_id,'name':admin_object.p_name}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)

        return render(request, 'house_page.html')
        # return HttpResponse("测试登陆成功")
    return render(request, 'login.html', {'form': form})


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/login/')

class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = People
        fields = ["p_name", 'p_password', "confirm_password"]
        widgets = {
            "p_password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("p_password")
        return pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("p_password")
        confirm = self.cleaned_data.get("confirm_password")
        if confirm != pwd:
            # raise ValidationError("密码不一致")
            pass
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm


def admin_add(request):
    # info_dict = request.session["info"]
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'change.html', {'form': form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    return render(request, 'change.html', {'form': form})

class MyModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = People
        fields = ["p_name", 'p_password']
        widgets = {
            "p_password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("p_password")
        return pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("p_password")
        confirm = self.cleaned_data.get("confirm_password")
        if confirm != pwd:
            # raise ValidationError("密码不一致")
            pass
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm


def user_edit(request, nid):
    """ 编辑用户 """
    row_object = People.objects.filter(p_id=nid).first()

    if request.method == "GET":
        form = MyModelForm(instance=row_object)
        return render(request, 'edit.html', {'form': form})

    form = MyModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return render(request, 'house_page.html')
    # 返回首页
    return render(request, 'edit.html', {"form": form})
def logout(request):
    request.session.clear()
    return redirect('/login/')

def register(request):
    return render(request, "register.html")


def house_page(request):
    return render(request, "house_page.html")


def school_get(request):
    return render(request, "school_get.html")


from app01.models import SchoolInfo, SchoolLogal, SchoolIndex
import base64


def school_info(request):
    # print(request.GET)
    sc_name = request.GET.get("sc_name")
    # print(sc_name)

    # 学校基本信息查询查询
    data = SchoolInfo.objects.filter(sc_name=sc_name)
    sc_data = data.values().first()
    # print(sc_data)

    if sc_data is None:
        return render(request, "school_info.html", {"error_msg": "请输入正确的学校名称！！！"})

    # 查询学校校徽
    icon = SchoolLogal.objects.filter(logal_name=sc_name)
    icon = icon.values().first()["logal_data"]
    icon = base64.b64encode(icon).decode('utf-8')
    # print(icon)

    imgs = SchoolIndex.objects.filter(si_name=sc_name)
    imgs = imgs.values().first()
    imgs_name = imgs["img_name"]
    # print(imgs_name.split(","))

    return render(request, "school_info.html", {"sc_data": sc_data,
                                                "icon": icon,
                                                "imgs": imgs,
                                                "imgs_name": imgs_name})


from app01.models import ScoreTable
from django.db.models import Q


class ScoreModelForm(forms.ModelForm):
    class Meta:
        model = ScoreTable
        fields = ["pro", "st_school_name", "st_year", "st_type", "st_spname",
                  "st_max", "st_min", "st_average", "st_min_section",
                  "st_level1_name", "st_level2_name", "st_level3_name", "st_zslx_name",
                  "st_local_batch_name", "st_sg_info"]


def score_get(request):
    form = ScoreModelForm()
    if request.method == "GET":
        return render(request, "score_get.html", {"from": form})

    data = request.POST.dict()
    del data['csrfmiddlewaretoken']

    the_del = []
    for key, value in data.items():
        if len(value) == 0:
            the_del.append(key)
    for i in the_del:
        del data[i]
    data = ScoreTable.objects.filter(**data)
    data = data.values()

    if data.first() is None:
        return render(request, "score_get.html", {"from": form, "error_msg": "输入信息有误！！！"})

    return render(request, "score_get.html", {"from": form, "data": data})

from app01.models import RatePredict
def score_pre(request):
    if request.method == "GET":
        return render(request, "score_pre.html")
    sc_name = request.POST.get("sc_name")
    # print(sc_name)
    data = RatePredict.objects.filter(ra_school_name=sc_name).order_by("-ra_predict_score")
    # print(data)
    if data.first() is None:
        return render(request, "score_pre.html", {"error_msg": "请输入正确的学校名称！！！"})

    return render(request, "score_pre.html", {"data": data})




def int_recom(request):
    if request.method == "GET":
        return render(request, "int_recom.html")

    st_name = request.POST.get("st_name")
    st_password = request.POST.get("st_password")

    dic = {'p_name': st_name, 'p_password': st_password}
    # print(dic)

    data2 = People.objects.filter(**dic)
    data2 = data2.values().first()["p_word"]
    data2 = data2.split(",")

    data3 = []

    for i in data2:
        # print(request.GET)
        sc_name = i
        # print(sc_name)

        # 学校基本信息查询查询
        data = SchoolInfo.objects.filter(sc_name=sc_name)
        sc_data = data.values().first()
        # print(sc_data)

        # 查询学校校徽
        icon = SchoolLogal.objects.filter(logal_name=sc_name)
        icon = icon.values().first()["logal_data"]
        icon = base64.b64encode(icon).decode('utf-8')
        # print(icon)

        cot = sc_data["sc_content"][0:150] + "  . . ."
        # print(cot)

        rer = {'sc_data': sc_data, 'icon': icon, 'cot': cot}
        data3.append(rer)

    return render(request, "int_recom.html", {"data3": data3})

    # return render(request, "int_recom.html", {"sc_data": sc_data, "icon": icon,
    #                                           "cot": cot})


from app01.models import ScMinAna, NumSpname


class ScMinModelForm(forms.ModelForm):
    class Meta:
        model = ScMinAna
        fields = ["min_pro_name", "min_st_name", "min_st_local_batch_name"]


def ana_sc(request):
    form = ScMinModelForm()
    if request.method == "GET":
        return render(request, "ana_sc.html", {"from": form})
    data_fi = request.POST.dict()
    del data_fi['csrfmiddlewaretoken']
    try:
        data = ScMinAna.objects.filter(**data_fi).order_by("min_st_min_section")
        data = data.values()
    except:
        return render(request, "ana_sc.html", {"from": form, "error_msg": "1输入信息有误！！！"})
    if data.first() is None:
        return render(request, "ana_sc.html", {"from": form, "error_msg": "1输入信息有误！！！"})

    name = []
    name_data = []
    for item in data:
        # print(item)
        name.append(item['min_st_school_name'])
        name_data.append(item['min_st_min_section'])

    # print(list(zip(name, name_data)))
    # thepie = pie_chart(list(zip(name, name_data)))

    theline = line_chart([name, name_data])

    data2 = {}
    data2["si_pro_name"] = data_fi["min_pro_name"]
    data2["si_st_year"] = data_fi["min_st_name"]
    # print(data2)
    try:
        data2 = NumSpname.objects.filter(**data2).order_by("si_st_spname")
        data2 = data2.values()
    except:
        return render(request, "ana_sc.html", {"from": form, "error_msg": "2输入信息有误！！！"})
    if data2.first() is None:
        return render(request, "ana_sc.html", {"from": form, "error_msg": "2输入信息有误！！！"})

    name2 = []
    name_data2 = []
    for item in data2:
        # print(item)
        name2.append(item['si_st_school_name'])
        name_data2.append(item['si_st_spname'])
    thebar = bar_chart([name2, name_data2])

    return render(request, "ana_sc.html", {"from": form, "data": data, "name": name,
                                           "name_data": name_data, "theline": theline,
                                           "thebar": thebar})

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
def pie_chart(request):
    # 生成饼图的数据和配置
    data = request
    chart = (
        Pie()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="饼图示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="b"))
    )

    # 将饼图转换为HTML代码
    chart_html = chart.render_embed()

    return chart_html

from pyecharts.charts import Line
from pyecharts.faker import Faker
def line_chart(request):
    # 生成折线图的数据和配置
    x_data = request[0]
    y_data = request[1]

    chart = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name='示例数据',
            y_axis=y_data,
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='各校对各省学生招生的最低位次'),
            tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
            xaxis_opts=opts.AxisOpts(
                # scale=True,
                axislabel_opts=opts.LabelOpts(interval=10)
            ),
            yaxis_opts=opts.AxisOpts(type_='value'),
            datazoom_opts=[opts.DataZoomOpts(type_='inside'), opts.DataZoomOpts()]
        )
    )

    # 将折线图转换为HTML代码
    chart_html = chart.render_embed()

    return chart_html

def bar_chart(request):
    # 生成条形图的数据和配置
    x_data = request[0]
    y_data = request[1]

    def color_manager(params):
        color_list = [
            '#0000FF', '#0040FF', '#0080FF', '#00BFFF', '#00FFFF', '#40FFBF', '#80FF80', '#C0FF40', '#FFFF00',
            '#FFBF00', '#FF8000', '#FF4000', '#FF0000', '#BF0000', '#800000', '#400000', '#000000'
        ]
        return color_list[params.dataIndex % len(color_list)]

    chart = (
        Bar()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name='示例',
            y_axis=y_data,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(color=color_manager),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='各校对各省学生招生的专业数量'),
            tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(interval=0, rotate=90),
            ),
            yaxis_opts=opts.AxisOpts(type_='value'),
            visualmap_opts=opts.VisualMapOpts(
                dimension=0,
                is_piecewise=True,
                pos_top='10%',
                pos_right='%',
                pieces=[
                    {"min": 0, "max": 30, "color": '#000000'},
                    {"min": 30, "max": 60, "color": '#400000'},
                    {"min": 60, "max": 90, "color": '#800000'},
                    {"min": 90, "max": 120, "color": '#BF0000'},
                    {"min": 120, "max": 150, "color": '#FF0000'},
                    {"min": 150, "max": 180, "color": '#FF4000'},
                    {"min": 180, "max": 210, "color": '#FF8000'},
                    {"min": 210, "max": 240, "color": '#FFBF00'},
                    {"min": 240, "max": 300, "color": '#FFFF00'},
                    {"min": 300, "max": 360, "color": '#C0FF40'},
                    {"min": 360, "max": 420, "color": '#80FF80'},
                    {"min": 420, "max": 480, "color": '#40FFBF'},
                    {"min": 480, "max": 540, "color": '#00FFFF'},
                    {"min": 540, "max": 600, "color": '#00BFFF'},
                    {"min": 600, "max": 660, "color": '#0080FF'},
                    {"min": 660, "max": 720, "color": '#0040FF'},
                    {"min": 720, "max": 800, "color": '#0020FF'},
                    {"min": 800, "max": 900, "color": '#0010FF'},
                    {"min": 800, "max": 1000, "color": '#0000FF'},
                ],
            ),
            datazoom_opts=[opts.DataZoomOpts(type_='inside'), opts.DataZoomOpts()],
        )
    )

    # 将条形图转换为HTML代码
    chart_html = chart.render_embed()

    return chart_html