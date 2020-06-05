function itemsController($scope) {


    var discount_applied = false;


    $scope.cart = [];
    $scope.discount_row = [];

    // lists 
    $scope.product_list = [
        { code: '0001', quantity: 0, price: 2.00, name: 'Oranges', label: 'Oranges' },
        { code: '0006', quantity: 0, price: 300.00, name: 'Television', label: 'Tele' },
        { code: '0007', quantity: 0, price: 80.00, name: 'casque', label: 'Casque' },
        { code: '0008', quantity: 0, price: 10.00, name: 'Beton', label: 'Beton' },
        { code: '0009', quantity: 0, price: 9.00, name: 'lampe', label: 'lampe' },
        { code: '0010', quantity: 0, price: 15.00, name: 'chassure', label: 'chaussure' },
        { code: '0002', quantity: 0, price: 5.35, name: 'Bananas', label: 'Bananas' },
        { code: '0003', quantity: 0, price: 1.05, name: 'Mangues', label: 'Mangues' },
        { code: '0004', quantity: 0, price: 24.05, name: 'Pawpaw', label: 'Pawpaw' },
        { code: '0005', quantity: 0, price: 6728.15, name: 'Roman Ruby Grapes', label: 'Roman Ruby Grapes' }
    ];

    $scope.search_list = function(name, list) {
        var item = [];
        for (var i in list) {
            if (name == list[i].name) {
                item = list[i];
                break;
            }
        }
        return item;
    }


    $scope.select_product = function() {
        $scope.product = $scope.search_list($scope.inputed_product_name, $scope.product_list);
        $scope.product_cost = $scope.product.price;
    }

    $scope.select_quantity = function() {
        $scope.product.quantity = $scope.inputed_product_quantity;
    }

    $scope.add_to_cart = function() {
        if ($scope.product.name != undefined > 0) {
            $scope.cart[$scope.cart.length] = $scope.product;
            $scope.product = undefined;
            $scope.inputed_product_name = "";
            $scope.product_cost = "";
            $scope.inputed_product_quantity = "1";
        }
    }

    $scope.void_last_transaction = function() {
        $scope.cart.pop();
    }

    $scope.void_sale = function() {
        $scope.cart = [];
        $scope.discount_row = [];
        $scope.product = undefined;
    }

    $scope.apply_discount = function() {
        if ($scope.purchasing_employee.name != undefined) {
            $scope.discount_row[$scope.discount_row.length] = $scope.purchasing_employee;
            discount_applied = true;
        }
    }

    $scope.total = function() {
        if ($scope.cart.length > 0) {
            var sum = 0;
            for (var i in $scope.cart) {
                sum += $scope.cart[i].price * $scope.cart[i].quantity;
            }
            var empDiscount = 0;
            if (discount_applied) {
                empDiscount += $scope.discount_row[0].discount;
            }
            sum *= 1 - empDiscount / 100;
        }
        return sum;
    }

}