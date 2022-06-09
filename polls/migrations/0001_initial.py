# Generated by Django 3.2.12 on 2022-06-09 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import polls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='sign',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(default=polls.models.random_id_field, max_length=12, primary_key=True, serialize=False, unique=True)),
                ('profilePic', models.ImageField(default=polls.models.random_profile, upload_to='profilePic/')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='other', max_length=25)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gmail', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('iscreator', models.BooleanField(default=False)),
                ('signup_referral_by', models.IntegerField(default=0)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('interest', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('item_key1', 'item_key1'), ('item_key2', 'item_key2'), ('item_key3', 'item_key3'), ('item_key4', 'item_key4'), ('item_key5', 'item_key5')], max_length=59, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', polls.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Addresources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcesid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('timeline', models.CharField(max_length=20, verbose_name='hr:min:se')),
                ('resourcesfile', models.FileField(blank=True, null=True, upload_to='resources/')),
            ],
        ),
        migrations.CreateModel(
            name='connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connectid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('connect', models.ImageField(null=True, upload_to='post/', verbose_name='connect')),
                ('title', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=100)),
                ('published_on', models.CharField(choices=[('public', 'public'), ('private', 'private'), ('unlist', 'unlist')], default='public', max_length=100)),
                ('likes', models.ManyToManyField(blank=True, related_name='connect_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gmail', models.EmailField(max_length=254)),
                ('auth_token', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('file', models.FileField(upload_to=polls.models.get_upload_to)),
                ('description', models.TextField(blank=True, null=True)),
                ('customthumbnail', models.ImageField(blank=True, null=True, upload_to=polls.models.get_upload_to, verbose_name='customthumbnail')),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
                ('skills', models.CharField(blank=True, max_length=500, null=True)),
                ('compress', models.BooleanField(default=False)),
                ('targetaudience', models.CharField(choices=[('not-for-kids', 'not-for-kids'), ('kids', 'kids')], default='not-for-kids', max_length=100)),
                ('agerestriction', models.CharField(choices=[('no-restrict', 'no-restrict'), ('restrict', 'restrict')], default='no-restrict', max_length=100)),
                ('isCommentsOn', models.BooleanField(default=True)),
                ('isLikeCountOn', models.BooleanField(default=True)),
                ('isAudioCommentOn', models.BooleanField(default=True)),
                ('publish', models.CharField(choices=[('public', 'public'), ('private', 'private'), ('unlist', 'unlist')], default='public', max_length=100)),
                ('published_on', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('Latest', 'Latest'), ('Old', 'Old'), ('unlist', 'unlist')], default='Latest', max_length=33)),
                ('ready_to_publish', models.BooleanField(default=False)),
                ('publish_time', models.CharField(blank=True, max_length=100, null=True)),
                ('likesvideo', models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr1', models.FileField(upload_to='attr1/')),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myid', models.CharField(default=polls.models.random_id_field, max_length=16, unique=True)),
                ('ex', models.FileField(upload_to='mymodel1/')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=30)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='social_handling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('social1', models.URLField(blank=True, null=True)),
                ('social2', models.URLField(blank=True, null=True)),
                ('social3', models.URLField(blank=True, null=True)),
                ('social4', models.URLField(blank=True, null=True)),
                ('social5', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkbaseAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_action', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('visit', models.IntegerField(default=0)),
                ('impressions', models.IntegerField(default=0)),
                ('new_visit', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='workbaseinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wbid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('workbasename', models.CharField(blank=True, max_length=25, null=True)),
                ('workbasechoices', models.CharField(choices=[('show my skills', 'show my skills'), ('Recruit candidate', 'Recruit candidate'), ('Startup(skills+Recruit)', 'Startup(skills+Recruit)')], default='show my skills', max_length=30)),
                ('wbemail', models.EmailField(blank=True, max_length=254, null=True)),
                ('wbdescription', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=50)),
                ('session', models.CharField(max_length=50)),
                ('view', models.PositiveIntegerField(default=0)),
                ('video', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='count', to='polls.detail')),
            ],
        ),
        migrations.CreateModel(
            name='User_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', polls.models.MyPickledObjectField(default=list, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='timelineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=200)),
                ('resourcesid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('resourcesfile', models.FileField(blank=True, null=True, upload_to='resources/')),
                ('connected_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.detail')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='supportTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.PositiveIntegerField()),
                ('minutes', models.PositiveIntegerField()),
                ('seconds', models.PositiveIntegerField()),
                ('resources', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.addresources')),
                ('videorefernce', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.detail')),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wbname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.workbaseinfo')),
            ],
        ),
        migrations.CreateModel(
            name='sharemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('status', models.CharField(choices=[('Invited', 'Invited'), ('Accepted', 'Accepted')], default='Invited', max_length=10)),
                ('clicked', models.BooleanField(default=False)),
                ('Accountsigned', models.BooleanField(default=False)),
                ('CreatorAccount', models.BooleanField(default=False)),
                ('videoupload', models.BooleanField(default=False)),
                ('recommended_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='recommended_by')),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('description', models.CharField(max_length=50000)),
                ('email_id', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=50)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='report4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('report_descript', models.CharField(max_length=100)),
                ('choice', models.CharField(choices=[('sexual content', 'sexual content'), ('violent or repulsive content', 'violent or repulsive content'), ('hateful or abusive content', 'hateful or abusive content'), ('harresment or bullyingcontent', 'harresment or bullyingcontent,'), ('hamrful or dangers act', 'hamrful or dangers act'), ('promotes terrorism', 'promotes terrorism,'), ('spam or misleading', 'spam or misleading'), ('infringes my rights', 'infringes my rights')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('report_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.detail')),
                ('report_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.connect')),
                ('report_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('reply_text', models.CharField(default=' ', max_length=2000)),
                ('for_reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='for_reply_1', to=settings.AUTH_USER_MODEL)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_name_1', to=settings.AUTH_USER_MODEL)),
                ('reply_of_reply', models.ManyToManyField(blank=True, related_name='_polls_reply_reply_of_reply_+', to='polls.Reply')),
                ('reply_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.detail')),
            ],
        ),
        migrations.CreateModel(
            name='RefferalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refferal_code', models.CharField(blank=True, default='', max_length=12, unique=True)),
                ('email', models.EmailField(blank=True, max_length=122, null=True)),
                ('refferal_for', models.CharField(blank=True, default='', max_length=34)),
                ('refferal_plateform', models.CharField(blank=True, max_length=100)),
                ('is_clicked', models.BooleanField(default=False)),
                ('is_signup', models.BooleanField(default=False)),
                ('is_creator', models.BooleanField(default=False)),
                ('is_uploaded', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('refferal_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refferal_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='questionnaires',
            fields=[
                ('ques_id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('questionnaireid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('description', models.TextField(default='')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('videoid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.detail')),
            ],
        ),
        migrations.CreateModel(
            name='question3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcqid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('question', models.TextField(default='')),
                ('imgfile', models.FileField(blank=True, null=True, upload_to='question3/')),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
                ('img1_option', models.FileField(blank=True, null=True, upload_to='question_mcq/img1_option')),
                ('img2_option', models.FileField(blank=True, null=True, upload_to='question_mcq/img2_option')),
                ('img3_option', models.FileField(blank=True, null=True, upload_to='question_mcq/img3_option')),
                ('img4_option', models.FileField(blank=True, null=True, upload_to='question_mcq/img4_option')),
                ('answer', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('isrequired', models.BooleanField(default=False)),
                ('questionnaire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.questionnaires')),
            ],
        ),
        migrations.CreateModel(
            name='question2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnaid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('question', models.TextField(default='')),
                ('imgfile', models.FileField(blank=True, null=True, upload_to='question2/')),
                ('answer', models.TextField(default='')),
                ('isrequired', models.BooleanField(default=True)),
                ('questionnaire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.questionnaires')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('question', models.TextField(default='')),
                ('imgfile', models.FileField(blank=True, null=True, upload_to='question/')),
                ('answer', models.TextField(default='')),
                ('isrequired', models.BooleanField(default=True)),
                ('ques', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.questionnaires')),
            ],
        ),
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grouplistid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('group_list_image', models.ImageField(blank=True, null=True, upload_to='grouplist/', verbose_name='group_list_image')),
                ('name', models.CharField(max_length=20)),
                ('files', models.ManyToManyField(to='polls.detail')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mycourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mycourse_title', models.CharField(max_length=50)),
                ('mycourse_choice', models.CharField(choices=[('public', 'public'), ('private', 'private')], default='private', max_length=40)),
                ('course_file', models.ManyToManyField(blank=True, to='polls.detail')),
                ('course_playlist', models.ManyToManyField(blank=True, to='polls.playlist')),
            ],
        ),
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('videos', models.ManyToManyField(to='polls.detail')),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupskillid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('title', models.CharField(max_length=30)),
                ('lists', models.ManyToManyField(to='polls.playlist')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='doc_verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('qualification', models.CharField(default='', max_length=10)),
                ('specialized', models.CharField(default='', max_length=15)),
                ('skill_tags', models.CharField(max_length=500)),
                ('year_of_experience', models.PositiveIntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='connect_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('post_comment', models.TextField()),
                ('post_created_on', models.DateTimeField(auto_now=True)),
                ('like_active', models.CharField(blank=True, max_length=12, null=True)),
                ('dislike_active', models.CharField(blank=True, max_length=12, null=True)),
                ('comment_dislikes', models.ManyToManyField(blank=True, related_name='Post_comment_dislkikes', to=settings.AUTH_USER_MODEL)),
                ('likes_comment', models.ManyToManyField(blank=True, related_name='Post_comment_likes', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='polls.connect_comment')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='polls.connect')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-post_created_on'],
            },
        ),
        migrations.CreateModel(
            name='Commentss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(default=' ', max_length=2000)),
                ('like_active', models.CharField(blank=True, default='null', max_length=2000)),
                ('dislike_active', models.CharField(blank=True, default='null', max_length=2000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('dis_likes_on_comment', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('likes_on_comment', models.ManyToManyField(blank=True, related_name='likes_on_comment', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='polls.commentss')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.detail')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='basic_display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlightid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('highlight1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highlight1', to='polls.detail')),
                ('highlight2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highlight2', to='polls.detail')),
                ('highlight3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highlight3', to='polls.detail')),
                ('highlight4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highlight4', to='polls.detail')),
                ('highlight5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highlight5', to='polls.detail')),
            ],
        ),
        migrations.CreateModel(
            name='basic_branding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandingid', models.CharField(default=polls.models.random_id_field, max_length=12, unique=True)),
                ('wblogo', models.FileField(blank=True, null=True, upload_to='wblogo/')),
                ('banner', models.FileField(blank=True, null=True, upload_to='banner/')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='addresources',
            name='questionnaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire', to='polls.questionnaires'),
        ),
        migrations.AddField(
            model_name='addresources',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addresources',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.detail'),
        ),
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('skills', models.CharField(max_length=100)),
                ('contact_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_id', to='polls.contact')),
            ],
        ),
        migrations.AddConstraint(
            model_name='report4',
            constraint=models.UniqueConstraint(fields=('report_file', 'report_user'), name='report_user_file'),
        ),
        migrations.AddConstraint(
            model_name='report4',
            constraint=models.UniqueConstraint(fields=('report_post', 'report_user'), name='report_user_post'),
        ),
    ]