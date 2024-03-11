---
layout: page
permalink: /showcase/
title: Student Projects Showcase
description: 
nav: false
nav_rank: 5
---

{% comment %} 
{% assign groups = site.showcase | sort: "group_rank" | map: "group" | uniq %} 
{% endcomment %}

<!-- This Liquid command looks in the Collection "showcase" and sorts it by the variable specified in the frontmatter for each markdown file. 
It then maps them into buckets based on "group" defined in the frontmatter of each markdown file. 
We can adjust this as needed for different categories/designations. -->

{% assign groups = site.showcase | sort: "group_rank" | map: "group" | uniq %}

{% for group in groups %}

## {{ group }}

    {% assign showcase_items = site.showcase | sort: "group_rank" | where: "group", group %}
    {% for item in showcase_items %}
    
<p>
    <div class="card {% if item.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="col-sm-4 col-md-3">
                <img src="{{ '/assets/img/' | append: item.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ item.profile.name }}" />
            </div>
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    <h5 class="card-title">{{ item.title }}</h5>
                    {% if item.description %}<p class="card-subtitle mb-2 text-muted">{{ item.description }}</p>{% endif %}
                    <p class="card-text">
                        {{ item.teaser }}
                    </p>
                    {% if item.profile.website %}
                        <br><a href="{{ item.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                    {% endif %}
                    {% if item.profile.email %}
                        <a href="mailto:{{ item.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                    {% endif %}
                    {% if item.profile.phone %}
                        <a href="tel:{{ item.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                    {% endif %}
                    {% if item.profile.orcid %}
                        <a href="https://orcid.org/{{ item.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                    {% endif %}
                    {% if item.profile.twitter %}
                        <a href="https://twitter.com/{{ item.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                    {% endif %}
                    {% if item.profile.github %}
                        <a href="https://github.com/{{ item.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                    {% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-thumbtack"></i> {{ item.profile.address | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

    {% endfor %}
<br>
{% endfor %}
