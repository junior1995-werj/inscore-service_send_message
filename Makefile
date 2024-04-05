NAMESPACE=inscore

PROJECT_NAME =service_send_message

AWS_ACCOUNT_ID=230291670968

CURRENT_VERSION=$(shell aws ecr describe-images --repository-name inscore/service_send_message --region us-east-1 --query 'sort_by(imageDetails,& imagePushedAt)[-1].imageTags' | grep v | grep -Eo '[0-9]' |  head -1)

NEW_VERSION = $(shell expr $(CURRENT_VERSION) + 1 )

install:
	poetry install

create-git-tag:
	git tag -a v$(NEW_VERSION) -m \
		"Creation of v$(NEW_VERSION): $(AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/$(NAMESPACE)/$(PROJECT_NAME):v$(NEW_VERSION)"

ecr-authenticate:
	aws ecr get-login-password \
		--region us-east-1 | docker login \
		--username AWS \
		--password-stdin $(AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com

build-image:
	docker  build -t $(PROJECT_NAME) .

tag-image:
	docker tag $(PROJECT_NAME):latest $(AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/$(NAMESPACE)/$(PROJECT_NAME):v$(NEW_VERSION)

push-image:
	docker push $(AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/$(NAMESPACE)/$(PROJECT_NAME):v$(NEW_VERSION)

pull-image:
	docker pull $(AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/$(NAMESPACE)/$(PROJECT_NAME):v$(CURRENT_VERSION)

build-push-image:
	@make ecr-authenticate
	@make build-image
	@make tag-image
	@make push-image


