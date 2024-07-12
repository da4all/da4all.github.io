---
layout: default
---

<style>
  hr.rounded {
  border-top: 5px solid #bbb;
  border-radius: 5px;
}

  sl-button.attribute::part(base):hover {
    transform: scale(0) rotate(0deg);
  }

 .noHover{
    pointer-events: none;
 }
  
</style>

<div class="page">
  <header class="page-header">
    <h1 class="page-title">{{ page.title }}</h1><br>
    <h4><b>Contributor(s):</b> {{ page.metadata.contributors | replace: '<br />', ', ' }}</h4>
  </header>

<br>

{% if page.metadata.typeofdataadvocacy %}
<sl-button class="attribute noHover">Type of Data Advocacy: {{ page.metadata.typeofdataadvocacy | replace: '<br />', ', ' }}</sl-button>
{% endif %}

{% if page.metadata.genre %}
<sl-button class="attribute noHover">Genre: {{ page.metadata.genre | replace: '<br />', ', ' }}</sl-button>
{% endif %}

{% if page.metadata.filetype %}<sl-button class="attribute noHover">Format: {{ page.metadata.filetype | replace: '<br />', ', ' }}</sl-button>{% endif %}

<br><br>

  <article>{{ content }}</article>

  <hr class="rounded">
  <br>

  <h2>Project Overview:</h2>

    <div class="row no-gutters">
      <div class="team col-sm-8 col-md-7">
        <div class="card-body">
          <p class="post-description" style="font-size: 14px">{{ page.teaser }}</p>
          {% if page.metadata.typeofdataadvocacy %}<sl-button class="attribute noHover" size="small">Type of Data Advocacy: {{ page.metadata.typeofdataadvocacy | replace: '<br />', ', ' }}</sl-button><br><br>{% endif %}
          {% if page.metadata.genre %}<sl-button class="attribute noHover" size="small">Genre: {{ page.metadata.genre | replace: '<br />', ', ' }}</sl-button><br><br>{% endif %}
          {% if page.metadata.filetype %}<sl-button class="attribute noHover" size="small">Format: {{ page.metadata.filetype | replace: '<br />', ', ' }}</sl-button><br><br>{% endif %}
        </div>
      </div>
      <div class="col-sm-4 col-md-5">
      <div class="page-info" style="background-color: #f2f2f2; padding: 2px">
      <img src="{{ '/assets/img/' | append: page.metadata.image | relative_url }}" class="card-img img-fluid" alt="{{ page.metadata.caption }}" /><br>
        <div class="card-body">
          <p style="font-size: 12px">
            <b>Caption:</b> {{ page.metadata.caption | replace: '<br />', ', ' }}</p></div>
        </div>
        <br>
            <p><br>{% if page.metadata.source %}<small class="test-muted"><i class="fa-solid fa-link"></i><b>&nbsp; Also Published Here:</b> <a href="{{ page.metadata.source }}">{{ page.metadata.source }}</a></small>{% endif %}</p>
      </div>
    </div>
    
</div>
