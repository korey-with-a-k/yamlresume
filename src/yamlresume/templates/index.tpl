% tlds = (".com", ".net", ".org", ".edu", ".us", ".app", ".dev", ".io", ".ai")
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Barlow">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.15.1/devicon.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
        <style>
            % include('style.tpl', **style)
        </style>
        <title>{{ full_name }}</title>
        % if defined('font_awesome_id'):
        <script src="https://kit.fontawesome.com/{{ font_awesome_id }}.js" crossorigin="anonymous"></script>
        % end
    </head>
    <body>
        <div id="sheet">
            <aside>
                <h1>{{ full_name }}</h1>
                <h2 class="current-job-title">{{ current_job_title }}</h2>
            % if defined('education'):
                <section>
                    <h3 class="sidebar-heading">Education</h3>
                % for item in education:
                    <div class="education-item">
                    % if item.degree:
                        <h4>{{ item.degree }}</h4>
                    % end
                    % if item.school:
                        <p>{{ item.school }}</p>
                    % end
                    % if item.start:
                        <p>{{ item.start }} - {{ item.end }}</p>
                    % end
                    % if item.gpa:
                        <p>GPA: {{ item.gpa }}</p>
                    % end
                    % if item.honor:
                        <p><em>{{ item.honor }}</em></p>
                    % end
                    </div>
                % end
                </section>
            % end
            % if defined('sidebar'):
            % for heading, items in sidebar.items():
                <section>
                    <h3 class="sidebar-heading">{{ heading.title() }}</h3>
                    <ul>
                    % for item in items:
                        <li>
                        % if item.icon:
                            <i class="{{ item.icon }} icon-fw"></i>
                        % end
                        % if item.path:
                            {{! item.svg }}
                        % end
                            {{ item.value }}
                        </li>
                    % end
                    </ul>
                </section>
            % end
            % end
            </aside>
            <main>
            % if defined('contact_info'):
                <header>
                    <ul class="contact">
                    % for item in contact_info.values():
                        <li>
                        % if item.link:
                            <a href="https://{{ item.link }}">
                        % end
                        % if item.icon:
                            <i class="{{ item.icon }} icon-fw"></i>
                        % end
                        % if item.path:
                            {{! item.svg }}
                        % end
                            {{ item.value }}
                        % if item.link:
                            </a>
                        % end
                        </li>
                    % end
                    </ul>
                % if defined('qr_code_svg'):
                    <a href="https://{{ qr_code.data }}">
                    {{! qr_code_svg }}
                    </a>
                % end
                </header>
            % end
            % if defined('main'):
            % for heading, items in main.items():
                <section>
                    <h2 class="primary">{{ heading.title() }}</h2>
                % for item in items:
                    <div class="main-item">
                        <h4>{{ item.title }}</h4>
                    % if item.details:
                        <div class="detail-row">
                        % for detail in item.details:
                        % link = any(tld in detail for tld in tlds)
                        % if link:
                            <a href="https://{{ detail }}">
                        % end
                            <p>{{ detail }}</p>
                        % if link:
                            </a>
                        % end
                        % end
                        </div>
                    % end
                    % if item.summary:
                        <p class="summary">{{ item.summary }}</p>
                    % end
                    % if item.highlights:
                        <ul>
                        % for highlight in item.highlights:
                            <li>{{ highlight }}</li>
                        % end
                        </ul>
                    % end
                    % if item.post_details:
                        <div class="detail-row">
                        % for detail in item.post_details:
                        % link = any(tld in detail for tld in tlds)
                        % if link:
                            <a href="https://{{ detail }}">
                        % end
                            <p>{{ detail }}</p>
                        % if link:
                            </a>
                        % end
                        % end
                        </div>
                    % end
                    </div>
                % end
                </section>
            % end
            % end
            </main>
        </div>
    </body>
</html>
