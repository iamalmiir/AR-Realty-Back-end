def change_password(user, old_password, new_password, response, status):
    if user.check_password(old_password):
        user.set_password(new_password)
        user.save()
        return Response(
            {"message": "Password changed successfully"}, status=status.HTTP_200_OK
        )
    return Response(
        {"message": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST
    )
