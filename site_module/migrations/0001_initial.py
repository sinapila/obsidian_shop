# Generated by Django 4.0.6 on 2022-07-15 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=202, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': ' دسته بندی لینک های فوتر',
                'verbose_name_plural': ' دسته بندی های لینک های فوتر',
            },
        ),
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(blank=True, null=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='images/banner', verbose_name='تصویر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('position', models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزییات محصولات'), ('article_page', 'صفحه لیست مقالات'), ('article_detail_page', 'صفحه مقاله'), ('about_us', 'صفحه درباره ما')], max_length=200, verbose_name='محل قرار گیری')),
            ],
            options={
                'verbose_name': 'بنر تبلیاتی',
                'verbose_name_plural': 'بنر هی تبلیغاتی',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200, verbose_name='نام سایت')),
                ('site_url', models.CharField(max_length=200, verbose_name='دامنه سایت')),
                ('address', models.CharField(max_length=200, verbose_name=' آدرس')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن')),
                ('fax', models.CharField(blank=True, max_length=200, null=True, verbose_name='فکس')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل')),
                ('copy_right', models.TextField(verbose_name='متن کپی رایت')),
                ('about_us_text', models.TextField(verbose_name='متن درباره ما')),
                ('site_logo', models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')),
                ('is_main_settings', models.BooleanField(verbose_name='تنظیملات اصلی')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.CharField(max_length=200, verbose_name='توضیحات اسلایدر')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('url_title', models.CharField(max_length=500, verbose_name='عنوان لینک')),
                ('image', models.ImageField(upload_to='images/site-setting/slider-images/', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیر فعال')),
            ],
            options={
                'verbose_name': 'تنظیمات اسلایدر',
                'verbose_name_plural': 'تنظیمات اسلایدر ها',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=202, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_module.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': ' لینک فوتر',
                'verbose_name_plural': ' لینک های فوتر',
            },
        ),
    ]
