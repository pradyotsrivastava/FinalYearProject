from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from .constants import Contants

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated()):
            return redirect_to_login(request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        
        if request.user.role_assigned.name==Contants.ROLE_USER:
            print('User')
            pass
        elif request.user.role_assigned.name==Contants.ROLE_HOSPITAL_ADMIN:
            print('Hospital admin')
            pass
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)