from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from serendipity import create_app
from exts import db
from apps.cms import models as cms_models

CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPersmission

app = create_app()

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('CMS User created successfully!')


@manager.command
def create_role():
    # 1. Visitors (can change personal information)
    visitor = CMSRole(name='visitor', desc='can only change personal information')
    visitor.permissions = CMSPermission.VISITOR

    # 2. Operation roles (modify personal information, manage posts, manage comments, manage front desk users)
    operator = CMSRole(name='operation_specialist', desc='Manage posts, manage comments, manage front desk users')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER

    # 3. Administrators (with most of the privileges)
    admin = CMSRole(name='administrator', desc='Have all permissions for this system')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER | CMSPermission.BOARDER

    # 4. Developer (all permissions)
    developer = CMSRole(name='developer', desc='Developer-only role')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


if __name__ == '__main__':
    manager.run()
