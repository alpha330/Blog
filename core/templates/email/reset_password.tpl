{% extends "mail_templated/base.tpl" %}

{% block subject %}
User Password Reset
{% endblock %}

{% block html %}
<p> <a href="{% url 'accounts:api_v1_user:activation' token %}" ><h2>Activation Link</h2></a></p>
<p> <a href="{% url 'accounts:reset-password-via-link' token %}" ><h2>Activation Link</h2></a></p>
{% endblock %}