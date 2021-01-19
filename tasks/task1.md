# Task 1: Create an API Endpoint that Supports Uploading Images

## Steps
For this task, we want to create an API Endpoint for uploading images and a way so that whenever a new image is uploaded, it's shown on our webpage automatically w/o the user needing to refresh the page.

For example, if a user uploads images a, b, c, the webpage should show:
```
<file upload button>
<image a>
<image b>
<image c>
```

See places where there is "TASK 1" in comments in `templates/index.html`, `app.py`, and `static/js/script.js`.

We recommend first looking at all the files to think about where to start first. 

For example, would it make more sense to have our Javascript trigger our endpoint in Python or vice versa?

Some questions to think about:
* How can we store images in our server?
* How can we append to our existing HTML and save that state (in other words, when we refresh our webpage, our images should still be listed out)

## Testing
In addition to directly testing your API endpoint by testing your server on localhost after each changes, you can use PostMan to test your API Endpoint. 

## Goals
We want to be able to upload images and display them to the website in order of how it was uploaded. 

The design of how it looks on the website is up to you!

In the optional Task 2, you'll have a chance to style your webpage to your liking!

## Things to consider
Think about different edge cases:
* How do we only allow images (jpg, pngs, etc.) to be uploaded? (Ex: what happens if a user uploads a file)
* What if a user upoads a really large image?
* What if our API endpoint fails or cannot process an image?
* Where do we store uploaded images on our server?
* Should our Endpoint be a GET or POST request?

## Submission
That's it - congrats on finishing Task 1. If you want an extra challenge, move onto Task 2 (task2.md).

If you don't want to do Task 2, follow the submission.md file.
