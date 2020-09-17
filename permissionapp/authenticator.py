from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from permissionapp.models import User

"""
1、创建认证器并继承`BaseAuthentication`
2、重写`authenticate`方法完成认证逻辑
3、自定义认证规则
    没有认证信息返回None(游客)
    有认证信息但不符合(非法用户)
    有认证信息且认证成功  返回用户与信息元祖(合法用户)
4、进行全局配置或者局部配置
"""


class MyAuth(BaseAuthentication):
    """
    前端需要携带认证信息 必须按照一定的格式来
    默认使用Authorization携带认证信息
    认证信息都包含着在 request.META字段中
    """

    def authenticate(self, request):
        # 获取认证信息
        auth = request.META.get("HTTP_AUTHORIZATION", None)
        print(auth)

        if auth is None:
            # 代表没有认证信息  游客
            return None

        # 设置认证信息的校验
        auth_list = auth.split()

        # 校验规则：认证信息的格式是否符合要求
        if not (len(auth_list) == 2 and auth_list[0].lower() == "auth"):
            raise exceptions.APIException("用户认证信息格式有误")

        # 如果认证成功，则解析用户  暂时规定认证信息必须是`xiefeng.com`
        if auth_list[1] != "xiefeng.com":
            raise exceptions.APIException("用户信息校验失败")

        # 校验数据库是否存在此用户
        user = User.objects.filter(username="xiefeng").first()

        if not user:
            raise exceptions.APIException("用户不存在")

        return (user, None)
