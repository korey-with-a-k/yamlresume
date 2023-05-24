*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

a {
    text-decoration: none;
    color: inherit;
}

:root {
    --background-color: {{ background_color }};
    --dark-color: {{ dark_color }};
    --light-color: {{ light_color }};
    --primary-color: {{ primary_color }};
    --secondary-color: {{ secondary_color }};
    --heading-font: "{{ heading_font }}","sans-serif";
    --body-font: "{{ body_font }}","sans-serif";
}

.primary {
    color: var(--primary-color);
}

.secondary {
    color: var(--secondary-color);
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--heading-font);
    font-weight: normal;
    line-height: 1;
    text-transform: uppercase;
}

h1 {
    font-size: 40px;
    letter-spacing: 2px;
    word-spacing: 2px;
    line-height: 1.2;
% if not wrap_full_name:
    white-space: nowrap;
% end
}

h2 {
    font-size: 20px;
    letter-spacing: 1px;
    word-spacing: 2px;
}

h3 {
    font-size: 18px;
    letter-spacing: 1px;
}

h4, h5, h6 {
    font-family: var(--body-font);
    font-weight: bold;
    font-size: 16px;
    text-transform: none;
}

ul {
    list-style-type: "- ";
    padding-left: 0.6em;
}

.contact {
    padding-left: 0em;
}

li::marker {
    color: var(--primary-color);
}

body {
    background-color: var(--background-color);
    font-family: var(--body-font);
}

#sheet {
    display: flex;
    margin: 20px auto;
    height: 11in;
    width: 8.5in;
    box-shadow: 0 0.5mm 2mm rgb(0 0 0 / 30%);
}

aside {
    padding: 35px;
    width: min-content;
    background-color: var(--secondary-color);
    color: var(--light-color);
}

main {
    flex-grow: 1;
    padding-top: 35px;
    padding-left: 20px;
    padding-right: 40px;
    background-color: var(--light-color);
    color: var(--dark-color);
}

header {
    display: flex;
    justify-content: space-between;
}

section {
    margin-top: 20px;
}

.current-job-title {
    margin-top: 5px;
% if not wrap_current_job_title:
    white-space: nowrap;
% end
    color: var(--primary-color);
}

.sidebar-heading {
    margin-bottom: 5px;
    color: var(--primary-color);
}

.education-item ~ .education-item {
    margin-top: 10px;
}

aside li {
    margin-bottom: 2px;
}

aside i {
    margin-right: 2px;
}

.icon-fw {
    display: inline-block;
    width: 1.25em;
    text-align: center;
}

.contact li {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
    white-space: nowrap;
    list-style-type: none;
}

.contact a {
    display: flex;
    align-items: center;
}

.contact i {
    margin-right: 8px;
    color: var(--primary-color);
}

.main-item {
    margin-top: 10px;
}

.detail-row {
    display: flex;
    justify-content: space-between;
    color: var(--primary-color);
}

.summary {
    text-align: justify;
}

aside svg * {
    fill: var(--light-color);
}

aside svg {
    height: 16px;
    width: 1.25em;
    margin-right: 2px;
}

header svg * {
    fill: var(--primary-color);
}

.contact svg {
    height: 16px;
    width: 1.25em;
    margin-right: 5px;
}

.svg-dark {
    fill: var(--dark-color);
}

.svg-light {
    fill: var(--light-color);
}

.svg-primary {
    fill: var(--primary-color);
}

.svg-secondary {
    fill: var(--secondary-color);
}

@page {
    size: auto;
    margin: 0mm;
}

@media print {
    #sheet {
        margin: 0;
    }
}
