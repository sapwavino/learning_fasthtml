from fasthtml.common import *
from fasthtml import Card
from fastcore.xtras import timed_cache


_blank = dict(target="_blank", rel="noopener noreferrer")
description = "Modern web applications in pure Python"

hdrs = [
    Meta(charset="UTF-8"),
    Meta(
        name="viewport",
        content="width=device-width, initial-scale=1.0, maximum-scale=1.0",
    ),
    Meta(name="description", content=description),
    # *Favicon("favicon.ico", "favicon-dark.ico"),
    # *Socials(
    #     title="FastHTML",
    #     description=description,
    #     site_name="fastht.ml",
    #     twitter_site="@answerdotai",
    #     image=f"/assets/og-sq.png",
    #     url="",
    # ),
    Link(href="css/main.css", rel="stylesheet"),
    Link(href="css/tailwind.css", rel="stylesheet"),
    # Link(href="css/preview-stack.css", rel="stylesheet"),
    # Link(href="css/highlighter-theme.css", rel="stylesheet"),
]

scripts = [
    Script(src="https://cdn.tailwindcss.com"),
]

app, rt = fast_app(live=True,hdrs=hdrs)



def benefit(title, content):
    return Div(
        H3(title, cls=f"text-black heading-3"),
        P(content, cls=f"l-body mt-6 lg:mt-6"),
        cls="w-1/2 p-6 bg-red-500 rounded-2xl xl:p-12 lg:h-[22rem] lg:w-[26rem] shadow-lg",
    )


# @timed_cache(seconds=60)
@rt("/")
def get():
    return (
        Main(
            Title("Hello"),
            benefit("A new bensfsefit", "This is asasa new benefidaadaaaaaaaat"),
            # cls=f"w-full flex flex-col items-center justify-center min-h-screen"
            # **scripts,
        ),
    )


serve(reload=True)
