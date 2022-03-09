# iamheadless_publisher_site_redirects

App to capture and redirect urls in `iamheadless_publisher_site` site

## Requires:
- `iamheadless_publisher_site`

## Installation

1. install package
2. add `iamheadless_publisher_site_redirects` to `INSTALLED_APPS` in `settings.py`
3. add `iamheadless_publisher_site_redirects.middleware.IamheadlessPublisherSiteRedirectMiddleware` to `MIDDLEWARE` in `settings.py`
4. add `iamheadless_publisher_site_redirects.pydantic_models.RedirectPydanticModel` to `IAMHEADLESS_PUBLISHER_SITE_SERIALIZER_LIST` in `settings.py`

