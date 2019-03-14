from django.utils.translation import ugettext as _
from oidc_provider.lib.claims import StandardScopeClaims


class CustomScopeClaims(StandardScopeClaims):
    info_foo = (
        _(u'Foo'),
        _(u'Some description for the scope.'),
    )

    def scope_foo(self):
        # self.user - Django user instance.
        # self.userinfo - Dict returned by OIDC_USERINFO function.
        # self.scopes - List of scopes requested.
        # self.client - Client requesting this claims.
        dic = {
            'bar': 'Something dynamic here',
        }

        return dic


# def userinfo(claims, user):
#     claims['name'] = '{0} {1}'.format(user.first_name, user.last_name)
#     claims['first_name'] = user.first_name
#     claims['last_name'] = user.last_name
#     claims['email'] = user.email
#
#     return claims
