{% extends "mail_templated/base.tpl" %}

{% block subject %}
User Activation
{% endblock %}

{% block html %}
http://127.0.0.1:8000/api/v1activate/confirm/{{token}}
{% endblock %}