<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PNJ</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@100..900&display=swap');
        div.container {
            display: flex;
            width: 85vw;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        div.container div.element {
            flex: 1 0 24.3%;
            /* flex-grow: unset; */
            /* flex-shrink: unset; */
            border: 1px solid #A0A0A0;
            overflow: hidden;
        }

        div.container div.element img,
        div.container div.element div {
            width: 100%;
        }

        div.reversed {
            transform: rotate(180deg);
            padding-bottom: 12px;
            border-top: 1px solid black;
        }

        div.element h1,
        div.element h2,
        div.element h3 {
            margin: 0;
            font-family: "Lexend", Arial, sans;
        }

        div.name,
        div.occupation {
            text-align: center;
            padding: 3px 0;
        }

        div.carac {font-size: 16px;}
        div.desc {font-size: 14px;}

        div.container div.element div.carac, div.container div.element div.desc{width: 97%; margin: 0 auto;}
        div.container div.element div.desc{margin-top: 6px; }
        div.desc {text-align: justify; height: 152px;}
        div.desc span.unique {
            color: teal;
        }

        div.carac ul{height:48px; margin: 0; padding: 0; display: inline-flex; list-style: none; flex-wrap: wrap;}
        div.carac ul li{height: 16px;}
        div.carac ul li:nth-of-type(2n + 1){font-weight: bold; }
        div.carac ul li:nth-of-type(2n){margin:0 6px;}
        div.carac ul li:nth-of-type(8n){margin-right: 0;}
        div.carac ul li:nth-of-type(8n + 1){margin-left: 6px;}
        div.carac ul li{flex: 1 0 7%;}
    </style>
    <style media="print">
        @page{
            size: A4 landscape;
        }
        div.container { width: 28cm;}
        div.container div.element{width: 6.5cm; height: 19cm; margin-right: 6px;}
        div.container div.element:nth-of-type(4n){margin-right: 0;}
    </style>
</head>

<body>
    <div class="container">
        {% for character_name, character in characters.items() %}
        <div class="element">
            <div class="reversed">
                <div class="name"><h1>{{ character.shortname }}</h1></div>
                <img src="{{ character.pic }}" alt="">
            </div>
            <div class="name"><h2>{{ character_name }}</h2></div>
            <div class="occupation"><h3>{{ character.occupation }}</h3></div>
            <div class="carac">
                <ul>
                    {% for quality, value in character.qualities.items() -%}
                    <li>{{ quality }}</li><li>{{ value }}</li>
                    {%- endfor %}
                    <li>PV</li><li>{{ ((character.qualities['CON'] + character.qualities['TAI']) / 10) | int }}</li>
                    <li>PM</li><li>{{ (character.qualities['POU'] / 5) | int }}</li>
                </ul>
            </div>
            <div class="desc">
                {{- ", ".join(character.skills) -}}
                {%- if character.uniqueskills -%}
                    {%- for current_unique_skill in character.uniqueskills -%}
                    , <span class="unique">{{ current_unique_skill }}</span>
                    {%- endfor -%}
                {%- endif -%}
            </div>
        </div>
        {%- endfor %}
    </div>
</body>

</html>
