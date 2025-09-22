# FlowMart EventCatalog Documentation

> Welcome to FlowMart EventCatalog. Here you can find all the information you need to know about our events and services (demo catalog).

## Events
- [Inventory adjusted - InventoryAdjusted - 1.0.1 ](https://demo.eventcatalog.dev/docs/events/InventoryAdjusted/1.0.1.mdx) - Indicates a change in inventory level
- [Inventory out of stock - OutOfStock - 0.0.4 ](https://demo.eventcatalog.dev/docs/events/OutOfStock/0.0.4.mdx) - Indicates inventory is out of stock
- [Order cancelled - OrderCancelled - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/OrderCancelled/0.0.1.mdx) - Indicates an order has been canceled
- [Order confirmed - OrderConfirmed - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/OrderConfirmed/0.0.1.mdx) - Indicates an order has been confirmed
- [Order amended - OrderAmended - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/OrderAmended/0.0.1.mdx) - Indicates an order has been changed
- [Delivery failed - DeliveryFailed - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/DeliveryFailed/0.0.1.mdx) - Event that is emitted when a shipment delivery fails.
- [Return initiated - ReturnInitiated - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/ReturnInitiated/0.0.1.mdx) - Event that is emitted when a return is initiated.
- [Shipment created - ShipmentCreated - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/ShipmentCreated/0.0.1.mdx) - Event that is emitted when a shipment is created.
- [Shipment delivered - ShipmentDelivered - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/ShipmentDelivered/0.0.1.mdx) - Event that is emitted when a shipment is delivered.
- [Shipment dispatched - ShipmentDispatched - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/ShipmentDispatched/0.0.1.mdx) - Event that is emitted when a shipment is dispatched.
- [Shipment in transit - ShipmentInTransit - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/ShipmentInTransit/0.0.1.mdx) - Event that is emitted when a shipment is in transit.
- [Fraud Check Completed - FraudCheckCompleted - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/FraudCheckCompleted/0.0.1.mdx) - Emitted when a fraud check has been completed for a transaction- [Fraud Detected - FraudDetected - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/FraudDetected/0.0.1.mdx) - Emitted when a fraud is detected in a transaction- [Risk Score Calculated - RiskScoreCalculated - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/RiskScoreCalculated/0.0.1.mdx) - Emitted when a risk score is calculated for a transaction- [Payment Failed - PaymentFailed - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/PaymentFailed/0.0.1.mdx) - Emitted when a payment attempt fails- [Payment Complete - PaymentComplete - 0.0.2 ](https://demo.eventcatalog.dev/docs/events/PaymentComplete/0.0.2.mdx) - Event is triggered when a user completes a payment through the Payment Service- [Payment Initiated - PaymentInitiated - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/PaymentInitiated/0.0.1.mdx) - Event is triggered when a user initiates a payment through the Payment Service- [Payment Processed - PaymentProcessed - 1.0.0 ](https://demo.eventcatalog.dev/docs/events/PaymentProcessed/1.0.0.mdx) - Event is triggered after the payment has been successfully processed- [Subscription Payment Due - SubscriptionPaymentDue - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/SubscriptionPaymentDue/0.0.1.mdx) - Emitted when a subscription payment is due for collection- [User subscription cancelled - UserSubscriptionCancelled - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/UserSubscriptionCancelled/0.0.1.mdx) - An event that is triggered when a users subscription has been cancelled
- [User subscription started - UserSubscriptionStarted - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/UserSubscriptionStarted/0.0.1.mdx) - An event that is triggered when a new user subscription has started
- [Inventory adjusted - InventoryAdjusted - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/InventoryAdjusted/0.0.1.mdx) - Indicates a change in inventory level
- [Inventory adjusted - InventoryAdjusted - 1.0.0 ](https://demo.eventcatalog.dev/docs/events/InventoryAdjusted/1.0.0.mdx) - Indicates a change in inventory level
- [Inventory out of stock - OutOfStock - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/OutOfStock/0.0.1.mdx) - Indicates inventory is out of stock
- [Payment Processed - PaymentProcessed - 0.0.1 ](https://demo.eventcatalog.dev/docs/events/PaymentProcessed/0.0.1.mdx) - Event is triggered after the payment has been successfully processed

## Commands
- [Delete Inventory - DeleteInventory - 0.0.3 ](https://demo.eventcatalog.dev/docs/commands/DeleteInventory/0.0.3.mdx) - Command that will delete a given inventory item from the system
- [Update inventory - UpdateInventory - 0.0.3 ](https://demo.eventcatalog.dev/docs/commands/UpdateInventory/0.0.3.mdx) - Command that will update a given inventory item
- [Add inventory - AddInventory - 0.0.3 ](https://demo.eventcatalog.dev/docs/commands/AddInventory/0.0.3.mdx) - Command that will add item to a given inventory id
- [Place Order - PlaceOrder - 0.0.1 ](https://demo.eventcatalog.dev/docs/commands/PlaceOrder/0.0.1.mdx) - Command that will place an order
- [Cancel shipment - CancelShipment - 0.0.1 ](https://demo.eventcatalog.dev/docs/commands/CancelShipment/0.0.1.mdx) - POST request that will cancel a shipment, identified by its shipmentId.
- [Create return label - CreateReturnLabel - 0.0.1 ](https://demo.eventcatalog.dev/docs/commands/CreateReturnLabel/0.0.1.mdx) - POST request that will create a return label for a specific shipment, identified by its shipmentId.
- [Create shipment - CreateShipment - 0.0.1 ](https://demo.eventcatalog.dev/docs/commands/CreateShipment/0.0.1.mdx) - POST request that will create a shipment for a specific order, identified by its orderId.
- [Update shipment status - UpdateShipmentStatus - 0.0.1 ](https://demo.eventcatalog.dev/docs/commands/UpdateShipmentStatus/0.0.1.mdx) - POST request that will update the status of a shipment, identified by its shipmentId.
- [Process Payment - ProcessPayment - 0.0.1 ](https://demo.eventcatalog.dev/docs/commands/ProcessPayment/0.0.1.mdx) - Command to process a payment through the payment gateway- [Cancel subscription - CancelSubscription - 0.0.1 ](https://demo.eventcatalog.dev/docs/commands/CancelSubscription/0.0.1.mdx) - Command that will try and cancel a users subscription
- [Subscribe user - SubscribeUser - 0.0.1 ](https://demo.eventcatalog.dev/docs/commands/SubscribeUser/0.0.1.mdx) - Command that will try and subscribe a given user


## Queries
- [List inventory list - GetInventoryList - 0.0.1 ](https://demo.eventcatalog.dev/docs/queries/GetInventoryList/0.0.1.mdx) - GET request that will return inventory list
- [Get inventory status - GetInventoryStatus - 0.0.1 ](https://demo.eventcatalog.dev/docs/queries/GetInventoryStatus/0.0.1.mdx) - GET request that will return the current stock status for a specific product.
- [Get user notifications - GetUserNotifications - 0.0.1 ](https://demo.eventcatalog.dev/docs/queries/GetUserNotifications/0.0.1.mdx) - GET request that will return a list of notifications for a specific user, with options to filter by status (unread or all).
- [Get notification details - GetNotificationDetails - 0.0.1 ](https://demo.eventcatalog.dev/docs/queries/GetNotificationDetails/0.0.1.mdx) - GET request that will return detailed information about a specific notification, identified by its notificationId.
- [Get order details - GetOrder - 0.0.1 ](https://demo.eventcatalog.dev/docs/queries/GetOrder/0.0.1.mdx) - GET request that will return detailed information about a specific order, identified by its orderId.
- [Get payment status - GetPaymentStatus - 0.0.1 ](https://demo.eventcatalog.dev/docs/queries/GetPaymentStatus/0.0.1.mdx) - GET request that will return the payment status for a specific order, identified by its orderId.
- [Get subscription status - GetSubscriptionStatus - 0.0.2 ](https://demo.eventcatalog.dev/docs/queries/GetSubscriptionStatus/0.0.2.mdx) - GET request that will return the current subscription status for a specific user, identified by their userId.
- [Get subscription status - GetSubscriptionStatus - 0.0.1 ](https://demo.eventcatalog.dev/docs/queries/GetSubscriptionStatus/0.0.1.mdx) - GET request that will return the current subscription status for a specific user, identified by their userId.


## Services
- [Inventory Service - InventoryService - 0.0.2 ](https://demo.eventcatalog.dev/docs/services/InventoryService/0.0.2.mdx) - Service that handles the inventory
- [Notifications - NotificationService - 0.0.2 ](https://demo.eventcatalog.dev/docs/services/NotificationService/0.0.2.mdx) - Service that handles orders
- [Orders Service - OrdersService - 0.0.3 ](https://demo.eventcatalog.dev/docs/services/OrdersService/0.0.3.mdx) - Service that handles orders
- [Shipping Service - ShippingService - 0.0.1 ](https://demo.eventcatalog.dev/docs/services/ShippingService/0.0.1.mdx) - Service that handles shipping
- [Fraud Detection Service - FraudDetectionService - 0.0.1 ](https://demo.eventcatalog.dev/docs/services/FraudDetectionService/0.0.1.mdx) - Analyzes payment transactions for fraudulent activity and risk assessment- [Payment Gateway Service - PaymentGatewayService - 0.0.1 ](https://demo.eventcatalog.dev/docs/services/PaymentGatewayService/0.0.1.mdx) - Manages integration with external payment processors (Stripe, PayPal, etc.)- [Payment Service - PaymentService - 0.0.1 ](https://demo.eventcatalog.dev/docs/services/PaymentService/0.0.1.mdx) - Service that handles payments
- [Billing Service - BillingService - 0.0.1 ](https://demo.eventcatalog.dev/docs/services/BillingService/0.0.1.mdx) - Manages billing cycles, invoice generation, and payment scheduling for subscriptions- [Subscription Service - SubscriptionService - 0.0.1 ](https://demo.eventcatalog.dev/docs/services/SubscriptionService/0.0.1.mdx) - Service that handles subscriptions
- [Inventory Service - InventoryService - 0.0.1 ](https://demo.eventcatalog.dev/docs/services/InventoryService/0.0.1.mdx) - Service that handles the inventory
- [Orders Service - OrdersService - 0.0.2 ](https://demo.eventcatalog.dev/docs/services/OrdersService/0.0.2.mdx) - Service that handles orders


## Domains
- [E-Commerce - E-Commerce - 1.0.0 ](https://demo.eventcatalog.dev/docs/domains/E-Commerce/1.0.0.mdx) - [Orders - Orders - 0.0.3 ](https://demo.eventcatalog.dev/docs/domains/Orders/0.0.3.mdx) - [Payment - Payment - 0.0.1 ](https://demo.eventcatalog.dev/docs/domains/Payment/0.0.1.mdx) - Domain that contains payment related services and messages for processing financial transactions.
- [Product Catalog - ProductCatalog - 0.0.1 ](https://demo.eventcatalog.dev/docs/domains/ProductCatalog/0.0.1.mdx) - Manages product information, categories, inventory, and customer reviews in the e-commerce system.- [Subscriptions - Subscriptions - 0.0.1 ](https://demo.eventcatalog.dev/docs/domains/Subscriptions/0.0.1.mdx) - Manages subscription lifecycle, billing cycles, and plan management for recurring revenue streams.
- [Orders - Orders - 0.0.1 ](https://demo.eventcatalog.dev/docs/domains/Orders/0.0.1.mdx) - Domain for everything shopping
- [Orders - Orders - 0.0.2 ](https://demo.eventcatalog.dev/docs/domains/Orders/0.0.2.mdx) 

## Flows
- [Payment Flow for customers - PaymentFlow - 1.0.0 ](https://demo.eventcatalog.dev/docs/flows/PaymentFlow/1.0.0.mdx) - Business flow for processing payments in an e-commerce platform
- [User Cancels Subscription - CancelSubscription - 1.0.0 ](https://demo.eventcatalog.dev/docs/flows/CancelSubscription/1.0.0.mdx) - Flow for when a user has cancelled a subscription
- [Subscription Renewal Flow - SubscriptionRenewed - 1.0.0 ](https://demo.eventcatalog.dev/docs/flows/SubscriptionRenewed/1.0.0.mdx) - Business flow for automatic subscription renewals and related processes
- [User Cancels Subscription - CancelSubscription - 0.0.1 ](https://demo.eventcatalog.dev/docs/flows/CancelSubscription/0.0.1.mdx) - Flow for when a user has cancelled a subscription

## Channels
- [Inventory Events Channel - inventory.{env}.events - 1.0.0 - protocol - kafka](https://demo.eventcatalog.dev/docs/channels/inventory.{env}.events/1.0.0.mdx) - Central event stream for all inventory-related events including stock updates, allocations, and adjustments
- [Order Events Channel - orders.{env}.events - 1.0.1 - protocol - azure-servicebus](https://demo.eventcatalog.dev/docs/channels/orders.{env}.events/1.0.1.mdx) - Central event stream for all order-related events in the order processing lifecycle
- [Payment Events Channel - payments.{env}.events - 1.0.0 - protocol - kafka](https://demo.eventcatalog.dev/docs/channels/payments.{env}.events/1.0.0.mdx) - All events contain payment ID for traceability and ordered processing.

## Ubiquitous Language
- Orders Domain
    - [Payment: - The act of paying for magical goods or services.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [Purchase Order: - A mystical document issued by a buyer to a seller indicating the types, quantities, and agreed prices for enchanted products or services.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [Order Line: - An individual enchanted item within a purchase order, representing a specific magical product or service being ordered.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [SKU: - Sorcery Keeping Unit - A unique identifier for distinct magical products and their variants in inventory.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [Consignment: - A batch of enchanted goods destined for or delivered to someone.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [Invoice: - A document issued by a seller to a buyer, listing enchanted goods or services provided and the amount due.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [Supplier: - An entity that provides enchanted goods or services to another organization.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [Inventory: - The complete list of enchanted items held in stock by a business.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [Fulfillment: - The process of completing an order and delivering it to the customer.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
    - [Return: - The process of sending back enchanted goods to the seller for a refund or exchange.](https://demo.eventcatalog.dev/docs/domains/Orders/language.mdx)
- Payment Domain
    - [Transaction: - The process of transferring funds from one party to another.](https://demo.eventcatalog.dev/docs/domains/Payment/language.mdx)
    - [Invoice: - A document issued by a seller to a buyer, listing goods or services provided and the amount due.](https://demo.eventcatalog.dev/docs/domains/Payment/language.mdx)
    - [Payment Method: - The means by which a payment is made, such as credit card or bank transfer.](https://demo.eventcatalog.dev/docs/domains/Payment/language.mdx)
    - [Receipt: - A document acknowledging that a payment has been made.](https://demo.eventcatalog.dev/docs/domains/Payment/language.mdx)
    - [Refund: - The process of returning funds to a customer for a returned product or service.](https://demo.eventcatalog.dev/docs/domains/Payment/language.mdx)
    - [Currency: - The system of money in general use in a particular country.](https://demo.eventcatalog.dev/docs/domains/Payment/language.mdx)
    - [Payment Gateway: - A service that authorizes and processes payments for online and offline transactions.](https://demo.eventcatalog.dev/docs/domains/Payment/language.mdx)
    - [Chargeback: - A demand by a credit card provider for a retailer to make good the loss on a fraudulent or disputed transaction.](https://demo.eventcatalog.dev/docs/domains/Payment/language.mdx)
- Subscriptions Domain
    - [Subscription: - A recurring agreement where a customer pays for access to a product or service at regular intervals.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)
    - [Billing Cycle: - The recurring period for which a subscription is billed.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)
    - [Plan: - A specific subscription offering with defined features, pricing, and terms.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)
    - [Trial Period: - A promotional period allowing customers to test a subscription service before committing.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)
    - [Auto-Renewal: - Automatic continuation of a subscription at the end of each billing period.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)
    - [Upgrade: - The process of moving to a higher-tier subscription plan.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)
    - [Downgrade: - The process of moving to a lower-tier subscription plan.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)
    - [Cancellation: - The termination of a subscription service.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)
    - [Usage Limit: - Restrictions on service usage within a subscription plan.](https://demo.eventcatalog.dev/docs/domains/Subscriptions/language.mdx)

## Entities
- Orders Domain
    - [Order](https://demo.eventcatalog.dev/docs/entities/Order/1.0.0.mdx) - Represents a customer's request to purchase products or services.
    - [OrderItem](https://demo.eventcatalog.dev/docs/entities/OrderItem/1.0.0.mdx) - Represents a single item within a customer's order.
    - [Customer](https://demo.eventcatalog.dev/docs/entities/Customer/1.0.0.mdx) - Represents an individual or organization that places orders.
    - [ShoppingCart](https://demo.eventcatalog.dev/docs/entities/ShoppingCart/1.0.0.mdx) - Represents a customer's shopping cart containing products before checkout.
    - [CartItem](https://demo.eventcatalog.dev/docs/entities/CartItem/1.0.0.mdx) - Represents an individual item within a shopping cart.
- Payment Domain
    - [Invoice](https://demo.eventcatalog.dev/docs/entities/Invoice/1.0.0.mdx) - Represents a bill issued to a customer, detailing charges for products or services.
    - [Payment](https://demo.eventcatalog.dev/docs/entities/Payment/1.0.0.mdx) - Represents payment transactions for orders in the e-commerce system.
    - [PaymentMethod](https://demo.eventcatalog.dev/docs/entities/PaymentMethod/1.0.0.mdx) - Represents a payment instrument a customer can use, like a credit card or bank account.
    - [Transaction](https://demo.eventcatalog.dev/docs/entities/Transaction/1.0.0.mdx) - Represents a low-level interaction with a payment gateway or processor (e.g., authorize, capture, refund, void).
    - [Address](https://demo.eventcatalog.dev/docs/entities/Address/1.0.0.mdx) - Represents shipping and billing addresses for customers and orders.
- Product Catalog Domain
    - [Product](https://demo.eventcatalog.dev/docs/entities/Product/1.0.0.mdx) - Represents a product or service available for purchase in the e-commerce system.
    - [Category](https://demo.eventcatalog.dev/docs/entities/Category/1.0.0.mdx) - Represents a product category with hierarchical structure support.
    - [Inventory](https://demo.eventcatalog.dev/docs/entities/Inventory/1.0.0.mdx) - Tracks stock levels and availability for products.
    - [Review](https://demo.eventcatalog.dev/docs/entities/Review/1.0.0.mdx) - Represents customer reviews and ratings for products.
- Subscriptions Domain
    - [BillingProfile](https://demo.eventcatalog.dev/docs/entities/BillingProfile/1.0.0.mdx) - Stores billing-related contact information and preferences for a customer, often used for invoices and communication.
    - [SubscriptionPeriod](https://demo.eventcatalog.dev/docs/entities/SubscriptionPeriod/1.0.0.mdx) - Represents a single billing cycle or interval within a subscription's lifetime.

## Teams
- [full-stack](https://demo.eventcatalog.dev/docs/teams/full-stack.mdx) - Full stackers
- [mobile-devs](https://demo.eventcatalog.dev/docs/teams/mobile-devs.mdx) - The mobile devs
- [order-management](https://demo.eventcatalog.dev/docs/teams/order-management.mdx) - The order management team
- [subscriptions-management](https://demo.eventcatalog.dev/docs/teams/subscriptions-management.mdx) - The subscriptions management team

## Users
- [asmith](https://demo.eventcatalog.dev/docs/users/asmith.mdx) - Amy Smith
- [alee](https://demo.eventcatalog.dev/docs/users/alee.mdx) - Alice Lee
- [azhang](https://demo.eventcatalog.dev/docs/users/azhang.mdx) - Alice Zhang
- [dboyne](https://demo.eventcatalog.dev/docs/users/dboyne.mdx) - David Boyne
- [dkim](https://demo.eventcatalog.dev/docs/users/dkim.mdx) - David Kim
- [jbrown](https://demo.eventcatalog.dev/docs/users/jbrown.mdx) - Jessica Brown
- [jchen](https://demo.eventcatalog.dev/docs/users/jchen.mdx) - Julia Chen
- [jmiller](https://demo.eventcatalog.dev/docs/users/jmiller.mdx) - James Miller
- [kpatel](https://demo.eventcatalog.dev/docs/users/kpatel.mdx) - Kiran Patel
- [lkim](https://demo.eventcatalog.dev/docs/users/lkim.mdx) - Lisa Kim
- [lnguyen](https://demo.eventcatalog.dev/docs/users/lnguyen.mdx) - Lily Nguyen
- [msmith](https://demo.eventcatalog.dev/docs/users/msmith.mdx) - Martin Smith
- [mchen](https://demo.eventcatalog.dev/docs/users/mchen.mdx) - Michelle Chen
- [mwang](https://demo.eventcatalog.dev/docs/users/mwang.mdx) - Michael Wang
- [mwilson](https://demo.eventcatalog.dev/docs/users/mwilson.mdx) - Mike Wilson
- [nshah](https://demo.eventcatalog.dev/docs/users/nshah.mdx) - Nina Shah
- [rjohnson](https://demo.eventcatalog.dev/docs/users/rjohnson.mdx) - Robert Johnson
- [rjones](https://demo.eventcatalog.dev/docs/users/rjones.mdx) - Robert Jones
- [rsingh](https://demo.eventcatalog.dev/docs/users/rsingh.mdx) - Raj Singh
- [rthomas](https://demo.eventcatalog.dev/docs/users/rthomas.mdx) - Ray Thomas
- [slee](https://demo.eventcatalog.dev/docs/users/slee.mdx) - Sarah Lee
- [spatel](https://demo.eventcatalog.dev/docs/users/spatel.mdx) - Sanya Patel
- [tgarcia](https://demo.eventcatalog.dev/docs/users/tgarcia.mdx) - Tom Garcia

## Custom Docs
- [Creating new microservices](https://demo.eventcatalog.dev/docs/custom/guides/creating-new-microservices/01-index.mdx) - A comprehensive guide to creating new microservices at FlowMart following our best practices and standards
- [Microservice Design Principles](https://demo.eventcatalog.dev/docs/custom/guides/creating-new-microservices/02-service-design-principles.mdx) - Core design principles and best practices for creating well-structured microservices at FlowMart
- [Database Patterns for Microservices](https://demo.eventcatalog.dev/docs/custom/guides/creating-new-microservices/03-database-patterns.mdx) - Best practices and patterns for managing data in FlowMart microservices
- [Event Schema Design](https://demo.eventcatalog.dev/docs/custom/guides/creating-new-microservices/04-event-schemas.mdx) - Best practices for designing and managing event schemas in FlowMart's event-driven architecture
- [New TypeScript service](https://demo.eventcatalog.dev/docs/custom/guides/creating-new-microservices/06-typescript-service.mdx) - Guide to implementing microservices using TypeScript at FlowMart
- [Getting Started with Event Storming](https://demo.eventcatalog.dev/docs/custom/guides/event-storming/01-index.mdx) - Learn how to use Event Storming to discover and model your business domain effectively
- [Facilitating an Event Storming Session](https://demo.eventcatalog.dev/docs/custom/guides/event-storming/02-facilitation.mdx) - A comprehensive guide on how to run effective Event Storming workshops at FlowMart
- [From Event Storming to Implementation](https://demo.eventcatalog.dev/docs/custom/guides/event-storming/03-implementation.mdx) - Learn how to transform Event Storming outcomes into concrete microservice implementations at FlowMart
- [Inventory Service - Runbook](https://demo.eventcatalog.dev/docs/custom/operations-and-support/runbooks/inventory-service-runbook.mdx) - Operational runbook for troubleshooting and maintaining the InventoryService
- [OrdersService Runbook](https://demo.eventcatalog.dev/docs/custom/operations-and-support/runbooks/orders-service-runbook.mdx) - Operational runbook for troubleshooting and maintaining the OrdersService
- [PaymentService Runbook](https://demo.eventcatalog.dev/docs/custom/operations-and-support/runbooks/payment-service-runbook.mdx) - Operational runbook for troubleshooting and maintaining the PaymentService
- [ShippingService Runbook](https://demo.eventcatalog.dev/docs/custom/operations-and-support/runbooks/shipping-service-runbook.mdx) - Operational runbook for troubleshooting and maintaining the ShippingService
- [Architecture Decision Records (ADR)](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/01-architecture-desicion-record.mdx) - A document that captures important architectural decisions and their context
- [Infrastructure as Code (IaC) Overview](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/infrastructure-as-code/01-iac-overview.mdx) - An overview of the infrastructure-as-code approach used in the FlowMart e-commerce platform
- [Terraform Implementation](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/infrastructure-as-code/02-terraform-implementation.mdx) - Details of how Terraform is used to provision and manage the FlowMart infrastructure
- [Environment Setups](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/infrastructure-as-code/03-environment-setups.mdx) - Detailed information about the different environments for the FlowMart e-commerce platform
- [CI/CD Pipelines](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/infrastructure-as-code/04-cicd-pipelines.mdx) - Detailed overview of the CI/CD pipelines used to deploy and maintain the FlowMart e-commerce platform
- [High-Level FlowMart System Architecture Overview](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/system-architecture-diagrams/01-high-level-system-overview.mdx) - A high-level overview of the FlowMart e-commerce system architecture
- [FlowMart Domain-Level Architecture](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/system-architecture-diagrams/02-domain-level-architecture.mdx) - A detailed view of FlowMart's domain architecture showing bounded contexts and domain interactions
- [FlowMart Service-Level Architecture](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/system-architecture-diagrams/03-service-level-architecture.mdx) - A detailed view of the services within each domain and their interactions
- [Cloud Infrastructure Strategy](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/drafts/01-cloud-infrastructure-strategy.mdx) - Architectural decision record for cloud infrastructure approach for the FlowMart e-commerce platform
- [FlowMart Data Flow Architecture](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/system-architecture-diagrams/04-data-flow-architecture.mdx) - A detailed view of key data flows and business processes within the FlowMart e-commerce platform
- [CI/CD and Deployment Strategy](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/drafts/02-cicd-deployment-strategy.mdx) - Architectural decision record for continuous integration, delivery and deployment approach for the FlowMart e-commerce platform
- [API Management and Governance](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/drafts/03-api-management-governance.mdx) - Architectural decision record for our API management and governance approach for the FlowMart e-commerce platform
- [Service Mesh Adoption](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/examples/01-microservice-mesh-adoption.mdx) - Architectural decision record for adopting a service mesh for TechNova's cloud platform
- [Data Platform Strategy](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/examples/02-data-platform-strategy.mdx) - Architectural decision record for adopting a modern data platform at FinSecure
- [API Gateway Pattern Adoption](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/published/01-api-gateway-pattern.mdx) - Architectural decision record for implementing an API Gateway for the FlowMart e-commerce platform
- [Event-driven architecture adoption](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/published/02-eda-adoption.mdx) - A document that captures important architectural decisions and their context
- [Authentication and Authorization Strategy](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/published/03-auth-strategy.mdx) - Architectural decision record for implementing authentication and authorization for the FlowMart e-commerce platform
- [Database Strategy for Microservices](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/published/04-database-strategy.mdx) - Architectural decision record for database selection and data management in the FlowMart e-commerce platform
- [Frontend Architecture](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/published/05-frontend-architecture.mdx) - Architectural decision record for frontend architecture of the FlowMart e-commerce platform
- [Observability Strategy](https://demo.eventcatalog.dev/docs/custom/technical-architecture-design/architecture-decision-records/published/06-observability-strategy.mdx) - Architectural decision record for implementing observability in the FlowMart e-commerce platform