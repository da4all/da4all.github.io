---
layout: page
permalink: /defining-data/
title: Defining Data
description: 
nav: false
nav_rank: 8
---

<head>

<style>
.collapsible:after {
  content: '\02795'; /* Unicode character for "plus" sign (+) */
  font-size: 13px;
  color: white;
  float: right;
  margin-left: 5px;
}

.active:after {
  content: "\2796"; /* Unicode character for "minus" sign (-) */
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}
	
</style>

</head>

# Collapsibles

<body>
<button type="button" class="collapsible">Open Collapsible</button>
<div class="content">
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>

<p>Collapsible Set:</p>
<button type="button" class="collapsible">Open Section 1</button>
<div class="content">
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>
<button type="button" class="collapsible">Open Section 2</button>
<div class="content">
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>
<button type="button" class="collapsible">Open Section 3</button>
<div class="content">
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>

</body>

<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>

# HTML

<div class="panel-group">
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" href="#collapse1">Collapsible panel</a>
      </h4>
    </div>
    <div id="collapse1" class="panel-collapse collapse">
      <div class="panel-body">Panel Body</div>
      <div class="panel-footer">Panel Footer</div>
    </div>
  </div>
</div>

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
