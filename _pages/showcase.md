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

<!--this Liquid command looks in the Collection "projects" that was created through a directory named projects + adding it as a collection in _config.yml file. It sorts it by the variable you specify in teh frontmatter for each project markdown file - ex. group_rank, lastname, etc. The map command then puts them into a few buckets based on  "group" - defined in the frontmatter of each of the individual project pages - ex. "Principal Investigators". It goes through and only looks at unique values for all pages listed in here. We can change this and/or add different categories/designations - ex. "Faculty" "Researchers" etc. or a "school" category for "University of Colorado Denver" "CU Boulder" etc.  -->

{% assign groups = site.showcase | sort: "title" | map: "group" | uniq %}

{% for group in groups %}

## {{ group }}

	{% assign project = site.showcase | sort: "title" | where: "group", group %}
	{% for project in project %}


<p>
    <div class="card {% if project.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="col-sm-4 col-md-3">
                <img src="{{ '/assets/img/' | append: project.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ project.profile.name }}" />
		    <p class="card-text">
                        {{ project.profile.caption }}</p>
            </div>
            <div class="team col-sm-8 col-md-9">
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


