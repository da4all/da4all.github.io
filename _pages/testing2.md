---
layout: page
permalink: /testing2/
title: Student Showcase Testing
description: This page showcases student data advocacy projects to demonstrate the types and potentials of projects afforded by the resources in the Data Advocacy for All Toolkit.
nav: false
nav_order: 6
---
 
{% assign groups = site.showcase | sort: "group_rank" | map: "group" | uniq %} 

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
                    <h5 class="card-title">{{ project.title }}</h5>
                    {% if project.metadata.contributors %}
			    {% assign contributors_text = project.metadata.contributors | replace: '<br />', ', ' %}
			    <br>
			    <h3 class="card-text">
				    <i class="fa-solid fa-people-group"></i>
				    <b>&nbsp; {% if contributors_text contains " and " %}Contributors{% else %}Contributor{% endif %}:</b> 
				    {{ contributors_text }}
			    </h3>
			    {% endif %}
                    <p class="card-text">
			    <small><i>{{ project.metadata.courseinfo | replace: '<br />', ', ' }}</i></small><br><br>
			    {{ project.teaser }}
			    <small><br><br></small>
                    </p>
                    {% if project.inline == false %}</a>{% endif %}
                </div></div>
		<div class="col-sm-4 col-md-5">
                <br>{% if project.inline == false %}<a href="{{ project.url | relative_url }}">{% endif %}<img src="{{ '/assets/img/' | append: project.metadata.image | relative_url }}" class="card-img img-fluid max-width: 80%" alt="{{ project.metadata.caption }}" />{% if project.inline == false %}</a>{% endif %}
                    <div class="card-body" style="margin: 2px;">
			<p class="card-text">
			{% if project.metadata.typeofdataadvocacy %}
                        <small class="test-muted"><i class="fa-solid fa-layer-group"></i><b>&nbsp; Type of Data Advocacy:</b> {{ project.metadata.typeofdataadvocacy | replace: '<br />', ', ' }}</small><br><br>
			{% endif %}
			{% if project.metadata.genre %}
			<small class="test-muted"><i class="fa-solid fa-bars-staggered"></i><b>&nbsp; Genre:</b> {{ project.metadata.genre | replace: '<br />', ', ' }}</small><br><br>
			{% endif %}
			{% if project.metadata.filetype %}
			<small class="test-muted">&nbsp;<i class="fa-solid fa-file"></i><b>&nbsp; Format:</b> {{ project.metadata.filetype | replace: '<br />', ', ' }}</small> <br><br>
			{% endif %}
			{% if project.metadata.source %}
			<small class="test-muted"><i class="fa-solid fa-link"></i><b>&nbsp; Also Published Here:</b> <a href="{{ project.metadata.source }}">{{ project.metadata.source }}</a></small><br><br>
			{% endif %}
			<small class="test-muted">&nbsp;<i class="fa-solid fa-quote-left"></i><b>&nbsp; License:</b> {{ project.metadata.license | replace: '<br />', ', ' }}</small> 
                    </p>
		    </div>
            </div>
            </div>
        </div>
</p>

	{% endfor %}
<br>
{% endfor %}
