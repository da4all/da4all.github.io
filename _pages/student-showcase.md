---
layout: page
permalink: /student-showcase/
title: Student Showcase
description:
nav: true
nav_order: 4
toc:
  sidebar: top
---

<style>
  hr.rounded {
  border-top: 1px solid #bbb;
  border-radius: 1px;
}

</style>

The resources from the Data Advocacy for All toolkit were piloted in several courses taught at the University of Colorado Boulder and University of Colorado Denver between 2023 to 2024. We’ve provided a showcase of student work from these courses in order to illustrate how these resources can be successfully applied in the classroom to help students learn how to build their own data advocacy projects.

{% assign groups = site.showcase | sort: "group_rank" | map: "group" | uniq %}

{% for group in groups %}

<div class="projects">
	<h2 class="category"> {{ group }} </h2>
</div>

    {% assign project = site.showcase | sort: "title" | where: "group", group %}
    {% for project in project %}

<p>
    <div class="card {% if project.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-7">
                <div class="card-body">
                    {% if project.inline == false %}<a href="{{ project.url | relative_url }}">{% endif %}
                    <h3 class="card-title">{{ project.title }}</h3>
                    {% if project.metadata.contributors %}
			    {% assign contributors_text = project.metadata.contributors | replace: '<br />', ', ' %}
			    <h4 class="card-text">
				    <i class="fa-solid fa-people-group"></i>
				    <b>&nbsp;{% if contributors_text contains " and " %}Contributors{% else %}Contributor{% endif %}:</b> {{ contributors_text }}
			    </h4>
			    {% endif %}
                    <p class="card-text">
			    <small><i>Created as part of {{ project.metadata.courseinfo | replace: '<br />', ', ' }}</i></small><br></p>
			    <hr class="rounded">
			    <p class="card-text">
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
                        <small class="test-muted"><i class="fa-solid fa-layer-group"></i><b>&nbsp; Type of Data Advocacy:</b> {{ project.metadata.typeofdataadvocacy | replace: '<br />', ', ' }}</small><br>
			{% endif %}
			{% if project.metadata.genre %}
			<small class="test-muted"><i class="fa-solid fa-bars-staggered"></i><b>&nbsp; Genre:</b> {{ project.metadata.genre | replace: '<br />', ', ' }}</small><br>
			{% endif %}
			{% if project.metadata.filetype %}
			<small class="test-muted"><i class="fa-solid fa-file"></i><b>&nbsp; Format:</b> {{ project.metadata.filetype | replace: '<br />', ', ' }}</small> <br>
			{% endif %}
			{% if project.metadata.source %}
			<small class="test-muted"><i class="fa-solid fa-link"></i><b>&nbsp; Also Published Here:</b> <a href="{{ project.metadata.source }}">{{ project.metadata.source }}</a></small><br>
			{% endif %}
			{% if project.metadata.license %}
			<small class="test-muted"><i class="fa-solid fa-quote-left"></i><b>&nbsp; License:</b> {{ project.metadata.license | replace: '<br />', ', ' }}</small> 
			{% endif %}
                    </p>
		    </div>
            </div>
            </div>
        </div>
</p>

    {% endfor %}

<br>
{% endfor %}
