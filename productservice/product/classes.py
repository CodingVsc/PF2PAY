from rest_framework import permissions, mixins, viewsets


class MixedPermissions:
    """Mixin permissions for actions."""

    def get_permissions(self):
        try:
            return [permission() for
                    permission in self.permission_classes_by_actions[self.action]]
        except KeyError:
            return [permission() for
                    permission in self.permission_classes]


class RetrieveUpdateDestroyDS(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              MixedPermissions,
                              viewsets.GenericViewSet):
    pass


class ListCreateUpdateDestroyDS(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                MixedPermissions,
                                viewsets.GenericViewSet):
    pass
