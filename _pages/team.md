---
layout: page
permalink: /team/
title: Data Advocacy for All Team
description:
nav: false
nav_rank: 8
---

{% assign groups = site.members | sort: "group_rank" | map: "group" | uniq %}

{% for group in groups %}

## {{ group }}

    {% assign members = site.members | sort: "lastname" | where: "group", group %}
    {% for member in members %}

<p>
    <div class="card {% if member.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="col-sm-4 col-md-3">
                <img src="{{ '/assets/img/' | append: member.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ member.profile.name }}" />
            </div>
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if member.inline == false %}<a href="{{ member.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ member.profile.name }}</h5>
                    {% if member.profile.position %}<h6 class="card-subtitle mb-2 text-muted">{{ member.profile.position }}</h6>{% endif %}
                    {% if member.profile.department %}<h6 class="card-subtitle mb-2 text-muted">{{ member.profile.department }}</h6>{% endif %}
                    {% if member.profile.organization %}<h6 class="card-subtitle mb-2 text-muted">{{ member.profile.organization }}</h6>{% endif %}
                    <p class="card-text">
                        {{ member.teaser }}
                    </p>
                    {% if member.inline == false %}</a>{% endif %}
                    {% if member.profile.website %}
                        <br><a href="{{ member.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                    {% endif %}
                    {% if member.profile.email %}
                        <a href="mailto:{{ member.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                    {% endif %}
                    {% if member.profile.phone %}
                        <a href="tel:{{ member.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                    {% endif %}
                    {% if member.profile.orcid %}
                        <a href="https://orcid.org/{{ member.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                    {% endif %}
                    {% if member.profile.twitter %}
                        <a href="https://twitter.com/{{ member.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                    {% endif %}
                    {% if member.profile.github %}
                        <a href="https://github.com/{{ member.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                    {% endif %}
                    <p class="card-text">
                        <span style="font-size: 0.875rem; display: block; padding-top: 0.7rem;"><i class="fas fa-building-columns"></i> {{ member.profile.address | replace: '<br />', ', ' }}</span> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

    {% endfor %}

<br>
{% endfor %}

## Advisory Board

<div class="row g-4">
  <div class="col-12 col-md-6">
    <div class="card" style="margin-bottom: 1rem;">
      <div class="card-body">
        <h5 class="card-title">Rachel Gross</h5>
        <p class="card-text">
          <i class="fas fa-university"></i> University of Colorado Denver
        </p>
      </div>
    </div>
    <div class="card" style="margin-bottom: 1rem;">
      <div class="card-body">
        <h5 class="card-title">Lindsay Poirier</h5>
        <p class="card-text">
          <i class="fas fa-university"></i> Smith College
        </p>
      </div>
    </div>
    <div class="card" style="margin-bottom: 1rem;">
      <div class="card-body">
        <h5 class="card-title">Urooj Raja</h5>
        <p class="card-text">
          <i class="fas fa-university"></i> Loyola University Chicago
        </p>
      </div>
    </div>
  </div>
  <div class="col-12 col-md-6">
    <div class="card" style="margin-bottom: 1rem;">
      <div class="card-body">
        <h5 class="card-title">Sara Stoudt</h5>
        <p class="card-text">
          <i class="fas fa-university"></i> Bucknell University
        </p>
      </div>
    </div>
    <div class="card" style="margin-bottom: 1rem;">
      <div class="card-body">
        <h5 class="card-title">Joanna Wolfe</h5>
        <p class="card-text">
          <i class="fas fa-university"></i> Carnegie Mellon University
        </p>
      </div>
    </div>
  </div>
</div>
