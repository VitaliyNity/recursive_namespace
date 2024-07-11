from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django_user_agents.utils import get_user_agent

class DeviceDetectionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_agent = get_user_agent(request)
        if user_agent.is_mobile or user_agent.is_tablet:
            if not request.path.startswith('/mobile/'):
                return HttpResponseRedirect(reverse('mobile:index'))
        else:
            if not request.path.startswith('/desktop/'):
                return HttpResponseRedirect(reverse('desktop:index'))