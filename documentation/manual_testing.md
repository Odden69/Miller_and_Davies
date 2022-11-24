## Manual Testing of Miller and Davies

### Link Tests
| Link | Action | Confirmation Message |
|:-------------|:-----------:|:------------------------:|
| **Footer** |  |  |
| Facebook | :heavy_check_mark: | - |
| Instagram | :heavy_check_mark: | - |
| |  |  |
| **Header, wide screen** |  |  |
| Logo | :heavy_check_mark: | - |
| Basket | :heavy_check_mark: | - |
| **Header, small screen** |  |  |
| Logo |  |
| |  |  |
| **Navbar, not logged in, wide screen** |  |  |
| Products, By Name|  | - |
| Products, By Price|  | - |
| Products, By Rating|  | - |
| Vegetables |  | - |
| Flowers |  | - |
| Herbs |  | - |
| Indoor Growing |  | - |
| Bargains |  | - |
| Favorites|  | - |
| User, Sign Up |  | - |
| User, Log In |  | - |
| |  |  |
| **Navbar, not logged in, small screen** |  |  |
| Collapse, Products, By Name |  | - |
| Collapse, Products, By Price |  | - |
| Collapse, Products, By Rating |  | - |
| Collapse, Vegetables, All |  | - |
| Collapse, Vegetables, Cucurbits |  | - |
| Collapse, Vegetables, Leafy Greens |  | - |
| Collapse, Vegetables, Legumes |  | - |
| Collapse, Vegetables, Onions |  | - |
| Collapse, Vegetables, Peppers |  | - |
| Collapse, Vegetables, Root Veg |  | - |
| Collapse, Vegetables, Tomatoes |  | - |
| Collapse, Vegetables, Various Veg |  | - |
| Collapse, Flowers, All |  | - |
| Collapse, Flowers, Annuals |  | - |
| Collapse, Flowers, Biennuals |  | - |
| Collapse, Flowers, Perennials |  | - |
| Collapse, Herbs |  | - |
| Collapse, Indoor Growing |  | - |
| Collapse, Bargains |  | - |
| Collapse, User, Sign Up |  | - |
| Collapse, User, Log In |  | - |
| Basket |  | - |
| **Navbar, reg user, wide screen** |  |  |
| User, My Profile |  | - |
| User, Log Out |  | - |
| **Navbar, reg user, small screen** |  |  |

| **Navbar, admin user, wide screen** |  |  |
| **Navbar, admin user, small screen** |  |  |
| **Header** |  |  |


### Page Tests
| Page | Lighthouse, Desktop | Lighthouse, Mobile | Responsive, Desktop | Responsive, Tablet | Responsive, Mobile | HTML-validator W3 |
|:-----|:-------------------:|:------------------:|:-------------------:|:------------------:|:------------------:|:-----------------:|
|  |  |  |  |  |  |  |
| Product |  |  |
| Product Detail |  |  |
| Basket |  |  |
| Checkout |  |  |
| Log In | :heavy_check_mark: | - |
| Sign Up |
| Instagram | :heavy_check_mark: | - |
| |  |  |
| **Header, wide screen** |  |  |
| Logo | :heavy_check_mark: | - |
| Basket | :heavy_check_mark: | - |


### Code Tests
| File | Jigsaw validator | pep8 pylint django | JSHint |
|:-----|:----------------:|:------------------:|:------:|
|  |  |  |  |
| **Basket** |  |  |  |
| contexts.py |  | :heavy_check_mark: |  |
| urls.py |  | :heavy_check_mark: |  |
| views.py |  | :heavy_check_mark: |  |
|  |  |  |  |
| **Checkout** |  |  |  |
| admin.py |  | :heavy_check_mark: |  |
| forms.py |  | :heavy_check_mark: |  |
| models.py |  | :heavy_check_mark: |  |
| signals.py |  | :heavy_check_mark: |  |
| urls.py |  | :heavy_check_mark: |  |
| views.py |  | :heavy_check_mark: |  |
| webhook_handler.py |  | :heavy_check_mark: |  |
| webhooks.py |  | :heavy_check_mark: |  |
|  |  |  |  |
| **Favorites** |  |  |  |
| urls.py |  | :heavy_check_mark: |  |
| views.py |  | :heavy_check_mark: |  |
|  |  |  |  |
| **Newsletters** |  |  |  |
| admin.py |  | :heavy_check_mark: |  |
| contexts.py |  | :heavy_check_mark: |  |
| forms.py |  | :heavy_check_mark: |  |
| models.py |  | :heavy_check_mark: |  |
|  |  |  |  |
| **Products** |  |  |  |
| admin.py |  | :heavy_check_mark: |  |
| forms.py |  | :heavy_check_mark: |  |
| models.py |  | :heavy_check_mark: |  |
| urls.py |  | :heavy_check_mark: |  |
| views.py |  | :heavy_check_mark: |  |
| widgets.py |  | :heavy_check_mark: |  |
|  |  |  |  |
| **Profiles** |  |  |  |
| admin.py |  | :heavy_check_mark: |  |
| forms.py |  | :heavy_check_mark: |  |
| models.py |  | :heavy_check_mark: |  |
| urls.py |  | :heavy_check_mark: |  |
| views.py |  | :heavy_check_mark: |  |
|  |  |  |  |
|  |  |  |  |
| **Miller_n_davies** |  |  |  |
| forms.py |  | :heavy_check_mark: |  |
| settings.py |  | long lines and env imported not used |  |
| urls.py |  | :heavy_check_mark: |  |
| views.py |  | :heavy_check_mark: |  |
|  |  |  |  |
|  |  |  |  |
| custom_storages.py |  | :heavy_check_mark: |  |


