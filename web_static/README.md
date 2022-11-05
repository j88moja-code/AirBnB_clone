# Web Static

Now that a command interpreter for managing your AirBnB objects has been, it’s time to make them alive!

Before developing a big and complex web application, in this part of the prject the front end was built step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, the repository `AirBnB_clone` was forked from my partner as I was the contributor during the previous project.

## Contents

- [images](https://github.com/j88moja-code/AirBnB_clone/tree/main/web_static/images) - contains the images used in the project (logo on the header of index.html file from task 3).
- [styles](https://github.com/j88moja-code/AirBnB_clone/tree/main/web_static/styles) - the CSS styles written for different tasks of this phase of the project.
- [0-index.html](https://github.com/j88moja-code/AirBnB_clone/blob/main/web_static/0-index.html) - an HTML page that displays a header and a footer.

  Layout:

  - Body:
    - no margin
    - no padding
  - Header:
    - color #FF0000 (red)
    - height: 70px
    - width: 100%
  - Footer:

    - color #00FF00 (green)
    - height: 60px
    - width: 100%
    - text `Best School` center vertically and horizontally
    - always at the bottom at the page

    Requirements:

        - You must use the `header` and `footer` tags
        - You are not allowed to import any files
        - You are not allowed to use the `style` tag in the `head` tag
        - Use inline styling for all your tags

* [1-index.html](https://github.com/j88moja-code/AirBnB_clone/blob/main/web_static/1-index.html) - an HTML page that displays a header and a footer by using the `style` tag in the `head` tag (same as `0-index.html`)

  Requirements:

        * You must use the header and footer tags
        * You are not allowed to import any files
        * No inline styling
        * You must use the style tag in the head tag

  The layout must be exactly the same as `0-index.html`

* [2-index.html](https://github.com/j88moja-code/AirBnB_clone/blob/main/web_static/2-index.html) - an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

  Requirements:

        * You must use the header and footer tags
        * No inline styling
        * You must have 3 CSS files:
            * `styles/2-common.css`: for global style (i.e. the `body` style)
            * `styles/2-header.css`: for header style
            * `styles/2-footer.css`: for footer style
        The layout must be exactly the same as `1-index.html`

* [3-index.html](https://github.com/j88moja-code/AirBnB_clone/blob/main/web_static/3-index.html) - an HTML page that displays a header and footer by using CSS files (same as `2-index.html`)

  Layout:

  - Common:
    _ no margin
    _ no padding
    _ font color: #484848
    _ font size: 14px
    _ font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif`;
    _ icon in the browser tab
  - Header:
    _ color: white
    _ height: 70px
    _ width: 100%
    _ border bottom 1px #CCCCCC \* logo align on left and center vertically (20px space at the left)
  - Footer:
    _ color white
    _ height: 60px
    _ width: 100%
    _ border top 1px #CCCCCC
    _ text Best School center vertically and horizontally
    _ always at the bottom at the page
  - Requirements:

          * No inline style
          * You are not allowed to use the `img` tag
          * You are not allowed to use the `style` tag in the `head` tag
          * All images must be stored in the `images` folder
          * You must have 3 CSS files:
              * `styles/3-common.css`: for the global style (i.e `body` style)
              * `styles/3-header.css`: for the header style
              * `styles/3-footer.css`: for the footer style

* [4-index.html](https://github.com/j88moja-code/AirBnB_clone/blob/main/web_static/4-index.html) - an HTML page that displays a header, footer and a filters box with a search button.

  Layout: (based on 3-index.html)

  - Container:
    - between header and footer tags, add a div:
    - classname: container
    - max width 1000px
    - margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
    - center horizontally
  - Filter section:
    - tag section
    - classname filters
    - inside the .container
    - color white
    - height: 70px
    - width: 100% of the container
    - border 1px #DDDDDD with radius 4px
  - Button search:

    - tag button
    - text Search
    - font size: 18px
    - inside the section filters
    - background color #FF5A5F
    - text color #FFFFFF
    - height: 48px
    - width: 20% of the section filters
    - no borders
    - border radius: 4px
    - center vertically and at 30px of the right border
    - change opacity to 90% when the mouse is on the button

  - Requirements:

           - You must use: `header`, `footer`, `section`, `button` tags
           - No inline style
           - You are not allowed to use the `img` tag
           - You are not allowed to use the style tag in the head tag
           - All images must be stored in the `images` folder
           - You must have 4 CSS files:
               - `styles/4-common.css`: for the global style (`body` and `.container` styles)
               - `styles/3-header.css`: for the header style
               - `styles/3-footer.css`: for the footer style
               - `styles/4-filters.css`: for the filters style
               - `4-index.html` won’t be W3C valid, don’t worry, it’s temporary

* [5-index.html](https://github.com/j88moja-code/AirBnB_clone/blob/main/web_static/5-index.html) - an HTML page that displays a header, footer and a filters box.

  - Layout: (based on `4-index.html`)

  - Locations and Amenities filters:
    - tag: div
    - classname: locations for location tag and amenities for the other
    - inside the section filters (same level as the button Search)
    - height: 100% of the section filters
    - width: 25% of the section filters
    - border right #DDDDDD 1px only for the first left filter
  - contains a title:
    - tag: h3
    - font weight: 600
    - text States or Amenities
  - contains a subtitle:
    - tag: h4
    - font weight: 400
    - font size: 14px
    - text with fake contents
  - Requirements:

            - You must use: header, footer, section, button, h3, h4 tags
            - No inline style
            - You are not allowed to use the img tag
            - You are not allowed to use the style tag in the head tag
            - All images must be stored in the images folder
            - You must have 4 CSS files:
                - styles/4-common.css: for the global style (body and .container styles)
                - styles/3-header.css: for the header style
                - styles/3-footer.css: for the footer style
                - styles/5-filters.css: for the filters style

* [6-index.html]() - an HTML page that displays a header, footer and a filters box with dropdown.

  Layout: (based on 5-index.html)

  - Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
    - tag `ul`
    - classname popover
    - text should be fake now
    - inside each `div`
    - not displayed by default
    - color #FAFAFA
    - width same as the `div` filter
    - border #DDDDDD 1px with border radius 4px
    - no list display
    - Location filter has 2 levels of `ul`/`li`:
      - state -> cities
      - state name must be display in a `h2` tag (font size 16px)
  - Requirements:

    - You must use: header, footer, section, button, h3, h4, ul, li tags
    - No inline style
    - You are not allowed to use the img tag
    - You are not allowed to use the style tag in the head tag
    - All images must be stored in the images folder
    - You must have 4 CSS files:
      - `styles/4-common.css`: for the global style (`body` and `.container` styles)
      - `styles/3-header.css`: for the header style
      - `styles/3-footer.css`: for the footer style
      - `styles/6-filters.css`: for the filters style