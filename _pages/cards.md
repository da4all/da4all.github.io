---
layout: page
permalink: /cards/
title: Data Advocacy Card System
description: 
nav: false
nav_rank: 8
---

# Data Justice Assignment:

{% assign cards = site.cards | where: "group", "Assignment" | where: "topic", "DataJustice" | sort: "last_name" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
		    {% if card.profile.group %}<h6 class="card-subtitle mb-2 text-muted">Type: {{ card.profile.group }}</h6>{% endif %}
                    {% if card.profile.literacy %}<h6 class="card-subtitle mb-2 text-muted">Literacy: {{ card.profile.literacy }}</h6>{% endif %}
                    {% if card.profile.position %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.position }}</h6>{% endif %}
                    {% if card.profile.department %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.department }}</h6>{% endif %}
                    {% if card.profile.organization %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.organization }}</h6>{% endif %}
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    {% if card.profile.website %}
                        <br><a href="{{ card.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                    {% endif %}
                    {% if card.profile.email %}
                        <a href="mailto:{{ card.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                    {% endif %}
                    {% if card.profile.phone %}
                        <a href="tel:{{ card.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                    {% endif %}
                    {% if card.profile.orcid %}
                        <a href="https://orcid.org/{{ card.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                    {% endif %}
                    {% if card.profile.twitter %}
                        <a href="https://twitter.com/{{ card.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                    {% endif %}
                    {% if card.profile.github %}
                        <a href="https://github.com/{{ card.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                    {% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-thumbtack"></i> {{ card.profile.address | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br>

# Data Justice:

{% assign cards = site.cards | where: "topic", "DataJustice" | sort: "last_name" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
		    {% if card.profile.group %}<h6 class="card-subtitle mb-2 text-muted">Type: {{ card.profile.group }}</h6>{% endif %}
                    {% if card.profile.literacy %}<h6 class="card-subtitle mb-2 text-muted">Literacy: {{ card.profile.literacy }}</h6>{% endif %}
                    {% if card.profile.position %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.position }}</h6>{% endif %}
                    {% if card.profile.department %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.department }}</h6>{% endif %}
                    {% if card.profile.organization %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.organization }}</h6>{% endif %}
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    {% if card.profile.website %}
                        <br><a href="{{ card.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                    {% endif %}
                    {% if card.profile.email %}
                        <a href="mailto:{{ card.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                    {% endif %}
                    {% if card.profile.phone %}
                        <a href="tel:{{ card.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                    {% endif %}
                    {% if card.profile.orcid %}
                        <a href="https://orcid.org/{{ card.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                    {% endif %}
                    {% if card.profile.twitter %}
                        <a href="https://twitter.com/{{ card.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                    {% endif %}
                    {% if card.profile.github %}
                        <a href="https://github.com/{{ card.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                    {% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-thumbtack"></i> {{ card.profile.address | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br>

# Assignments:
{% assign cards = site.cards | where: "group", "Assignment" | sort: "last_name" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
		    {% if card.profile.group %}<h6 class="card-subtitle mb-2 text-muted">Type: {{ card.profile.group }}</h6>{% endif %}
                    {% if card.profile.literacy %}<h6 class="card-subtitle mb-2 text-muted">Literacy: {{ card.profile.literacy }}</h6>{% endif %}
                    {% if card.profile.position %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.position }}</h6>{% endif %}
                    {% if card.profile.department %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.department }}</h6>{% endif %}
                    {% if card.profile.organization %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.organization }}</h6>{% endif %}
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    {% if card.profile.website %}
                        <br><a href="{{ card.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                    {% endif %}
                    {% if card.profile.email %}
                        <a href="mailto:{{ card.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                    {% endif %}
                    {% if card.profile.phone %}
                        <a href="tel:{{ card.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                    {% endif %}
                    {% if card.profile.orcid %}
                        <a href="https://orcid.org/{{ card.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                    {% endif %}
                    {% if card.profile.twitter %}
                        <a href="https://twitter.com/{{ card.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                    {% endif %}
                    {% if card.profile.github %}
                        <a href="https://github.com/{{ card.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                    {% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-thumbtack"></i> {{ card.profile.address | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<br>

# All Cards:
{% comment %} 
{% assign groups = site.cards | sort: "group_rank" | map: "group" | uniq %} 
{% endcomment %}

<!--this Liquid command looks in the Collection "cards" that was created through a directory named cards + adding it as a collection in _config.yml file. It sorts it by the variable you specify in teh frontmatter for each card markdown file - ex. group_rank, lastname, etc. The map command then puts them into a few buckets based on  "group" - defined in the frontmatter of each of the individual card pages - ex. "Principal Investigators". It goes through and only looks at unique values for all pages listed in here. We can change this and/or add different categories/designations - ex. "Faculty" "Researchers" etc. or a "school" category for "University of Colorado Denver" "CU Boulder" etc.  -->

{% assign groups = site.cards | sort: "lastname" | map: "group" | uniq %}

{% for group in groups %}

## {{ group }}

	{% assign cards = site.cards | sort: "last_name" | where: "group", group %}
	{% for card in cards %}


<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team col-sm-8 col-md-9">
                <div class="card-body">
                    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
                    <h5 class="card-title">{{ card.profile.name }}</h5>
		    {% if card.profile.group %}<h6 class="card-subtitle mb-2 text-muted">Type: {{ card.profile.group }}</h6>{% endif %}
                    {% if card.profile.literacy %}<h6 class="card-subtitle mb-2 text-muted">Literacy: {{ card.profile.literacy }}</h6>{% endif %}
                    {% if card.profile.position %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.position }}</h6>{% endif %}
                    {% if card.profile.department %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.department }}</h6>{% endif %}
                    {% if card.profile.organization %}<h6 class="card-subtitle mb-2 text-muted">{{ card.profile.organization }}</h6>{% endif %}
                    <p class="card-text">
                        {{ card.teaser }}
                    </p>
                    {% if card.inline == false %}</a>{% endif %}
                    {% if card.profile.website %}
                        <br><a href="{{ card.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                    {% endif %}
                    {% if card.profile.email %}
                        <a href="mailto:{{ card.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                    {% endif %}
                    {% if card.profile.phone %}
                        <a href="tel:{{ card.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                    {% endif %}
                    {% if card.profile.orcid %}
                        <a href="https://orcid.org/{{ card.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                    {% endif %}
                    {% if card.profile.twitter %}
                        <a href="https://twitter.com/{{ card.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                    {% endif %}
                    {% if card.profile.github %}
                        <a href="https://github.com/{{ card.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                    {% endif %}
                    <p class="card-text">
                        <br><small class="test-muted"><i class="fas fa-thumbtack"></i> {{ card.profile.address | replace: '<br />', ', ' }}</small> 
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

	{% endfor %}
<br>
{% endfor %}

