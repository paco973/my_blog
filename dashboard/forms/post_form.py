from django.db import models
from app.models.category import Category
from app.models.tag import Tag
from user_profile.models import User
from my_blog.middleware import get_current_user
from app.models.post_view import PostView

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_current_user, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def view(self):
        return len(PostView.objects.filter(posts=self))

    écrit moi le django model en pansant a bien garder les attrinut de ce model et ce code html:

            model:
        from django.db import models
from .post_view import PostView
from app.models.category import Category
from app.models.tag import Tag
from user_profile.models import User
from my_blog.middleware import get_current_user


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user())
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_current_user(), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def view(self) -> int:
        return len(PostView.objects.filter(posts=self))


code html:

        <form>
        <!-- Main form -->
        <div class="row">
        <div class="col-12">
        <!-- Post name -->
        <div class="mb-3">
        <label class="form-label">Post name</label>
                    <input required id="con-name" name="name" type="text" class="form-control" placeholder="Post name">
                    <small>Moving heaven divide two sea female great midst spirit</small>
        </div>
        </div>
          <!-- Post type START -->
        <div class="col-12">
        <div class="mb-3">
        <label class="form-label">Post type</label>
                    <div class="d-flex flex-wrap gap-3">
        <!-- Post type item -->
        <div class="flex-fill">
        <input type="radio" class="btn-check" name="poll" id="option">
                        <label class="btn btn-outline-light w-100" for="option">
        <i class="bi bi-chat-left-text fs-1"></i>
                          <span class="d-block"> Post </span>
        </label>
        </div>
          <!-- Post type item -->
        <div class="flex-fill">
        <input type="radio" class="btn-check" name="poll" id="option2">
                        <label class="btn btn-outline-light w-100" for="option2">
        <i class="bi bi-patch-question fs-1"></i>
        <span class="d-block"> Question </span>
                        </label>
        </div>
          <!-- Post type item -->
        <div class="flex-fill">
        <input type="radio" class="btn-check" name="poll" id="option3" checked>
                        <label class="btn btn-outline-light w-100" for="option3">
        <i class="bi bi-chat-right-dots fs-1"></i>
                          <span class="d-block"> Poll </span>
        </label>
        </div>
          <!-- Post type item -->
        <div class="flex-fill">
        <input type="radio" class="btn-check" name="poll" id="option4">
                        <label class="btn btn-outline-light w-100" for="option4">
        <i class="bi bi-ui-checks-grid fs-1"></i>
                          <span class="d-block"> Images </span>
        </label>
        </div>
          <!-- Post type item -->
        <div class="flex-fill">
        <input type="radio" class="btn-check" name="poll" id="option5">
                        <label class="btn btn-outline-light w-100" for="option5">
        <i class="bi bi-camera-reels fs-1"></i>
                          <span class="d-block"> Video </span>
        </label>
        </div>
          <!-- Post type item -->
        <div class="flex-fill">
        <input type="radio" class="btn-check" name="poll" id="option6">
                        <label class="btn btn-outline-light w-100" for="option6">
        <i class="bi bi-chat-square fs-1"></i>
                          <span class="d-block"> Other </span>
        </label>
        </div>
        <!-- Post type item -->
        </div>
        </div>
        </div>
          <!-- Post type END -->

        <!-- Short description -->
        <div class="col-12">
        <div class="mb-3">
        <label class="form-label">Short description </label>
                    <textarea class="form-control" rows="3" placeholder="Add description"></textarea>
        </div>
        </div>

          <!-- Main toolbar -->
        <div class="col-md-12">
        <!-- Subject -->
        <div class="mb-3">
        <label class="form-label">Post body</label>
                    <!-- Editor toolbar -->
        <div class="bg-light border border-bottom-0 rounded-top py-3" id="quilltoolbar">
        <span class="ql-formats">
        <select class="ql-size"></select>
        </span>
          <span class="ql-formats">
        <button class="ql-bold"></button>
                          <button class="ql-italic"></button>
                          <button class="ql-underline"></button>
                          <button class="ql-strike"></button>
        </span>
          <span class="ql-formats">
        <select class="ql-color"></select>
                          <select class="ql-background"></select>
        </span>
          <span class="ql-formats">
        <button class="ql-code-block"></button>
        </span>
          <span class="ql-formats">
        <button class="ql-list" value="ordered"></button>
                          <button class="ql-list" value="bullet"></button>
                          <button class="ql-indent" value="-1"></button>
                          <button class="ql-indent" value="+1"></button>
        </span>
          <span class="ql-formats">
        <button class="ql-link"></button>
                          <button class="ql-image"></button>
        </span>
          <span class="ql-formats">
        <button class="ql-clean"></button>
        </span>
        </div>
          <!-- Main toolbar -->
        <div class="bg-body border rounded-bottom h-300 overflow-hidden" id="quilleditor">
                      </div>
        </div>
        </div>
          <div class="col-12">
        <div class="mb-3">
                  <!-- Image -->
        <div class="position-relative">
        <h6 class="my-2">Upload post image here, or<a href="#!" class="text-primary"> Browse</a></h6>
                    <label class="w-100" style="cursor:pointer;">
        <span>
        <input class="form-control stretched-link" type="file" name="my-image" id="image" accept="image/gif, image/jpeg, image/png">
        </span>
        </label>
        </div>
          <p class="small mb-0 mt-2"><b>Note:</b> Only JPG, JPEG and PNG. Our suggested dimensions are 600px * 450px. Larger image will be cropped to 4:3 to fit our thumbnails/previews.</p>
                                                                                                                                                                                           </div>
        </div>
          <div class="col-lg-7">
        <!-- Tags -->
        <div class="mb-3">
        <label class="form-label">Tags</label>
                    <textarea class="form-control" rows="1" placeholder="business, sports ..."></textarea>
                    <small>Maximum of 14 keywords. Keywords should all be in lowercase and separated by commas. e.g. javascript, react, marketing.</small>
        </div>
        </div>
          <div class="col-lg-5">
        <!-- Message -->
        <div class="mb-3">
        <label class="form-label">Category</label>
                    <select class="form-select" aria-label="Default select example">
        <option selected>Lifestyle</option>
                                    <option value="1">Technology</option>
                                                                  <option value="2">Travel</option>
                                                                                            <option value="3">Business</option>
                                                                                                                        <option value="4">Sports</option>
                                                                                                                                                  <option value="5">Marketing</option>
        </select>
        </div>
        </div>
          <div class="col-12">
        <div class="form-check mb-3">
        <input class="form-check-input" type="checkbox" value="" id="postCheck">
                    <label class="form-check-label" for="postCheck">
        Make this post featured?
        </label>
        </div>
        </div>
          <!-- Create post button -->
        <div class="col-md-12 text-start">
        <button class="btn btn-primary w-100" type="submit">Create post</button>
        </div>
        </div>
        </form>
        
