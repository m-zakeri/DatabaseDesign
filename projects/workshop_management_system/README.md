# Workshop Management System

An educational platform offering a diverse range of online and offline courses for sale, covering various fields of
knowledge.

## Objectives

- Creating a space to sell and introduce training courses by professors and different specialties .

- Improving the level of knowledge and skills of people in many fields and at any level of experience .

- Creating opportunities for direct communication between professors and students .

- Support for offline training courses held in different places .

## Advantages

- Access to a diverse range of educational courses in various fields.
- Expert instructors and experienced guides in the teaching domain.
- Opportunity to participate in offline courses at different city locations.

## Diagram/Schemas

[Google Drive](https://drive.google.com/drive/folders/1UhIXpGBSXpGy2EnQZ9C6Djh_cCtaMAIa?usp=sharing)


## Models

###### User:

- **username**: CharField for the username with a maximum length of 50 characters (unique).
- **first_name**: CharField for the first name with a maximum length of 50 characters (nullable and blank).
- **last_name**: CharField for the last name with a maximum length of 50 characters (nullable and blank).
- **date_of_birth**: DateField for the date of birth (nullable and blank).
- **image**: ImageField for the user's profile image, default image set, uploads to 'image/user' directory.
- **email**: EmailField for the user's email address (unique).
- **phone_number**: CharField for the phone number with a maximum length of 11 characters, including a custom
  validator (nullable and blank).
- **caption**: CharField for a user caption with a maximum length of 300 characters (nullable and blank).
- **is_active**: BooleanField indicating if the user account is active, default is True.
- **is_admin**: BooleanField indicating if the user has admin privileges, default is False.
- **is_teacher**: BooleanField indicating if the user is a teacher, default is False.
- **created_at**: DateTimeField capturing the creation timestamp.
- **updated_at**: DateTimeField capturing the last update timestamp.

###### Country:

- `name`: A character field with a maximum length of 50 characters, representing the name of the country.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### City:

- `name`: A character field with a maximum length of 50 characters, representing the name of the city.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Address:

- `user`: A ForeignKey field linking the address to a user. If the associated user is deleted, the address records will
  also be deleted.
- `country`: A ForeignKey field linking the address to a country using the `Country` model. The default country is set
  to 'Iran'. If the associated country is deleted, the address records will also be deleted.
- `city`: A ForeignKey field linking the address to a city using the `City` model. The default city is set to 'Tehran'.
  If the associated city is deleted, the address records will also be deleted.
- `state`: A CharField with a maximum length of 50 characters, representing the state of the address.
- `postal_code`: A CharField with a maximum length of 10 characters, representing the postal code of the address.
- `full_address`: A TextField representing the full address. Each address should have a unique full address.
- `is_active`: A BooleanField with a default value of `False`, representing whether the address is currently active.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the address is
  modified.

###### Social Media:

- `user`: A ForeignKey field linking the social media profile to a user. If the associated user is deleted, the social
  media records will also be deleted.
- `platform`: A CharField with a maximum length of 50 characters, representing the social media platform name.
- `profile_link`: A URLField with a maximum length of 200 characters, representing the link to the user's profile on the
  social media platform.
- `is_active`: A BooleanField with a default value of `False`, representing whether the social media profile is
  currently active.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the social media
  profile is modified.

###### Card:

- `user`: A ForeignKey field linking the card to a user. If the associated user is deleted, the card records will also
  be deleted.
- `card_number`: A CharField with a maximum length of 16 characters, representing the card number. It is unique and
  validated using a custom validator (`validate_credit_card_number`).
- `cv2`: A CharField with a maximum length of 4 characters, representing the Card Security Code (CV2). It is validated
  using a custom validator (`validate_credit_cv2`).
- `date_month`: A CharField with a maximum length of 2 characters, representing the card expiration month.
- `date_year`: A CharField with a maximum length of 2 characters, representing the card expiration year.
- `recipient_name`: A CharField with a maximum length of 50 characters, representing the name of the cardholder.
- `is_active`: A BooleanField with a default value of `False`, representing whether the card is currently active.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the card is modified.

###### New User

- `token`: A CharField with a maximum length of 300 characters, representing a unique token associated with the user
  registration.
- `randcode`: A CharField with a maximum length of 5 characters, representing a random code associated with the user
  registration.
- `username`: A CharField with a maximum length of 50 characters, representing the username chosen by the user during
  registration.
- `email`: An EmailField representing the email address provided by the user during registration.
- `password`: A CharField with a maximum length of 20 characters, representing the user's chosen password.
- `confirm_password`: A CharField with a maximum length of 20 characters, representing the confirmation of the user's
  chosen password.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Email Change Password:

- `email`: An EmailField representing the email address for which the password change is requested.
- `token`: A CharField with a maximum length of 300 characters, representing a unique token associated with the password
  change request.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Blog Category:

- `name`: A CharField with a maximum length of 100 characters, representing the name of the blog category.
- `slug`: A SlugField representing the URL-friendly version of the category name.
- `description`: A TextField that allows for storing additional information or descriptions about the blog category. It
  can be null and blank.
- `image`: An ImageField for uploading and storing an image associated with the blog category. The images are stored in
  the 'img/category/blog' directory.
- `is_publish`: A BooleanField with a default value of `False`, representing whether the blog category is set to be
  published.
- `parent`: A ForeignKey field linking the category to its parent category (if any). If the parent category is deleted,
  the subcategories (related by `related_name='subs'`) will also be deleted.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the blog category is
  modified.

###### Blog Label:

- `name`: A CharField with a maximum length of 100 characters, representing the name of the blog label.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Blog:

- `author`: A ManyToManyField linking the blog post to one or more authors (User model) using the `related_name='blog'`
  attribute.
- `subject`: A CharField with a maximum length of 100 characters, representing the subject or title of the blog post.
- `caption`: A TextField that allows for storing additional information or captions for the blog post. It can be null
  and blank.
- `slug`: A SlugField representing the URL-friendly version of the blog post title.
- `image`: An ImageField for uploading and storing an image associated with the blog post. The images are stored in
  the 'image/blog' directory.
- `category`: A ManyToManyField linking the blog post to one or more categories (BlogCategory model) using
  the `related_name='blog'` attribute.
- `label`: A ManyToManyField linking the blog post to one or more labels (BlogLabel model) using
  the `related_name='blog'` attribute.
- `is_publish`: A BooleanField with a default value of `False`, representing whether the blog post is set to be
  published.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the blog post is
  modified.

###### Blog Description:

- `blog`: A ForeignKey field linking the blog description to a specific blog post (Blog model) using
  the `related_name='description'` attribute.
- `subject`: A CharField with a maximum length of 100 characters, representing the subject or title of the blog
  description.
- `content`: A TextField representing the detailed content of the blog description.
- `parent`: A ForeignKey field linking the blog description to its parent description (if any) using
  the `related_name='subs'` attribute. If the parent description is deleted, the sub-descriptions will also be deleted.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the blog description
  is modified.

###### Blog Comment:

- `blog`: A ForeignKey field linking the blog comment to a specific blog post (Blog model) using
  the `related_name='comment'` attribute.
- `user`: A ForeignKey field linking the blog comment to the user who posted the comment using
  the `related_name='blog_comment'` attribute.
- `message`: A CharField with a maximum length of 300 characters, representing the comment message.
- `is_publish`: A BooleanField with a default value of `False`, representing whether the comment is set to be published.
- `parent`: A ForeignKey field linking the blog comment to its parent comment (if any) using the `related_name='subs'`
  attribute. If the parent comment is deleted, the sub-comments will also be deleted.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Like Blog Comment:

- `user`: A ForeignKey field linking the comment like to a specific user (User model) using
  the `related_name='like_blog_comment'` attribute.
- `comment`: A ForeignKey field linking the comment like to the comment that was liked (BlogComment model) using
  the `related_name='like'` attribute.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Order:

- `customer`: A ForeignKey field linking the order to a specific customer (Customer model) using
  the `related_name='order'` attribute.
- `total_price`: A CharField with a maximum length of 50 characters, representing the total price of the order.
- `is_paid`: A BooleanField with a default value of `False`, representing whether the order has been paid.
- `is_discount`: A BooleanField with a default value of `False`, representing whether the order includes a discount.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the order is
  modified.

###### Order Item

- `order`: A ForeignKey field linking the order item to a specific order (Order model) using the `related_name='items'`
  attribute.
- `course`: A ForeignKey field linking the order item to a specific course (Course model) using
  the `related_name='order_item'` attribute.
- `final_price`: A PositiveIntegerField representing the final price of the course within the order item.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the order item is
  modified.

###### Language:

- `name`: A CharField with a maximum length of 50 characters, representing the name of the language.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Course Label:

- `name`: A CharField with a maximum length of 50 characters, representing the name of the course label.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Course Category:

- `name`: A CharField with a maximum length of 50 characters, representing the name of the course category.
- `slug`: A SlugField representing the URL-friendly version of the category name.
- `description`: A TextField that allows for storing additional information or descriptions about the course category.
  It can be null and blank.
- `image`: An ImageField for uploading and storing an image associated with the course category. The images are stored
  in the 'image/category/course' directory.
- `parent`: A ForeignKey field linking the category to its parent category (if any) using the `related_name='subs'`
  attribute. If the parent category is deleted, the subcategories will also be deleted.
- `is_publish`: A BooleanField with a default value of `False`, representing whether the course category is set to be
  published.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the course category
  is modified.

###### Course:

- `name`: A CharField with a maximum length of 50 characters, representing the name of the course.
- `caption`: A CharField with a maximum length of 150 characters, providing a brief caption for the course.
- `image`: An ImageField for uploading and storing an image associated with the course. The images are stored in the '
  image/course' directory.
- `introduction_video`: A FileField for uploading an introduction video for the course. The videos are stored in the '
  video/course' directory.
- `level`: A CharField with choices for the course level.
- `state`: A CharField with choices representing the state of the course.
- `slug`: A SlugField representing the URL-friendly version of the course name.
- `language`: A ManyToManyField linking the course to one or more languages (Language model) using
  the `related_name='course'` attribute.
- `label`: A ManyToManyField linking the course to one or more labels (CourseLabel model) using
  the `related_name='course'` attribute.
- `category`: A ManyToManyField linking the course to one or more categories (CourseCategory model) using
  the `related_name='course'` attribute.
- `teacher`: A ManyToManyField linking the course to one or more teachers (Teacher model) using
  the `related_name='course'` attribute.
- `customer`: A ManyToManyField linking the course to one or more customers (Customer model) using
  the `related_name='course'` attribute.
- `number_customer`: A PositiveIntegerField representing the number of customers enrolled in the course.
- `number_video`: A PositiveIntegerField representing the number of videos in the course.
- `video_time`: A DurationField representing the total duration of the course videos.
- `course_start_date`: A DateField representing the start date of the course.
- `is_exam`: A BooleanField indicating whether the course includes exams.
- `is_graduation`: A BooleanField indicating whether the course includes a graduation.
- `registering_open`: A BooleanField indicating whether course registration is open.
- `is_publish`: A BooleanField indicating whether the course is set to be published.
- `price`: A FloatField representing the price of the course.
- `discount`: A FloatField representing the discount applied to the course.
- `start_discount`: A DateTimeField representing the start date of the discount.
- `end_discount`: A DateTimeField representing the end date of the discount.
- `total_points`: A FloatField representing the total points associated with the course.
- `type`: A CharField with choices representing the type of course.

###### Course Description:

- `course`: A ForeignKey field linking the course description to a specific course (Course model) using
  the `related_name='descriptions'` attribute.
- `subject`: A CharField with a maximum length of 100 characters, representing the subject or title of the course
  description.
- `content`: A TextField representing the detailed content of the course description. It can be null and blank.
- `parent`: A ForeignKey field linking the course description to its parent description (if any) using
  the `related_name='subs'` attribute. If the parent description is deleted, the sub-descriptions will also be deleted.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the course
  description is modified.

###### Course Like:

- `user`: A ForeignKey field linking the course like to a specific user (User model) using
  the `related_name='like_course'` attribute.
- `course`: A ForeignKey field linking the course like to the course that was liked (Course model) using
  the `related_name='like'` attribute.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Course Certificate:

- `course`: A ForeignKey field linking the certificate to a specific course (Course model) using
  the `related_name='certificate'` attribute.
- `name`: A CharField with a maximum length of 50 characters, representing the name of the certificate.
- `certificate_image`: A FileField for uploading and storing the certificate image. The documents are stored in the '
  document/certificate/course' directory.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Coupon Code:

- `user_costumer`: A ManyToManyField linking the coupon code to one or more users (Customer model) using
  the `related_name='coupon_code'` attribute. It is blank to allow coupons not tied to specific users.
- `course`: A ManyToManyField linking the coupon code to one or more courses (Course model) using
  the `related_name='coupon_code'` attribute.
- `name`: A CharField with a maximum length of 50 characters, representing the name or code of the coupon. It is set to
  be unique.
- `discount`: A FloatField representing the discount value associated with the coupon.
- `number_discount`: A PositiveIntegerField representing the number of available discounts for the coupon.
- `is_active`: A BooleanField indicating whether the coupon is currently active.
- `valid_from`: A DateTimeField representing the start date and time when the coupon becomes valid.
- `valid_to`: A DateTimeField representing the end date and time until the coupon is valid.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the coupon is
  modified.

###### Course Comment:

- `user`: A ForeignKey field linking the course comment to a specific user (User model) using
  the `related_name='course_comment'` attribute.
- `course`: A ForeignKey field linking the course comment to the course that was commented on (Course model) using
  the `related_name='comment'` attribute.
- `message`: A CharField with a maximum length of 300 characters, representing the message or content of the comment.
- `score`: A FloatField representing the score or rating given to the course in the comment. It has a default value of
    0.
- `parent`: A ForeignKey field linking the course comment to its parent comment (if any) using the `related_name='subs'`
  attribute. If the parent comment is deleted, the sub-comments will also be deleted.
- `is_publish`: A BooleanField indicating whether the comment is set to be published.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the comment is
  modified.

###### Like Course Comment:

- `user`: A ForeignKey field linking the like on a course comment to a specific user (User model) using
  the `related_name='like_course_comment'` attribute.
- `comment`: A ForeignKey field linking the like on a course comment to the comment that was liked (CourseComment model)
  using the `related_name='like'` attribute.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Frequently Asked Questions:

- `course`: A ForeignKey field linking the FAQ to a specific course (Course model) using
  the `related_name='faq_frequently'` attribute.
- `question`: A CharField with a maximum length of 100 characters, representing the frequently asked question.
- `answer`: A TextField representing the detailed answer to the frequently asked question.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Asked Question:

- `course`: A ForeignKey field linking the asked question to a specific course (Course model) using
  the `related_name='ask_question'` attribute.
- `user`: A ForeignKey field linking the asked question to the user who asked it (User model) using
  the `related_name='ask_question_course'` attribute.
- `question`: A CharField with a maximum length of 300 characters, representing the asked question.
- `parent`: A ForeignKey field linking the asked question to its parent question (if any) using
  the `related_name='subs'` attribute. If the parent question is deleted, the sub-questions will also be deleted.
- `is_publish`: A BooleanField indicating whether the question is set to be published.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.

###### Season:

- `course`: A ForeignKey field linking the season to a specific course (Course model) using the `related_name='season'`
  attribute.
- `name`: A CharField with a maximum length of 100 characters, representing the name of the season.
- `description`: A TextField representing the description of the season. It can be null and blank.
- `is_publish`: A BooleanField indicating whether the season is set to be published.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the season is
  modified.

###### Meeting:

- `season`: A ForeignKey field linking the meeting to a specific season (Season model) using
  the `related_name='meetings'` attribute.
- `name`: A CharField with a maximum length of 100 characters, representing the name of the meeting.
- `description`: A TextField representing the description of the meeting. It can be null and blank.
- `location_and_time`: A TextField representing the location and time information for the meeting. It can be null and
  blank.
- `link`: A URLField with a maximum length of 200 characters, representing the link to the meeting (if any). It can be
  null and blank.
- `video`: A FileField for uploading and storing the meeting video. The videos are stored in the 'video/meeting'
  directory. It can be null and blank.
- `video_time`: A DurationField representing the duration of the meeting video. It has a default value of 0.
- `file`: A FileField for uploading and storing additional documents/files related to the meeting. The files are stored
  in the 'file/document' directory. It can be null and blank.
- `free`: A BooleanField indicating whether the meeting is free.
- `is_publish`: A BooleanField indicating whether the meeting is set to be published.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the meeting is
  modified.

###### Exam:

- `course`: A ForeignKey field linking the exam to a specific course (Course model) using the `related_name='exam'`
  attribute.
- `name`: A CharField with a maximum length of 100 characters, representing the name of the exam.
- `description`: A TextField representing the description of the exam. It can be null and blank.
- `start_exam`: A DateTimeField representing the start date and time of the exam.
- `link`: A URLField representing the link to the exam.
- `is_publish`: A BooleanField indicating whether the exam is set to be published.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the exam is modified.

###### Exam Score:

- `exam`: A ForeignKey field linking the exam score to a specific exam (Exam model) using the `related_name='Score'`
  attribute.
- `costumer`: A ForeignKey field linking the exam score to a specific customer (Customer model) using
  the `related_name='exam'` attribute.
- `score`: A FloatField representing the score achieved by the customer in the exam.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the exam score is
  modified.

###### Festival:

- `course`: A ManyToManyField linking the festival to one or more courses (Course model) using
  the `related_name='festival'` attribute.
- `name`: A CharField with a maximum length of 100 characters, representing the name of the festival.
- `description`: A TextField representing the description of the festival. It can be null and blank.
- `image`: An ImageField for uploading and storing the image associated with the festival. The images are stored in
  the 'image/festival' directory.
- `start_time`: A DateTimeField representing the start time of the festival.
- `end_time`: A DateTimeField representing the end time of the festival.
- `is_publish`: A BooleanField indicating whether the festival is set to be published.
- `registering_open`: A BooleanField indicating whether the registering for the festival is open.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the festival is
  modified.

###### Customer:

- `user`: A OneToOneField linking the customer to a specific user account (User model) using
  the `related_name='customer'` attribute.
- `is_valid`: A BooleanField indicating whether the customer is considered valid. Default is set to `True`.

###### Customer Certificate:

- `customer`: A ForeignKey field linking the certificate to a specific customer (Customer model) using
  the `related_name='customer_certificate'` attribute.
- `name`: A CharField with a maximum length of 50 characters, representing the name of the certificate.
- `description`: A TextField representing the description of the certificate. It can be null and blank.
- `type`: A CharField with a maximum length of 50 characters, representing the type or category of the certificate.
- `certificate_image`: A FileField for uploading and storing the image of the certificate. The images are stored in
  the 'documents/certificate/customer' directory.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the certificate is
  modified.

###### Teacher Income:

- `teacher`: A ForeignKey field linking the income to a specific teacher (Teacher model) using
  the `related_name='income'` attribute.
- `course`: A ManyToManyField linking the income to one or more courses (Course model) using
  the `related_name='teacher_income'` attribute.
- `amount`: A PositiveIntegerField representing the income amount.
- `status`: A CharField with a maximum length of 50 characters, representing the status of the income. Choices include '
  Paid', 'Awaiting Payment', and 'Unpaid'.
- `method`: A CharField with a maximum length of 50 characters, representing the payment method. Choices include '
  Online' and 'Card by card'.
- `payment_date`: A DateTimeField representing the date and time of the payment.
- `tax_amount`: A PositiveIntegerField representing the tax amount. Default is set to 0.
- `transaction_image`: A FileField for uploading and storing the image of the transaction. The images are stored in
  the 'document/transaction/income_teacher' directory.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the income record is
  modified.

###### Notification:

- `user`: A ManyToManyField linking the notification to one or more users (User model) using
  the `related_name='notification'` attribute.
- `subject`: A CharField with a maximum length of 100 characters, representing the subject of the notification.
- `message`: A TextField representing the message content of the notification.
- `status`: A CharField with a maximum length of 50 characters, representing the status of the notification. Choices
  include 'READ' and 'UNREAD'.
- `display`: A BooleanField indicating whether the notification is set to be displayed. Default is set to `False`.
- `type`: A CharField with a maximum length of 50 characters, representing the type or category of the notification.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the notification is
  modified.

###### Teacher:

- `user`: A OneToOneField linking the teacher to a specific user account (User model) using the `related_name='teacher'`
  attribute.
- `description`: A TextField representing the description of the teacher.
- `score`: A FloatField representing the score or rating of the teacher. Default is set to 0.
- `gender`: A CharField with a maximum length of 50 characters, representing the gender of the teacher. Choices
  include 'man' and 'woman'.
- `teaching_experience`: An IntegerField representing the number of years of teaching experience. Default is set to 0.
- `is_valid`: A BooleanField indicating whether the teacher is considered valid. Default is set to `False`.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the teacher
  information is modified.

###### Work:

- `teacher`: A ForeignKey field linking the work to a specific teacher (Teacher model) using the `related_name='work'`
  attribute.
- `name`: A CharField with a maximum length of 50 characters, representing the name of the work.
- `work_phone`: A CharField with a maximum length of 11 characters, representing the work phone number. It includes a
  custom validator (`validate_credit_work_phone`) to ensure the phone number's validity.
- `employment_file`: A FileField for uploading and storing the employment photo. The files are stored in the '
  document/certificate/work' directory.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the work information
  is modified.

###### Skill:

- `teacher`: A ForeignKey field linking the skill to a specific teacher (Teacher model) using the `related_name='skill'`
  attribute.
- `name`: A CharField with a maximum length of 50 characters, representing the name of the skill.
- `description`: A TextField representing the description of the skill.
- `certificate_photo`: A FileField for uploading and storing the certificate photo. The files are stored in the '
  document/certificate/skill' directory.
- `learning_percentage`: A FloatField representing the learning percentage or proficiency level in the skill. Default is
  set to 0.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the skill information
  is modified.

###### Level Education:

- `teacher`: A ForeignKey field linking the educational level to a specific teacher (Teacher model) using
  the `related_name='level_education'` attribute.
- `name_university`: A CharField with a maximum length of 50 characters, representing the name of the university.
- `date_of_graduation`: A DateField representing the date of graduation.
- `graduation`: A CharField with choices representing the level of graduation. Choices include 'diploma', "Bachelor's
  degree", "Master's degree", and "doctorate degree".
- `Academic_discipline`: A CharField with a maximum length of 50 characters, representing the academic discipline.
- `graduation_image`: A FileField for uploading and storing the graduation image. The files are stored in the '
  file/certificate/graduation_teacher' directory.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the educational level
  information is modified.

###### Ticket:

- `user`: A ForeignKey field linking the ticket to a specific user (User model) using the `related_name='ticket'`
  attribute.
- `course`: A ForeignKey field linking the ticket to a specific course (Course model) using the `related_name='ticket'`
  attribute. This field is optional and can be null or blank.
- `subject`: A CharField with a maximum length of 100 characters, representing the subject of the ticket.
- `message`: A TextField representing the detailed message or request of the ticket.
- `status`: A CharField with choices representing the status of the ticket. Choices include 'Read' and 'Unread'.
- `priority`: A CharField with choices representing the priority of the ticket. Choices include 'Many', 'Very Many', '
  Low', and 'Very Low'.
- `parent`: A ForeignKey field linking the ticket to a parent ticket (self-referential) using the `related_name='subs'`
  attribute. This field is optional and can be null or blank.
- `is_publish`: A BooleanField representing the publish status of the ticket. Default is set to False.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the ticket
  information is modified.

###### Transaction:

- `user`: A ForeignKey field linking the transaction to a specific user (User model) using
  the `related_name='transaction'` attribute.
- `course`: A ManyToManyField linking the transaction to one or more courses (Course model) using
  the `related_name='transaction'` attribute.
- `teacher`: A ManyToManyField linking the transaction to one or more teachers (Teacher model) using
  the `related_name='transaction'` attribute. This field is optional and can be blank.
- `amount`: A PositiveIntegerField representing the transaction amount.
- `currency`: A CharField with choices representing the currency of the transaction. Choices include 'Rial' and '
  Dollar'.
- `payment_method`: A CharField representing the payment method used for the transaction.
- `status`: A CharField with choices representing the status of the transaction. Choices include 'Paid', 'Unpaid', and '
  Awaiting Payment'.
- `description`: A TextField representing additional information or notes about the transaction. This field is optional
  and can be null or blank.
- `sender_card_number`: A CharField representing the sender's card number, validated using
  the `validate_credit_card_number` validator.
- `recipient_card_number`: A CharField representing the recipient's card number, validated using
  the `validate_credit_card_number` validator.
- `transaction_image`: A FileField storing the transaction image and using the 'document/transaction/user' upload path.
- `created_at`: A DateTimeField set to auto_now_add, automatically capturing the creation date and time.
- `updated_at`: A DateTimeField set to auto_now, automatically updating the date and time whenever the transaction
  information is modified.

## Features
### Api
- API implementation for all models.
- Add authentication for create, update and delete accesses.
- Providing a beautiful view for the api

### Course Interactions

#### Likes

- **Like Courses:**
    - Users can like (or favorite) courses to bookmark them or show interest.

#### Comments

- **Comment on Courses:**
    - Users can leave comments on each course to share their thoughts or ask questions.

#### Ratings

- **Rate Courses:**
    - Users can give ratings to courses to provide feedback on their experience.

### Q&A Section

- **Ask Questions:**
    - Users can ask questions related to each course.

- **Answer Questions:**
    - Users can answer questions asked by other users.

### User Engagement

#### User Profiles

- **View Liked Courses:**
    - Users can view a list of courses they have liked.

- **View Comments:**
    - Users can see comments they have made on courses.

- **View Ratings:**
    - Users can see the ratings they have given to courses.

## Getting Started

1. **Visit the website:**
    - To explore courses and tutorials, visit [Eduport](https://www.Eduport.com).


2. **Sign Up and Log In:**
    - To access full features, sign up or log in to your user account.


3. **Search and Filter:**
    - Use the site's search and filter features to find courses that match your preferences.


4. **Purchase and Join Courses:**
    - With a single click, easily participate in your preferred courses and benefit from educational resources.

## Authentication

The system supports multiple authentication methods for both login and registration.
The system provides a password reset functionality that requires users to enter their email address to initiate the
process.

### Login

1. **Email and Password:**
    - Users can log in using their email and password.


2. **Username and Password:**
    - Users can log in using their username and password.


3. **Google Sign-In:**
    - Users can log in using their Google accounts.

### Registration

1. **Email Verification:**
    - After registration, a five-digit verification code is sent to the user's email.
    - Users must enter the code to complete the email verification process.


2. **Google Sign-Up:**
    - Users can register by signing up with their Google accounts.
    - Click on the "Sign Up with Google" button and follow the prompts to complete the registration process.

### Password Reset

1. **Forgot Password:**
    - Users who forget their passwords can click on the "Forgot Password" link on the login page.


2. **Enter Email:**
    - Users need to enter their email address associated with their account.


3. **Email Verification:**
    - A link for resetting the password is sent to the user's email.


4. **Reset Password:**
    - Users click on the link and are directed to a page where they can enter a new password.

## Installation and Setup

### 1. Install Python and Virtual Environment

Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/). After
that, follow these steps:

```bash
# Install virtualenv
pip install virtualenv

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (Unix or MacOS)
source venv/bin/activate 
```

### 2. Clone the Project

```bash
# Clone the project from the repository
git clone https://github.com/rezasharafdini/DatabaseDesign.git
cd DatabaseDesign/project/workshop_management_system
```

### 3. Install Dependencies

```bash
# Install the project dependencies
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
# Apply migrations to set up the database
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server

```bash
# Run the development server
python manage.py runserver
```

