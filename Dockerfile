FROM postgres:latest
LABEL author="Jeongsup Byun <jeongsup.byun@gmail.com>"

## Set timezone to Melbourne
RUN echo Australia/Melbourne > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata