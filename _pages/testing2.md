---
layout: page
permalink: /testing2/
title: Student Showcase Testing
description:
nav: false
nav_order: 
---

<style>
  hr.rounded {
  border-top: 5px solid #bbb;
  border-radius: 5px;
}

  sl-button.attribute::part(base) {
    border-radius: 0;
    background-color: #002868;
    color: white;
  }
  
  sl-button.attribute::part(base):hover {
    transform: scale(0) rotate(0deg);
  }

 .noHover{
    pointer-events: none;
 }
  
</style>
 
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
			    <br><h3 class="card-text"><i class="fa-solid fa-people-group"></i><b>&nbsp; Contributor(s):</b> {{ project.metadata.contributors | replace: '<br />', ', ' }}</h3><br>
                    {% endif %}
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
                    </p>
		    </div>
			{% if project.metadata.typeofdataadvocacy %}
      <sl-button class="attribute noHover">Type of Data Advocacy: {{ project.metadata.typeofdataadvocacy | replace: '<br />', ', ' }}</sl-button>
      {% endif %}
      
      {% if project.metadata.genre %}
      <sl-button class="attribute noHover">Genre: {{ project.metadata.genre | replace: '<br />', ', ' }}</sl-button>
      {% endif %}
      
      {% if project.metadata.filetype %}
      <sl-button class="attribute noHover">Format: {{ project.metadata.filetype | replace: '<br />', ', ' }}</sl-button>
      {% endif %}
		</div>
            </div>
      </div>
</p>

	{% endfor %}
<br>
{% endfor %}
