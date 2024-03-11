---
layout: page
permalink: /showcase/
title: Student Showcase Projects
description: Here is a sample description for this page.
nav: false
nav_rank: 8
---

{% comment %} 
{% assign groups = site.showcase | sort: "group_rank" | map: "group" | uniq %} 
{% endcomment %}

{% assign groups = site.showcase | sort: "title" | map: "group" | uniq %}

{% for group in groups %}

## {{ group }}

	{% assign showcases = site.showcase | sort: "title" | where: "group", group %}
	{% for showcase in showcases %}


<p>
    <div class="card {% if showcase.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="col-sm-4 col-md-3">
                <img src="{{ '/assets/img/' | append: showcase.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ showcase.profile.name }}" />
            </div>
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if showcase.inline == false %}<a href="{{ showcase.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ showcase.profile.name }}</h5>
                    {% if showcase.profile.position %}<h6 class="card-subtitle mb-2 text-muted">{{ showcase.profile.position }}</h6>{% endif %}
                    {% if showcase.profile.department %}<h6 class="card-subtitle mb-2 text-muted">{{ showcase.profile.department }}</h6>{% endif %}
                    {% if showcase.profile.organization %}<h6 class="card-subtitle mb-2 text-muted">{{ showcase.profile.organization }}</h6>{% endif %}
                    <p class="card-text">
                        {{ showcase.teaser }}
                    </p>
                    {% if showcase.inline == false %}</a>{% endif %}
                    {% if showcase.profile.website %}
                        <br><a href="{{ showcase.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                    {% endif %}
                    {% if showcase.profile.email %}
                        <a href="mailto:{{ showcase.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                    {% endif %}
                    {% if showcase.profile.phone %}
                        <a href="tel:{{ showcase.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                    {% endif %}
                    {% if showcase.profile.orcid %}
                        <a href="https://orcid.org/{{ showcase.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                    {% endif %}
                    {% if showcase.profile.twitter %}
                        <a href="https://twitter.com/{{ showcase.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                    {% endif %}
                    {% if showcase.profile.github %}
                        <a href="https://github.com/{{ showcase.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                    {% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-thumbtack"></i> {{ showcase.profile.address | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

	{% endfor %}
<br>
{% endfor %}

