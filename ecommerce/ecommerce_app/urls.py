from django.urls import path, include
from .views import*
from ecommerce_app import views
from django.conf.urls.static import static
# from .invoice import*

from rest_framework import routers
routers = routers.DefaultRouter()
routers.register('cancel/order',views.OrderCancelViewSet , "Cancel Order")


urlpatterns = [
    path('', include(routers.urls)),
    # API's for User
    path('register', UserRegistrationView.as_view(), name='User Registration'),
    path('verify', VerifyOtp.as_view(), name='Email Verification'),
    path('login', UserLoginView.as_view(), name='User login'),
    path('list', UserListView.as_view(), name='Users'),
    path('forgot/password', ForgotPasswordView.as_view(), name='Forgot Password'),
    path('reset/password', ResetPasswordView.as_view(), name='Reset Password'),
    path('change/password', ChangePasswordView.as_view(), name='change Password'),
    path('delete/<int:pk>/', DeleteAccountView.as_view(), name='delete account'),

    #API's for profile & delivery man's profile
    path('profile', ProfileView.as_view(), name='Profile'), #Create, Retrieve, Update
    path('profile/list', ProfileList.as_view(), name='Profile List'), #List
    path('delivery/profile', DeliverymanProfile.as_view(), name='Delivery Profile'), #Create, Retrieve, Update
    path('delivery/profile/list', DeliveryProfileList.as_view(), name='Delivery Profile List'), #List
    
    #API's for addresses
    path('address/', AddressView.as_view(), name='Address'), #Create and List 
    path('address/<int:pk>/', AddressById.as_view()), #retrieve, update and delete 
    path('user/address/<int:pk>/', AddressByUserId.as_view()), #retrieve by user id

    #API's for store/settings 
    path('store', StoreView.as_view(), name='Store Settings'), #Create, Retrieve, Update (store settings)
    path('twilio', TwilioView.as_view(), name='Twilio Settings'), #Create, Retrieve, Update (twilio crdentials)
    path('msg91', Msg91View.as_view(), name='Msg 91 Settings'), #Create, Retrieve, Update (Msg91 crdentials)
    path('content', ContentView.as_view(), name='Content Settings'),#Create, Retrieve, Update (content settings)
    path('razorpay', RazorpayView.as_view(), name='Razorpay Settings'),#Create, Retrieve, Update (razorpay settings)
    path('instamojo', InstaMOJOView.as_view(), name='Instamojo Settings'),#Create, Retrieve, Update (instamojo settings)
    path('paytm', PayTMView.as_view(), name='Paytm Settings'),#Create, Retrieve, Update (paytm settings)

    # API's for Banners
    path('banner/create', BannerCreateView.as_view(), name='Create Banner'),
    path('banners', BannersView.as_view(), name='Banner List'),
    path('banner/retrieve/<int:pk>/', BannerRetrieveView.as_view(), name='Banner Retrieve By Id'),
    path('banner/update/<int:pk>/', BannerUpdateView.as_view(), name='Update Banner'),

    # API's for Subscription
    path('subscription', PlanSubscription.as_view()),#create and list
    path('subscription/update/<int:pk>/', PlanSubscriptionUpdate.as_view()), #update
    path('subscription/<int:pk>/', PlanSubscriptioRetrieveDelete.as_view()), #get & delete

    # API's for Category
    path('category/create', CategoryCreateView.as_view(), name='Create Category'),
    path('categories', CategoriesView.as_view(), name='Categories List'),
    path('category/<int:pk>/', CategoryRetrieveView.as_view(), name='Category Retrieve By Id'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='Update Category'),
    path('category/excel/bulk', CategoryBulkUploadView.as_view()),
    path("cate/bulk/delete/", BulkCategoryDelete.as_view()),
    path('category/bulk', BulkCategoryCreateView.as_view(), name='Create bulk Category'),

    # API's for Subcategory
    path('subcategory/create', SubcategoryCreateView.as_view(), name='Create Subcategory'),
    path('subcategories', SubcategoriesView.as_view(), name='Subcategories List'),
    path('subcategory/<int:pk>/', SubcategoryRetrieveView.as_view(), name='Subcategory Retrieve By Id'),
    path('subcategory/update/<int:pk>/', SubcategoryUpdateView.as_view(), name='Update Subcategory'),
    path('subcat/xl/bulk', SubcategoryBulkUploadView.as_view()),
    path('subcategory/bulk', BulkSubcategoryCreateView.as_view(), name='Create bulk Subcategory'),
    path("subcate/bulk/delete/", BulkSubcategoryDelete.as_view()),

    # API's for Products
    path('product/create', ProductsCreateView.as_view(), name='Create Products'),
    path('products', ProductsView.as_view(), name='Products List'),
    path('product/retrieve/<int:pk>/', ProductRetrieve.as_view(), name='Products Retrieve By Id'),
    path('product/update/<int:pk>/', ProductsUpdateView.as_view(), name='Update Products'),
    path('product/discount', BigDiscount.as_view()),#filter. 
    # This api is applicable only if the discount_type is percentage.
    path('product/bulk', BulkProductsCreateView.as_view(), name='Create Bulk Products'),
    path('product/xl/bulk', ProductBulkUploadView.as_view()),
    path("product/bulk/delete/", BulkProductDelete.as_view()), 

    # Product variant APIs
    path('product/variant', VarientsPost.as_view()),# create
    path('product/variant/list', Varientslist.as_view()),# list
    path('product/variant/<int:pk>/', VarientsDetails.as_view()),# retrive / get
    path('variant/update/<int:pk>/', VarientUpdateView.as_view()),# update and delete
    path('variant/xl/bulk', VarientBulkUploadView.as_view()),
    path('variant/bulk', CreateBulkVariants.as_view()),

    # API's for product questions
    path('product/que', ProductQuestionsCreate.as_view()),
    path('product/que/list', ProductQuestionslist.as_view()),
    path('product/que/<int:pk>/', ProductQuestionsDetails.as_view()),
    path('product/question/<int:pk>/', ProductQuestionsView.as_view()),

    # API's for product answers
    path('product/ans', PostAnswer.as_view()),
    path('product/ans/list', Answerslist.as_view()),
    path('product/ans/<int:pk>/', AnswerDetails.as_view()),
    path('product/answers/<int:pk>/', ProductAnswersView.as_view()),

    # API's for product reviews
    path('review', CreateProductReview.as_view()),
    path('review/list', ListProductReview.as_view()),
    path('review/<int:pk>/', RetrieveProductReview.as_view()),
    path('product/review/<int:pk>/', ProductReview.as_view()),

    # API's for count
    path('count', Count.as_view(), name='Count'),
    path('user/count', UserCount.as_view(), name='Count By Role based'),
    # path('revenue', CalculateRevenue.as_view()),

    # wishlist APIs
    path('wishlist', WishListView.as_view(), name='WishList'),

    # cart APIs
    path('cart/', CartView.as_view()),
    # products add to cart, update quantity of product, delete a product from cart
    path('cartlist/', CartlistView.as_view()),

    # checkout APIs
    path('checkout/', Checkout.as_view(), name='cart-checkout'), # order placed
    path('orders/', OrderView.as_view()),# retrieve user orders
    path('orders/list', OrderList.as_view()),
    path('change/status/<int:pk>/', ChangeStatus.as_view()), # change order status
    path('order/address/<int:pk>/', ChangeOrderAddress.as_view()),# change address

    # page CRUD
    path('page', PageView.as_view()),#create, list
    path('page/<int:pk>/', PageDetail.as_view()),#update, retrieve, delete

    # delivery
    path('deliveries', AssigningOrder.as_view()),
    path('delivery/<int:pk>/', AssignedOrdersUpdateView.as_view()),
    # path('invoice/<str:order_id>/', generate_invoice_pdf, name='generate_invoice_pdf'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)