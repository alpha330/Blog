{% extends "mail_templated/base.tpl" %}

{% block subject %}
User Activation
{% endblock %}

{% block html %}
<p> <a href="{% url 'accounts:verify-account' token %}" ><h2>Activation Link</h2></a></p>
{% endblock %}