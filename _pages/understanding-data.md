---
layout: page
permalink: /understanding-data/
title: Understanding Data
description: 
nav: false
nav_rank: 8
---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.5.2/cdn/themes/light.css" />
<script type="module" src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.5.2/cdn/shoelace.js" ></script>

## Overview

“Understanding data” is a crucial literacy domain for helping students develop the critical, ethical, and rhetorical impulses needed to define data; understand its complicated relations to power, privilege, oppression, and liberation; and imagine ethical and responsible ways of working with data toward more just futures.

The resources offered under this literacy domain push students to ask critical questions about data such as:
- What is “data”?
- How and why does data ethically matter?
- What critical habits toward data are important to develop?
- What rhetorical dimensions of data need to be considered?
- What is data advocacy? And how can we do data advocacy ethically and responsibly?

<!--DEFINING DATA -->

<details>
<summary>Defining Data</summary>

<div style="height:5px;font-size:1px;">&nbsp;</div>
      <sl-button-group label="Alignment">
        <sl-button href="../defining-data/">Go to the "Defining Data" overview page</sl-button>
      </sl-button-group>



<div style="height:1px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Reading" and "Defining Data" -->

<details>
<summary> Readings </summary>

{% assign cards = site.cards | where: "group", "Reading" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Term" and "Defining Data" -->

<details>
<summary> Glossary </summary>

{% assign cards = site.cards | where: "group", "Term" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Assignment" and "Defining Data" -->

<details>
<summary> Assignments </summary>

{% assign cards = site.cards | where: "group", "Assignment" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Activity" and "Defining Data" -->

<details>
<summary> Activities </summary>

{% assign cards = site.cards | where: "group", "Activity" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Tutorial" and "Defining Data" -->

<details>
<summary> Tutorials </summary>

{% assign cards = site.cards | where: "group", "Tutorial" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Teaching Modules" and "Defining Data" -->

<details>
<summary> Teaching Modules </summary>

{% assign cards = site.cards | where: "group", "Teaching Module" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--This section filters by "Dataset" and "Defining Data" -->

<details>
<summary> Datasets </summary>

{% assign cards = site.cards | where: "group", "Datasets" | where: "topic", "Defining Data" | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>


</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--CRITIQUING DATA -->

<details>
<summary>Critiquing Data</summary>
Organized cards will go here.</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--ACTING ETHICALLY WITH DATA -->

<details>
<summary>Acting Ethically with Data</summary>
Organized cards will go here.</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

<!--LINKING DATA AND JUSTICE-->

<details>
<summary>Linking Data and Justice</summary>
Organized cards will go here.</details>
