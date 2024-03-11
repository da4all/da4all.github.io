---
layout: page
permalink: /showcase/
title: Showcase
description: 
nav: true
nav_rank: 10
---

{% comment %} 
{% assign groups = site.showcase | sort: "group_rank" | map: "group" | uniq %} 
{% endcomment %}

{% assign groups = site.showcase | sort: "title" | map: "group" | uniq %}

{% for group in groups %}

## {{ group }}

	{% assign project = site.showcase | sort: "title" | where: "group", group %}
	{% for project in project %}


<p>
    <div class="card {% if project.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="col-sm-4 col-md-6">
                <img src="{{ '/assets/img/' | append: project.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ project.profile.name }}" />
		    <p class="card-text">
                        {{ project.profile.caption }}</p>
            </div>
            <div class="team col-sm-8 col-md-6">
                <div class="card-body">
                    {% if project.inline == false %}<a href="{{ project.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ project.profile.name }}</h5>
                    <p class="card-text">
                        {{ project.teaser }}
                    </p>
                    {% if project.inline == false %}</a>{% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-thumbtack"></i> {{ project.profile.address | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

	{% endfor %}
<br>
{% endfor %}
