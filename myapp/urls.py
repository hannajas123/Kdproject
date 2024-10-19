from django.urls import path

from myapp import views

urlpatterns=[
path('login/',views.login),
path('login_post/',views.login_post),
path('logout/',views.logout),
path('admin_home/',views.admin_home),
path('Add_kdunit/',views.Add_kdunit),
path('Addkunit_post/',views.Addkunit_post),
path('View_kdunit/',views.View_kdunit),
path('vkunit_post/',views.vkunit_post),
path('Edit_kdunit/<id>',views.Edit_kdunit),
path('editkdunit_post/',views.editkdunit_post),
path('delete_kdunit/<id>',views.delete_kdunit),
path('Add_meeting/<id>',views.Add_meeting),
path('addmeeting_post/',views.addmeeting_post),
path('View_meeting/<id>',views.View_meeting),
path('viewmeeting_post/',views.viewmeeting_post),
path('Edit_meeting/<id>',views.Edit_meeting),
path('delete_meeting/<id>',views.delete_meeting),
path('editmeting_post/',views.editmeting_post),
path('Add_notification/',views.Add_notification),
path('addnotification_post/',views.addnotification_post),
path('View_notification/',views.View_notification),
path('viewnotification_post/',views.viewnotification_post),
path('Edit_notification/<id>',views.Edit_notification),
path('editnotification_post/',views.editnotification_post),
path('Delete_notification/<id>',views.Delete_notification),
path('Change_paassword/',views.Change_paassword),
path('changepassword_post/',views.changepassword_post),
path('View_events/',views.View_events),
path('viewevents_post/',views.viewevents_post),
path('View_feedback/',views.View_feedback),
path('viewfeedback_post/',views.viewfeedback_post),
path('View_kdmembers/<id>',views.View_kdmembers),
path('viewkdmembers_post/',views.viewkdmembers_post),

path('View_users/',views.View_users),
path('viewusers_post/',views.viewusers_post),
path('View_kuris_nd_payment/',views.View_kuris_nd_payment),
path('View_kuris_nd_payment_post/',views.View_kuris_nd_payment_post),
########################### kdunit##########################################################3##########
path('kd_Home/',views.kd_Home),
path('kd_View_profile/',views.kd_View_profile),

path('kd_Add_member/',views.kd_Add_member),
path('kd_Add_member_post/',views.kd_Add_member_post),
path('kd_View_member/',views.kd_View_member),
path('kd_View_member_post/',views.kd_View_member_post),
path('kd_Edit_member/<id>',views.kd_Edit_member),
path('kd_Edit_member_post/',views.kd_Edit_member_post),
path('kd_delete_members/<id>',views.kd_delete_members),

path('kd_Add_events/',views.kd_Add_events),
path('kd_Add_events_post/',views.kd_Add_events_post),
path('kd_View_events/',views.kd_View_events),
path('kd_View_events_post/',views.kd_View_events_post),
path('kd_Edit_events/<id>',views.kd_Edit_events),
path('kd_Edit_events_post/',views.kd_Edit_events_post),
path('kd_delete_events_post/<id>',views.kd_delete_events_post),

path('kd_view_notification_nd_forward/',views.kd_view_notification_nd_forward),
path('frwd_noti/<id>',views.frwd_noti),
path('kd_view_notification_nd_forward_post/',views.kd_view_notification_nd_forward_post),

path('kd_Change_password/',views.kd_Change_password),
path('kd_Change_password_post/',views.kd_Change_password_post),

path('kd_Add_member_meeting/',views.kd_Add_member_meeting),
path('kd_Add_member_meeting_post/',views.kd_Add_member_meeting_post),
path('kd_View_member_meeting/',views.kd_View_member_meeting),
path('kd_View_member_meeting_post/',views.kd_View_member_meeting_post),
path('kd_Edit_member_meeting/<id>',views.kd_Edit_member_meeting),
path('kd_Edit_member_meeting_post/',views.kd_Edit_member_meeting_post),
path('kd_delete_member_meeting_post/<id>',views.kd_delete_member_meeting_post),

path('kd_Add_kuries/',views.kd_Add_kuries),
path('kd_Add_kuries_post/',views.kd_Add_kuries_post),
path('kd_View_kuries/',views.kd_View_kuries),
path('kd_View_kuries_post/',views.kd_View_kuries_post),
path('kd_Edit_kuries/<id>',views.kd_Edit_kuries),
path('kd_Edit_kuries_post/',views.kd_Edit_kuries_post),
path('kd_delete_kuries_post/<id>',views.kd_delete_kuries_post),

path('kd_Add_Product/',views.kd_Add_Product),
path('kd_Add_Product_post/',views.kd_Add_Product_post),
path('kd_View_Product/',views.kd_View_Product),
path('kd_View_Product_post/',views.kd_View_Product_post),
path('kd_Edit_Product/<id>',views.kd_Edit_Product),
path('kd_Edit_Product_post/',views.kd_Edit_Product_post),
path('kd_delete_Product_post/<id>',views.kd_delete_Product_post),

path('kd_View_Order/',views.kd_View_Order),
path('kd_View_Order_post/',views.kd_View_Order_post),

path('kd_View_Payment/',views.kd_View_Payment),
path('kd_View_Payment_post/',views.kd_View_Payment_post),

path('kd_View_Kuri_Payment/',views.kd_View_Kuri_Payment),
path('kd_View_Kuri_Payment_post/',views.kd_View_Kuri_Payment_post),



##################################members#######################################

path('mem_login/',views.mem_login),

path('mem_view_profile/',views.mem_view_profile),

path('mem_change_password/',views.mem_change_password),

path('mem_forwarded_notification/',views.mem_forwarded_notification),

path('mem_view_events/',views.mem_view_events),

path('mem_view_kurees/',views.mem_view_kurees),

path('mem_send_payment/',views.mem_send_payment),

path('mem_view_product/',views.mem_view_product),



    ###########################user#################
path('usr_signup/',views.usr_signup),

path('usr_view_profile/',views.usr_view_profile),
path('usr_edit_profile/',views.usr_edit_profile),

path('usr_view_kdunit/',views.usr_view_kdunit),

path('usr_view_product/',views.usr_view_product),
path('usr_view_productall/',views.usr_view_productall),

# path('usr_place_order/',views.usr_place_order),

path('usr_view_ordered_product/',views.usr_view_ordered_product),

path('User_return_product/',views.User_return_product),
path('User_return_product_post/',views.User_return_product_post),
#
# path('usr_send_payment/',views.usr_send_payment),

path('usr_send_complaint/',views.usr_send_complaint),

path('usr_view_reply/',views.usr_view_reply),

path('usr_view_events/',views.usr_view_events),

path('usr_change_password/',views.usr_change_password),

path('usr_send_feeddback/',views.usr_send_feeddback),

path('User_add_tocart/',views.User_add_tocart),
path('User_AddCart_post/',views.User_AddCart_post),
path('User_View_cart/',views.User_View_cart),

path('user_makepayment/',views.user_makepayment),
















]