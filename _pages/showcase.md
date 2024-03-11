---
layout: page
permalink: /showcase/
title: Showcases
description: 
nav: false
nav_rank: 10
---

# Version 1: 

<br>

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
            <div class="team col-sm-8 col-md-7">
                <div class="card-body">
                    {% if project.inline == false %}<a href="{{ project.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ project.profile.title }}</h5>
                    <p class="card-text">
                        {{ project.teaser }}
			    <small><br><br></small>
                    </p>
                    {% if project.inline == false %}</a>{% endif %}
                    <p class="card-text">
			<small class="test-muted"><i class="fa-solid fa-people-group"></i><b>&nbsp; Contributors:</b> {{ project.profile.contributors | replace: '<br />', ', ' }}</small> 
                        <br><small class="test-muted"><i class="fa-solid fa-layer-group"></i><b>&nbsp; Type of Data Advocacy:</b> {{ project.profile.topic | replace: '<br />', ', ' }}</small> 
			<br><small class="test-muted">&nbsp;<i class="fa-solid fa-file"></i><b>&nbsp; Medium of Project:</b> {{ project.profile.filetype | replace: '<br />', ', ' }}</small> 
			<br><small class="test-muted"><i class="fa-solid fa-link"></i><b>&nbsp; Also Published Here:</b> <a href="{{ project.profile.source }}">{{ project.profile.source }}</a></small>
                    </p>
                </div></div>
		<div class="col-sm-4 col-md-5">
                <img src="{{ '/assets/img/' | append: project.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ project.profile.caption }}" />
            </div>
            </div>
        </div>
</p>

	{% endfor %}
<br>
{% endfor %}

# Version 2: 

<br>

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
            <div class="team col-sm-8 col-md-7">
                <div class="card-body">
                    {% if project.inline == false %}<a href="{{ project.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ project.profile.title }}</h5>
                    <p class="card-text">
                        {{ project.teaser }}
			    <small><br><br></small>
                    </p>
                    {% if project.inline == false %}</a>{% endif %}
                </div></div>
		<div class="col-sm-4 col-md-5">
                <img src="{{ '/assets/img/' | append: project.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ project.profile.caption }}" />
                    <div class="card-body" style="margin: 10px;">
			<p class="card-text">
			<small class="test-muted"><i class="fa-solid fa-people-group"></i><b>&nbsp; Contributors:</b> {{ project.profile.contributors | replace: '<br />', ', ' }}</small> 
                        <br><small class="test-muted"><i class="fa-solid fa-layer-group"></i><b>&nbsp; Type of Data Advocacy:</b> {{ project.profile.topic | replace: '<br />', ', ' }}</small> 
			<br><small class="test-muted">&nbsp;<i class="fa-solid fa-file"></i><b>&nbsp; Medium of Project:</b> {{ project.profile.filetype | replace: '<br />', ', ' }}</small> 
			<br><small class="test-muted"><i class="fa-solid fa-link"></i><b>&nbsp; Also Published Here:</b> <a href="{{ project.profile.source }}">{{ project.profile.source }}</a></small>
                    </p>
		    </div>
            </div>
            </div>
        </div>
</p>

	{% endfor %}
<br>
{% endfor %}
