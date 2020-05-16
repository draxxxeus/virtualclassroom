def user_registrations(request):
    registrations = {}
    if request.user.is_authenticated:
        registrations = {'registrations': list(request.user.registration_set.all())}  # noqa: E501

    return registrations
