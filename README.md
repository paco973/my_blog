# my_blog



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/lawa_zone/my_blog.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/lawa_zone/my_blog/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.


Écrit moi ce formulaire en django modelform en gardant tous les attributs et les veules par défaut le champ elle-même :
<div class="card border mb-4">
          <div class="card-header border-bottom p-3">
            <h5 class="card-header-title mb-0">Profile</h5>
          </div>
          <div class="card-body">
            <!-- Full name -->
            <div class="mb-3">
              <label class="form-label">Full name</label>
              <div class="input-group">
                <input type="text" class="form-control" value="Louis" placeholder="First name">
                <input type="text" class="form-control" value="Ferguson" placeholder="Last name">
              </div>
            </div>
            <!-- Username -->
            <div class="mb-3">
              <label class="form-label">Username</label>
              <div class="input-group">
                <span class="input-group-text">webestica.com</span>
                <input type="text" class="form-control" value="louisferguson">
              </div>
            </div>
            <!-- Profile picture -->
            <div class="mb-3">
              <label class="form-label">Profile picture</label>
              <!-- Avatar upload START -->
              <div class="d-flex align-items-center">
                <div class="position-relative me-3">
                  <!-- Avatar edit -->
                  <div class="position-absolute top-0 end-0  z-index-9">
                    <a class="btn btn-sm btn-light btn-round mb-0 mt-n1 me-n1" href="#"> <i class="bi bi-pencil"></i> </a>
                  </div>
                  <!-- Avatar preview -->
                  <div class="avatar avatar-xl">
                    <img class="avatar-img rounded-circle border border-white border-3 shadow" src="{{request.user.photo.url}}" alt="">
                  </div>
                </div>
                <!-- Avatar remove button -->
                <div class="avatar-remove">
                  <button type="button" class="btn btn-light">Delete</button>
                </div>
              </div>
              <!-- Avatar upload END -->
            </div>
            <!-- Job title -->
            <div class="mb-3">
              <label class="form-label">Job title</label>
              <input class="form-control" type="text" value="An editor at Blogzine">
            </div>
            <!-- Location -->
            <div class="mb-3">
              <label class="form-label">Location</label>
              <input class="form-control" type="text" value="New Hampshire">
            </div>
            <!-- Bio -->
            <div class="mb-3">
              <label class="form-label">Bio</label>
              <textarea class="form-control" rows="3">I’ve found a way to get paid for my favorite hobby, and do so while following my dream of traveling the world.</textarea>
              <div class="form-text">Brief description for your profile.</div>
            </div>
            <!-- Birthday -->
            <div>
              <label class="form-label">Birthday</label>
              <input type="text" class="form-control flatpickr-input" placeholder="DD/MM/YYYY" value="12/10/1990">
            </div>
            <!-- Save button -->
            <div class="d-flex justify-content-end mt-4">
              <a href="#" class="btn text-secondary border-0 me-2">Discard</a>
              <a href="#" class="btn btn-primary">Save changes</a>
            </div>
          </div>
        </div>

avec pour modele :

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    subscribe = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    def fullname(self):
        return f'{self.fullname} {self.last_name}'.title()
