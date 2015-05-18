from flask import jsonify, request, Blueprint
from flask.views import MethodView

import animalprison.core
import animalprison.common


class ServiceCollectionAPI(MethodView):

    __serializer__ = None

    def on_get(self):
        """
        :return:
        """
        pass

    def on_serialize(self):
        """
        :return:
        """
        pass

    def get(self, service_id):
        """
        :type service_id: str
        :param service_id:
        :return:
        """

        result = animalprison.core.get_service(service_id)

        if not result:
            res = jsonify(error='Not Found')
            res.status_code = 404
            return res

        if service_id:
            return jsonify(service=result)
        else:
            return jsonify(services=result)

    def post(self):

        service_data = request.get_json()
        animalprison.core.add_service(service_data)


service_blueprint = Blueprint("service_blueprint", __name__)
services_view_func = ServiceCollectionAPI.as_view('service_collection_api')

animalprison.common.add_url_rule(service_blueprint, '/services/', services_view_func, ['GET', ],
                                 defaults_dict={'service_id': None},)
animalprison.common.add_url_rule(service_blueprint, '/services/', services_view_func,
                                 methods_list=['POST', ])
animalprison.common.add_url_rule(service_blueprint, '/services/<string:service_id>',
                                 services_view_func, ['GET', 'PUT', 'DELETE'])
