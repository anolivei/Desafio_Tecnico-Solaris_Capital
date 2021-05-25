# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 20:31:32 by anolivei          #+#    #+#              #
#    Updated: 2021/05/24 21:05:25 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

FROM python:3.9.1 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

# second unnamed stage
FROM python:3.9.1-slim
WORKDIR /code

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY ./solaris_challenge .

# update PATH environment variable
ENV PATH=/root/.local:$PATH

CMD ["python", "./solaris_challenge.py"]