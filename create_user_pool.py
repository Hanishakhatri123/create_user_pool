import boto3
aws_client = boto3.client('cognito-idp', 
    region_name = "ap-south-1"
)
print("aws",aws_client)

response = aws_client.create_user_pool(
    PoolName='string',
    Policies={
        'PasswordPolicy': {
            'MinimumLength': 8,
            'RequireUppercase': True,
            'RequireLowercase': True,
            'RequireNumbers': True,
            'RequireSymbols': True
        }
    },
    AutoVerifiedAttributes=[
        'email',
    ],
    UsernameAttributes=[
       'email',
    ],
    VerificationMessageTemplate={
        'DefaultEmailOption': 'CONFIRM_WITH_CODE'
    },
    MfaConfiguration='OFF',
    UserAttributeUpdateSettings={
        'AttributesRequireVerificationBeforeUpdate': [
            'email',
        ]
    },
    EmailConfiguration={
        'SourceArn': 'arn:aws:ses:ap-south-1:168933414344:identity/support@offsetmax.digital',
        'ReplyToEmailAddress': 'support@offsetmax.digital',
        'EmailSendingAccount': 'DEVELOPER',
    },
    UsernameConfiguration={
        'CaseSensitive': True
    }
)