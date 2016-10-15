from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un usuario puede ejecutar el método o acceder a la vista/controlador que quiere acceder
        :param request:
        :param view:
        :return:
        """
        if request.method == "POST" and request.user.is_authenticated:
            return True
        if request.user.is_superuser:
            return True
        if view.action in ("list", "retrieve", "update", "destroy", "partial_update"):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si un usuario puede realizar la operacion que quiere sobre el objeto 'obj'
        :param request:
        :param view:
        :param obj:
        :return:
        """
        if view.action in ("retrieve",):
            return True
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated:
            if view.action in ("update", "destroy", "partial_update") and request.user == obj.blog.usuario:
                return True
        return False