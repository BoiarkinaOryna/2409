import flask

main_app = flask.Flask(
    import_name = "main",
    static_url_path = "/main/",
    template_folder = "templates"
)
