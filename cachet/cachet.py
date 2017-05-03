import os
import requests

CACHET_URL = os.getenv('CACHET_URL', None)
CACHET_TOKEN = os.getenv('CACHET_TOKEN', None)


class Cachet(object):
    def __init__(self):
        if not CACHET_URL and not CACHET_TOKEN:
            raise Exception('Set CACHET_URL and  CACHET_TOKEN environment variables')
        self.url = CACHET_URL
        self.apiToken = CACHET_TOKEN

    def __get_request(self, path):
        return requests.get(self.url + path)

    def __post_request(self, path, data):
        return requests.post(self.url + path, data, headers={'X-Cachet-Token': self.apiToken})

    def __put_request(self, path, data):
        return requests.put(self.url + path, data, headers={'X-Cachet-Token': self.apiToken})

    def __del_request(self, path):
        return requests.delete(self.url + path, headers={'X-Cachet-Token': self.apiToken})

    def ping(self):
        """API test endpoint.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__get_request('/ping')

    def get_components(self):
        """Return all components that have been created.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__get_request('/components')

    def get_components_by_id(self, id):
        """Return a single component.

        :param id: Component ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__get_request('/components/%s' % id)

    def post_components(self, name, status, **kwargs):
        """Create a new component.

        :param name: Name of the component
        :param status: Status of the component; 1-4
        :param description: (optional) Description of the component
        :param link: (optional) A hyperlink to the component
        :param order: (optional) Order of the component
        :param group_id: (optional) The group id that the component is within
        :param enabled: (optional)
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        kwargs['name'] = name
        kwargs['status'] = status
        return self.__post_request('/components', kwargs)

    def put_components_by_id(self, _id, **kwargs):
        """Updates a component.

        :param _id: Component ID
        :param name: (optional) Name of the component
        :param status: (optional) Status of the component; 1-4
        :param link: (optional) A hyperlink to the component
        :param order: (optional) Order of the component
        :param group_id: (optional) The group id that the component is within
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__put_request('/components/%s' % _id, kwargs)

    def delete_components_by_id(self, _id):
        """Delete a component.

        :param _id: Component ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__del_request('/components/%s' % _id)

    def get_components_groups(self):
        """

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__get_request('/components/groups')

    def get_components_groups_by_id(self, _id):
        """

        :param _id: ID of the group you want to fetch
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__get_request('/components/groups/%s' % _id)

    def post_components_groups(self, name, **kwargs):
        """

        :param name: Name of the component group
        :param order: (optional) Order of the component group
        :param collapsed: (optional) Whether to collapse the group by default
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        kwargs['name'] = name
        return self.__post_request('/components/groups', kwargs)

    def put_components_groups_by_id(self, _id, **kwargs):
        """

        :param _id: Component group to update
        :param name: (optional) Name of the component group
        :param order: (optional) Order of the group
        :param collapsed: (optional) Whether to collapse the group by default
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__put_request('/components/groups/%s' % _id, kwargs)

    def delete_components_groups_by_id(self, _id):
        """

        :param _id: Component group to delete
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__get_request('/components/groups/%s' % _id)

    def get_incidents(self):
        """Return all incidents.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__get_request('/incidents')

    def get_incidents_by_id(self, _id):
        """Returns a single incident.

        :param _id: Incident ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        return self.__get_request('/incidents/%s' % _id)

    def post_incidents(self, name, message, status, visible, **kwargs):
        """
        Create a new incident.

        :param name: Name of the incident
        :param message: A message (supporting Markdown) to explain more.
        :param status: Status of the incident.
        :param visible: Whether the incident is publicly visible.
        :param component_id: (optional) Component to update.
        :param component_status: (optional) The status to update the given component with.
        :param notify: (optional) Whether to notify subscribers.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        kwargs['name'] = name
        kwargs['message'] = message
        kwargs['status'] = status
        kwargs['visible'] = visible
        return self.__post_request('/incidents', kwargs)

    def put_incidents_by_id(self, _id, **kwargs):
        '''

        :param _id: ID of the incident to update.
        :param name: (optional) Name of the incident
        :param message: (optional) A message (supporting Markdown) to explain more.
        :param status: (optional) Status of the incident.
        :param visible: (optional) Whether the incident is publicly visible.
        :param component_id: (optional) Component to update.
        :param notify: (optional) Whether to notify subscribers.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__put_request('/incidents/%s' % _id, kwargs)

    def delete_incidents_by_id(self, _id):
        '''Delete an incident.

        :param _id: Incident ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__del_request('/incidents/%s' % _id)

    def getMetrics(self):
        '''Returns all metrics that have been setup.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__get_request('/metrics')

    def post_metrics(self, name, suffix, description, default_value, **kwargs):
        '''Create a new metric.

        :param name: Name of metric
        :param suffix: Measurments in
        :param description: Description of what the metric is measuring
        :param default_value: The default value to use when a point is added
        :param display_chart: (optional) Whether to display the chart on the status page
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['name'] = name
        kwargs['suffix'] = suffix
        kwargs['description'] = description
        kwargs['default_value'] = default_value
        return self.__post_request('/metrics', kwargs)

    def get_metrics_by_id(self, _id):
        '''Returns a single metric, without points.

        :param _id: Metric ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__get_request('/metrics/%s' % _id)

    def delete_metrics_by_id(self, _id):
        '''Delete a metric.

        :param _id: Metric ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__del_request('/metrics/%s' % _id)

    def get_metrics_points_by_id(self, _id):
        '''Return a list of metric points.

        :param _id: Metric ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__get_request('/metrics/%s/points' % _id)

    def post_metrics_points_by_id(self, _id, value, **kwargs):
        '''Add a metric point to a given metric.

        :param _id: Metric ID
        :param value: Value to plot on the metric graph
        :param timestamp: Unix timestamp of the point was measured
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['value'] = value
        return self.__post_request('/metrics/%s/points' % _id, kwargs)

    def delete_metrics_points_by_id(self, _id, point_id):
        '''Delete a metric point.

        :param _id: Metric ID
        :param point_id: Metric Point ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__del_request('/metrics/%s/points/%s' % (_id, point_id))

    def get_subscribers(self):
        '''Returns all subscribers.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__get_request('/subscribers')

    def post_subscribers(self, email, **kwargs):
        '''Create a new subscriber.

        :param email: Email address to subscribe
        :param verify: (optional) Whether to send verification email
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['email'] = email
        return self.__post_request('/subscribers', kwargs)

    def delete_subscribers_by_id(self, _id):
        '''Delete a subscriber.

        :param _id: ID of the subscriber to delete
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__del_request('/subscribers/%s' % _id)
