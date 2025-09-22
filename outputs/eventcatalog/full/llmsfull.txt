---
id: InventoryAdjusted
name: Inventory adjusted
version: 1.0.1
summary: |
  Indicates a change in inventory level
owners:
    - dboyne
    - msmith
    - asmith
    - full-stack
    - mobile-devs
channels:
  - id: inventory.{env}.events
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
    - content: Broker:Apache Kafka
      backgroundColor: yellow
      textColor: yellow
      icon: kafka
schemaPath: 'schema.avro'
draft: 
  title: "Inventory Adjusted 1.0.1 is in draft"
  message: |
    ### New version of Inventory Adjusted is in draft

    This is a new version of the Inventory Adjusted event. It is not yet ready for production. We are still working on it and collecting feedback from the team.

    You can use this version in lower environments, **but please be aware that it is still in draft and may change.**

    You can still use a previous version of the event, [Inventory Adjusted 1.0.0](/docs/events/InventoryAdjusted/1.0.0), until that version is deprecated.

    _If you would like to provide feedback, please contact us at [feedback@eventcatalog.io](mailto:feedback@eventcatalog.io) or our slack channel [Order Management](https://join.slack.com/t/eventcatalog/shared_invite/zt-1q900000000000000000000000000000)_

---

import Footer from '@catalog/components/footer.astro';

## Overview

The `Inventory Adjusted` event is triggered whenever there is a change in the inventory levels of a product. This could occur due to various reasons such as receiving new stock, sales, returns, or manual adjustments by the inventory management team. The event ensures that all parts of the system that rely on inventory data are kept up-to-date with the latest inventory levels.

<Tiles >
    <Tile icon="UserGroupIcon" href="/docs/teams/full-stack" title="Contact the team" description="Any questions? Feel free to contact the owners" />
    <Tile icon="DocumentIcon" href={`/generated/events/Inventory/${frontmatter.id}/schema.avro`} title="View the schema" description="View the schema directly in your browser" />
</Tiles>

## Architecture diagram

<NodeGraph />


<SchemaViewer file="schema.yml" title="JSON Schema" maxHeight="500" />

## Payload example

Event example you my see being published.

```json title="Payload example"
{
  "Name": "John Doe",
  "Age": 30,
  "Department": "Engineering",
  "Position": "Software Engineer",
  "Salary": 85000.50,
  "JoinDate": "2024-01-15"
}
```

## Schema (avro)

<Schema file="schema.avro" title="Inventory Adjusted Schema (avro)" />

## Producing the Event

Select the language you want to produce the event in to see an example.

<Tabs>
  <TabItem title="Python">

    ```python title="Produce event in Python" frame="terminal"
    from kafka import KafkaProducer
    import json
    from datetime import datetime

    # Kafka configuration
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Event data
    event_data = {
      "event_id": "abc123",
      "timestamp": datetime.utcnow().isoformat() + 'Z',
      "product_id": "prod987",
      "adjusted_quantity": 10,
      "new_quantity": 150,
      "adjustment_reason": "restock",
      "adjusted_by": "user123"
    }

    # Send event to Kafka topic
    producer.send('inventory.adjusted', event_data)
    producer.flush()
    ```
  </TabItem>
  <TabItem title="TypeScript">

    ```typescript title="Produce event in TypeScript" frame="terminal"
    import { Kafka } from 'kafkajs';

    // Kafka configuration
    const kafka = new Kafka({
      clientId: 'inventory-producer',
      brokers: ['localhost:9092']
    });

    const producer = kafka.producer();

    // Event data
    const eventData = {
      event_id: "abc123",
      timestamp: new Date().toISOString(),
      product_id: "prod987", 
      adjusted_quantity: 10,
      new_quantity: 150,
      adjustment_reason: "restock",
      adjusted_by: "user123"
    };

    // Send event to Kafka topic
    async function produceEvent() {
      await producer.connect();
      await producer.send({
        topic: 'inventory.adjusted',
        messages: [
          { value: JSON.stringify(eventData) }
        ],
      });
      await producer.disconnect();
    }

    produceEvent().catch(console.error);
    ```
  </TabItem>
  <TabItem title="Java">

    ```java title="Produce event in Java" frame="terminal"
    import org.apache.kafka.clients.producer.*;
    import org.apache.kafka.common.serialization.StringSerializer;
    import com.fasterxml.jackson.databind.ObjectMapper;
    import java.util.Properties;
    import java.util.HashMap;
    import java.util.Map;
    import java.time.Instant;

    public class InventoryProducer {
        public static void main(String[] args) {
            // Kafka configuration
            Properties props = new Properties();
            props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
            props.put(ProducerConfig.CLIENT_ID_CONFIG, "inventory-producer");
            props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
            props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

            Producer<String, String> producer = new KafkaProducer<>(props);
            ObjectMapper mapper = new ObjectMapper();

            try {
                // Event data
                Map<String, Object> eventData = new HashMap<>();
                eventData.put("event_id", "abc123");
                eventData.put("timestamp", Instant.now().toString());
                eventData.put("product_id", "prod987");
                eventData.put("adjusted_quantity", 10);
                eventData.put("new_quantity", 150);
                eventData.put("adjustment_reason", "restock");
                eventData.put("adjusted_by", "user123");

                // Create producer record
                ProducerRecord<String, String> record = new ProducerRecord<>(
                    "inventory.adjusted",
                    mapper.writeValueAsString(eventData)
                );

                // Send event to Kafka topic
                producer.send(record, (metadata, exception) -> {
                    if (exception != null) {
                        System.err.println("Error producing message: " + exception);
                    }
                });

            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                producer.flush();
                producer.close();
            }
        }
    }
    ```
  </TabItem>
</Tabs>



### Consuming the Event

To consume an Inventory Adjusted event, use the following example Kafka consumer configuration in Python:

```python title="Consuming the event with python" frame="terminal"
from kafka import KafkaConsumer
import json

# Kafka configuration
consumer = KafkaConsumer(
    'inventory.adjusted',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='inventory_group',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Consume events
for message in consumer:
    event_data = json.loads(message.value)
    print(f"Received Inventory Adjusted event: {event_data}")
```

<Footer />

 ## Raw Schema:schema.avro

{
  "type" : "record",
  "namespace" : "Tutorialspoint",
  "name" : "Employee",
  "fields" : [
     { "name" : "Name", "type" : "string" },
     { "name" : "Age", "type" : "int" },
     { "name" : "Department", "type" : "string" },
     { "name" : "Position", "type" : "string" },
     { "name" : "Salary", "type" : "double" },
     { "name" : "JoinDate", "type" : "string", "logicalType": "date" }
  ]
}

---
id: OutOfStock
name: Inventory out of stock
version: 0.0.4
summary: |
  Indicates inventory is out of stock
owners:
    - dboyne
    - msmith
    - asmith
    - full-stack
    - mobile-devs
channels:
  - id: inventory.{env}.events
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
    - content: Broker:Apache Kafka
      backgroundColor: yellow
      textColor: yellow
      icon: kafka
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `Inventory Adjusted` event is triggered whenever there is a change in the inventory levels of a product. This could occur due to various reasons such as receiving new stock, sales, returns, or manual adjustments by the inventory management team. The event ensures that all parts of the system that rely on inventory data are kept up-to-date with the latest inventory levels.

<NodeGraph />

### Payload
The payload of the `Inventory Adjusted` event includes the following fields:

```json title="Example of payload" frame="terminal"
{
  "event_id": "string",
  "timestamp": "ISO 8601 date-time",
  "product_id": "string",
  "adjusted_quantity": "integer",
  "new_quantity": "integer",
  "adjustment_reason": "string"
}
```

### Producing the Event

To produce an Inventory Adjusted event, use the following example Kafka producer configuration in Python:

```python title="Produce event in Python" frame="terminal"
from kafka import KafkaProducer
import json
from datetime import datetime

# Kafka configuration
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Event data
event_data = {
  "event_id": "abc123",
  "timestamp": datetime.utcnow().isoformat() + 'Z',
  "product_id": "prod987",
  "adjusted_quantity": 10,
  "new_quantity": 150,
  "adjustment_reason": "restock",
  "adjusted_by": "user123"
}

# Send event to Kafka topic
producer.send('inventory.adjusted', event_data)
producer.flush()
```

### Consuming the Event

To consume an Inventory Adjusted event, use the following example Kafka consumer configuration in Python:

```python title="Consuming the event with python" frame="terminal"
from kafka import KafkaConsumer
import json

# Kafka configuration
consumer = KafkaConsumer(
    'inventory.adjusted',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='inventory_group',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Consume events
for message in consumer:
    event_data = json.loads(message.value)
    print(f"Received Inventory Adjusted event: {event_data}")
```

<Footer />
---
id: OrderCancelled
name: Order cancelled
version: 0.0.1
summary: |
  Indicates an order has been canceled
owners:
    - order-management
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
    - content: Broker:Apache Kafka
      backgroundColor: yellow
      textColor: yellow
      icon: kafka
schemaPath: 'schema.json'
channels:
  - id: orders.{env}.events
---

import Footer from '@catalog/components/footer.astro';

## Overview

The OrderCancelled event is triggered whenever an existing order is cancelled. This event ensures that all relevant services are notified of the cancellation, allowing them to take appropriate actions such as updating inventory levels, refunding payments, and notifying the user. The event helps maintain consistency across the system by ensuring all dependent services are aware of the order cancellation.

## Example payload

```json title="Example payload"
{
  "orderId": "123e4567-e89b-12d3-a456-426614174000",
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "orderItems": [
    {
      "productId": "789e1234-b56c-78d9-e012-3456789fghij",
      "productName": "Example Product",
      "quantity": 2,
      "unitPrice": 29.99,
      "totalPrice": 59.98
    }
  ],
  "orderStatus": "cancelled",
  "totalAmount": 59.98,
  "cancellationReason": "Customer requested cancellation",
  "timestamp": "2024-07-04T14:48:00Z"
}

```

## Schema

JSON schema for the event.

<Schema title="JSON Schema" file="schema.json"/>

<Footer />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "OrderCancelledEvent",
    "type": "object",
    "properties": {
      "orderId": {
        "type": "string",
        "format": "uuid",
        "description": "The unique identifier of the order that was cancelled."
      },
      "userId": {
        "type": "string",
        "format": "uuid",
        "description": "The unique identifier of the user who placed the order."
      },
      "orderItems": {
        "type": "array",
        "description": "A list of items included in the cancelled order, each containing product details and quantities.",
        "items": {
          "type": "object",
          "properties": {
            "productId": {
              "type": "string",
              "format": "uuid",
              "description": "The unique identifier of the product."
            },
            "productName": {
              "type": "string",
              "description": "The name of the product."
            },
            "quantity": {
              "type": "integer",
              "description": "The quantity of the product ordered."
            },
            "unitPrice": {
              "type": "number",
              "format": "float",
              "description": "The price per unit of the product."
            },
            "totalPrice": {
              "type": "number",
              "format": "float",
              "description": "The total price for this order item (quantity * unit price)."
            }
          },
          "required": ["productId", "productName", "quantity", "unitPrice", "totalPrice"]
        }
      },
      "orderStatus": {
        "type": "string",
        "description": "The current status of the order after cancellation.",
        "enum": ["cancelled"]
      },
      "totalAmount": {
        "type": "number",
        "format": "float",
        "description": "The total amount of the order that was cancelled."
      },
      "cancellationReason": {
        "type": "string",
        "description": "The reason for the order cancellation, if provided."
      },
      "timestamp": {
        "type": "string",
        "format": "date-time",
        "description": "The date and time when the order was cancelled."
      }
    },
    "required": ["orderId", "userId", "orderItems", "orderStatus", "totalAmount", "timestamp"],
    "additionalProperties": false
  }
  
---
id: OrderConfirmed
name: Order confirmed
version: 0.0.1
summary: |
  Indicates an order has been confirmed
owners:
    - order-management
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
      icon: StarIcon
    - content: Broker:Apache Kafka
      backgroundColor: yellow
      textColor: yellow
      icon: kafka
schemaPath: schema.json
channels:
  - id: orders.{env}.events
draft: true
---

import Footer from '@catalog/components/footer.astro';

## Overview

The OrderConfirmed event is triggered when an order has been successfully confirmed. This event notifies relevant services that the order is ready for further processing, such as inventory adjustment, payment finalization, and preparation for shipping.

## Architecture Diagram

<NodeGraph />

## Payload

```json title="Example payload"
{
  "orderId": "123e4567-e89b-12d3-a456-426614174000",
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "orderItems": [
    {
      "productId": "789e1234-b56c-78d9-e012-3456789fghij",
      "productName": "Example Product",
      "quantity": 2,
      "unitPrice": 29.99,
      "totalPrice": 59.98
    }
  ],
  "orderStatus": "confirmed",
  "totalAmount": 150.75,
  "confirmationTimestamp": "2024-07-04T14:48:00Z"
}
```

## Schema

<Schema file="schema.json"/>

<Footer />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "OrderConfirmedEvent",
    "type": "object",
    "properties": {
      "orderId": {
        "type": "string",
        "format": "uuid",
        "description": "The unique identifier of the confirmed order."
      },
      "userId": {
        "type": "string",
        "format": "uuid",
        "description": "The unique identifier of the user who placed the order."
      },
      "orderItems": {
        "type": "array",
        "description": "A list of items included in the confirmed order, each containing product details and quantities.",
        "items": {
          "type": "object",
          "properties": {
            "productId": {
              "type": "string",
              "format": "uuid",
              "description": "The unique identifier of the product."
            },
            "productName": {
              "type": "string",
              "description": "The name of the product."
            },
            "quantity": {
              "type": "integer",
              "description": "The quantity of the product ordered."
            },
            "unitPrice": {
              "type": "number",
              "format": "float",
              "description": "The price per unit of the product."
            },
            "totalPrice": {
              "type": "number",
              "format": "float",
              "description": "The total price for this order item (quantity * unitPrice)."
            }
          },
          "required": ["productId", "productName", "quantity", "unitPrice", "totalPrice"]
        }
      },
      "orderStatus": {
        "type": "string",
        "description": "The current status of the order after confirmation."
      },
      "totalAmount": {
        "type": "number",
        "format": "float",
        "description": "The total amount of the confirmed order."
      },
      "confirmationTimestamp": {
        "type": "string",
        "format": "date-time",
        "description": "The date and time when the order was confirmed."
      }
    },
    "required": ["orderId", "userId", "orderItems", "orderStatus", "totalAmount", "confirmationTimestamp"],
    "additionalProperties": false
  }
  
---
id: OrderAmended
name: Order amended
version: 0.0.1
summary: |
  Indicates an order has been changed
owners:
    - order-management
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
    - content: Broker:Apache Kafka
      backgroundColor: yellow
      textColor: yellow
      icon: kafka
schemaPath: schema.avro
channels:
  - id: orders.{env}.events
    parameters:
      env: staging
draft: 
  title: "In draft awaiting feedback"
  message: |
    ### Use with caution, still in draft
    This event is still in draft. It is not yet ready for production. We are still working on it and collecting feedback from the team.
    If you would like to provide feedback, please contact us at [feedback@eventcatalog.io](mailto:feedback@eventcatalog.io) or our slack channel [Order Management](https://join.slack.com/t/eventcatalog/shared_invite/zt-1q900000000000000000000000000000).

    If you are looking for a similar event, you can still use the [OrderConfirmed](/docs/events/OrderConfirmed/0.0.1) event, until it is deprecated.

    If you want to use this event in lower environments, you can. We are looking for feedback on the event and how it is used in the team.

---

import Footer from '@catalog/components/footer.astro';

## Overview

The OrderAmended event is triggered whenever an existing order is modified. This event ensures that all relevant services are notified of changes to an order, such as updates to order items, quantities, shipping information, or status. The event allows the system to maintain consistency and ensure that all dependent services can react appropriately to the amendments.

<NodeGraph />

## Example payload

```json title="Example Payload"
{
  "orderId": "123e4567-e89b-12d3-a456-426614174000",
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "amendedItems": [
    {
      "productId": "789e1234-b56c-78d9-e012-3456789fghij",
      "productName": "Example Product",
      "oldQuantity": 2,
      "newQuantity": 3,
      "unitPrice": 29.99,
      "totalPrice": 89.97
    }
  ],
  "orderStatus": "confirmed",
  "totalAmount": 150.75,
  "timestamp": "2024-07-04T14:48:00Z"
}
```

## Schema (Avro)s

<Schema file="schema.avro" />

## Schema (JSON)

<Schema file="schema.json" />

<Footer />

 ## Raw Schema:schema.avro

{
  "type": "record",
  "name": "OrderAmendedEvent",
  "namespace": "com.example.events",
  "fields": [
    {
      "name": "orderId",
      "type": "string",
      "doc": "The unique identifier of the order that was amended."
    },
    {
      "name": "userId",
      "type": "string",
      "doc": "The unique identifier of the user who placed the order."
    },
    {
      "name": "amendedItems",
      "type": {
        "type": "array",
        "items": {
          "type": "record",
          "name": "AmendedItem",
          "fields": [
            {
              "name": "productId",
              "type": "string",
              "doc": "The unique identifier of the product."
            },
            {
              "name": "productName",
              "type": "string",
              "doc": "The name of the product."
            },
            {
              "name": "oldQuantity",
              "type": "int",
              "doc": "The original quantity of the product ordered."
            },
            {
              "name": "newQuantity",
              "type": "int",
              "doc": "The new quantity of the product ordered."
            },
            {
              "name": "unitPrice",
              "type": "double",
              "doc": "The price per unit of the product."
            },
            {
              "name": "totalPrice",
              "type": "double",
              "doc": "The total price for this order item (newQuantity * unitPrice)."
            }
          ]
        }
      },
      "doc": "A list of items that were amended in the order, each containing product details and updated quantities."
    },
    {
      "name": "orderStatus",
      "type": "string",
      "doc": "The current status of the order after the amendment."
    },
    {
      "name": "totalAmount",
      "type": "double",
      "doc": "The total amount of the order after the amendment."
    },
    {
      "name": "timestamp",
      "type": "string",
      "doc": "The date and time when the order was amended, in ISO 8601 format."
    }
  ]
}

---
id: DeliveryFailed
name: Delivery failed
version: 0.0.1
summary: |
  Event that is emitted when a shipment delivery fails.
owners:
    - dboyne
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `DeliveryFailed` event is emitted when a shipment delivery fails. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This event can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time shipment data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "DeliveryFailed",
    "description": "Schema for delivery failed event",
    "properties": {
        "shipmentId": {
            "type": "string",
            "description": "Unique identifier for the shipment"
        },
        "orderId": {
            "type": "string",
            "description": "Identifier for the associated order"
        }
    },
    "required": ["shipmentId", "orderId"]
}
---
id: ReturnInitiated
name: Return initiated
version: 0.0.1
summary: |
  Event that is emitted when a return is initiated.
owners:
    - dboyne
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `ReturnInitiated` event is emitted when a return is initiated. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This event can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time return data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "ReturnInitiated",
    "description": "Schema for return initiated event",
    "properties": {
        "shipmentId": {
            "type": "string",
            "description": "Unique identifier for the shipment"
        },
        "orderId": {
            "type": "string",
            "description": "Identifier for the associated order"
        }
    },
    "required": ["shipmentId", "orderId"]
}
---
id: ShipmentCreated
name: Shipment created
version: 0.0.1
summary: |
  Event that is emitted when a shipment is created.
owners:
    - dboyne
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `ShipmentCreated` event is emitted when a shipment is created. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This event can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time shipment data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "ShipmentCreated",
  "description": "Schema for shipment created event",
  "properties": {
    "shipmentId": {
      "type": "string",
      "description": "Unique identifier for the shipment"
    },
    "orderId": {
      "type": "string",
      "description": "Identifier for the associated order"
    },
    "address": {
      "type": "object",
      "properties": {
        "street": {
          "type": "string",
          "description": "Street address for the shipment"
        },
        "city": {
          "type": "string",
          "description": "City for the shipment"
        },
        "state": {
          "type": "string",
          "description": "State for the shipment"
        },
        "postalCode": {
          "type": "string",
          "description": "Postal code for the shipment"
        },
        "country": {
          "type": "string",
          "description": "Country for the shipment"
        }
      },
      "required": ["street", "city", "state", "postalCode", "country"]
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "itemId": {
            "type": "string",
            "description": "Identifier for the item"
          },
          "quantity": {
            "type": "integer",
            "description": "Quantity of the item"
          }
        },
        "required": ["itemId", "quantity"]
      }
    },
    "shippingMethod": {
      "type": "string",
      "description": "Method of shipping (e.g., standard, express)"
    }
  },
  "required": ["shipmentId", "orderId", "address", "items", "shippingMethod"]
}


---
id: ShipmentDelivered
name: Shipment delivered
version: 0.0.1
summary: |
  Event that is emitted when a shipment is delivered.
owners:
    - dboyne
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `ShipmentDelivered` event is emitted when a shipment is delivered. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This event can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time shipment data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "ShipmentDelivered",
    "description": "Schema for shipment delivered event",
    "properties": {
        "shipmentId": {
            "type": "string",
            "description": "Unique identifier for the shipment"
        },
        "orderId": {
            "type": "string",
            "description": "Identifier for the associated order"
        }
    },
    "required": ["shipmentId", "orderId"]
}
---
id: ShipmentDispatched
name: Shipment dispatched
version: 0.0.1
summary: |
  Event that is emitted when a shipment is dispatched.
owners:
    - dboyne
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `ShipmentDispatched` event is emitted when a shipment is dispatched. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This event can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time shipment data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "ShipmentDispatched",
    "description": "Schema for shipment dispatched event",
    "properties": {
        "shipmentId": {
            "type": "string",
            "description": "Unique identifier for the shipment"
        },
        "orderId": {
            "type": "string",
            "description": "Identifier for the associated order"
        }
    },
    "required": ["shipmentId", "orderId"]
}
---
id: ShipmentInTransit
name: Shipment in transit
version: 0.0.1
summary: |
  Event that is emitted when a shipment is in transit.
owners:
    - dboyne
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `ShipmentInTransit` event is emitted when a shipment is in transit. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This event can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time shipment data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "ShipmentInTransit",
    "description": "Schema for shipment in transit event",
    "properties": {
        "shipmentId": {
            "type": "string",
            "description": "Unique identifier for the shipment"
        },
        "orderId": {
            "type": "string",
            "description": "Identifier for the associated order"
        }
    },
    "required": ["shipmentId", "orderId"]
}
---
id: FraudCheckCompleted
version: 0.0.1
name: Fraud Check Completed
summary: Emitted when a fraud check has been completed for a transaction
tags:
  - payment
  - fraud
  - security
badges:
  - content: New
    backgroundColor: green
    textColor: white
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro'

## Overview

The `FraudCheckCompleted` event is emitted when the fraud detection service has completed its analysis of a payment transaction. This event contains the risk assessment results and recommendations.

## Schema

<SchemaViewer title="FraudCheckCompleted Schema" schemaPath="schema.json" />

## Event Details

- **Risk Score**: A numerical score from 0-100 indicating fraud risk
- **Decision**: APPROVED, DECLINED, or MANUAL_REVIEW
- **Reasons**: Array of reasons for the decision
- **Confidence**: Confidence level of the fraud detection

## Example Payload

```json
{
  "transactionId": "txn_1234567890",
  "paymentId": "pay_9876543210",
  "riskScore": 25,
  "decision": "APPROVED",
  "reasons": ["Low risk merchant", "Customer history positive"],
  "confidence": 0.92,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

<Footer />

 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "transactionId": {
      "type": "string",
      "description": "Unique identifier for the transaction"
    },
    "paymentId": {
      "type": "string",
      "description": "Unique identifier for the payment"
    },
    "riskScore": {
      "type": "number",
      "minimum": 0,
      "maximum": 100,
      "description": "Risk score from 0-100"
    },
    "decision": {
      "type": "string",
      "enum": ["APPROVED", "DECLINED", "MANUAL_REVIEW"],
      "description": "Fraud check decision"
    },
    "reasons": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Reasons for the decision"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "description": "Confidence level of the decision"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "When the fraud check was completed"
    }
  },
  "required": ["transactionId", "paymentId", "riskScore", "decision", "timestamp"]
}
---
id: FraudDetected
version: 0.0.1
name: Fraud Detected
summary: Emitted when a fraud is detected in a transaction
tags:
  - payment
  - fraud
  - security
badges:
  - content: New
    backgroundColor: green
    textColor: white
---

import Footer from '@catalog/components/footer.astro'

## Overview

The `FraudDetected` event is emitted when the fraud detection service identifies a potential fraud in a payment transaction. This event contains the details of the detected fraud.

## Event Details

- **Fraud Type**: Type of fraud detected
- **Severity**: LOW, MEDIUM, or HIGH
- **Indicators**: Array of indicators that led to the detection
- **Confidence**: Confidence level of the fraud detection

## Example Payload

```json
{
  "transactionId": "txn_1234567890",
  "paymentId": "pay_9876543210",
  "fraudType": "Stolen Card",
  "severity": "HIGH",
  "indicators": ["Unusual location", "High transaction amount"],
  "confidence": 0.95,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

<Footer />
---
id: RiskScoreCalculated
version: 0.0.1
name: Risk Score Calculated
summary: Emitted when a risk score is calculated for a transaction
tags:
  - payment
  - fraud
  - security
badges:
  - content: New
    backgroundColor: green
    textColor: white
---

import Footer from '@catalog/components/footer.astro'

## Overview

The `RiskScoreCalculated` event is emitted when the fraud detection service calculates a risk score for a payment transaction. This event contains the details of the calculated risk score.

## Event Details

- **Risk Score**: Calculated risk score for the transaction
- **Severity**: LOW, MEDIUM, or HIGH
- **Indicators**: Array of indicators used in the calculation
- **Confidence**: Confidence level of the risk score calculation

## Example Payload

```json
{
  "transactionId": "txn_1234567890",
  "paymentId": "pay_9876543210",
  "riskScore": 85,
  "severity": "MEDIUM",
  "indicators": ["Unusual location", "High transaction amount"],
  "confidence": 0.85,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

<Footer />
---
id: PaymentFailed
version: 0.0.1
name: Payment Failed
summary: Emitted when a payment attempt fails
badges:
  - content: Error Event
    backgroundColor: red
    textColor: white
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro'

## Overview

The `PaymentFailed` event is emitted when a payment attempt fails for any reason. This event is consumed by various services to handle payment failures appropriately.

## Consumers

This event is consumed by:
- **BillingService** (Subscriptions Domain) - To handle subscription payment failures
- **OrdersService** (Orders Domain) - To handle order payment failures
- **NotificationService** (Orders Domain) - To notify customers of payment failures

## Failure Reasons

Common failure reasons include:
- **insufficient_funds** - Card has insufficient funds
- **card_declined** - Card was declined by issuer
- **expired_card** - Card has expired
- **fraud_suspected** - Payment flagged as potentially fraudulent
- **network_error** - Payment gateway network error
- **invalid_payment_method** - Payment method is invalid

## Schema

<SchemaViewer title="PaymentFailed Schema" schemaPath="schema.json" />

## Example Payload

```json
{
  "paymentId": "pay_123456",
  "amount": 49.99,
  "currency": "USD",
  "failureReason": "insufficient_funds",
  "failureMessage": "Your card has insufficient funds",
  "metadata": {
    "subscriptionId": "sub_ABC123",
    "invoiceId": "inv_123456",
    "customerId": "cust_XYZ789"
  },
  "canRetry": true,
  "nextRetryAt": "2024-02-02T00:00:00Z",
  "timestamp": "2024-02-01T10:30:00Z"
}
```

<Footer />

 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "paymentId": {
      "type": "string",
      "description": "Unique identifier for the failed payment"
    },
    "amount": {
      "type": "number",
      "description": "Payment amount that failed"
    },
    "currency": {
      "type": "string",
      "description": "Currency code (ISO 4217)"
    },
    "failureReason": {
      "type": "string",
      "enum": [
        "insufficient_funds",
        "card_declined",
        "expired_card",
        "fraud_suspected",
        "network_error",
        "invalid_payment_method",
        "authentication_required",
        "other"
      ],
      "description": "Reason for payment failure"
    },
    "failureMessage": {
      "type": "string",
      "description": "Human-readable failure message"
    },
    "metadata": {
      "type": "object",
      "properties": {
        "subscriptionId": {
          "type": "string"
        },
        "invoiceId": {
          "type": "string"
        },
        "customerId": {
          "type": "string"
        },
        "orderId": {
          "type": "string"
        }
      }
    },
    "canRetry": {
      "type": "boolean",
      "description": "Whether this payment can be retried"
    },
    "nextRetryAt": {
      "type": "string",
      "format": "date-time",
      "description": "Suggested time for next retry attempt"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "When the failure occurred"
    }
  },
  "required": ["paymentId", "amount", "currency", "failureReason", "timestamp"]
}
---
id: PaymentComplete
name: Payment Complete
version: 0.0.2
summary: Event is triggered when a user completes a payment through the Payment Service
owners:
    - dboyne
channels:
  - id: payments.{env}.events
    parameters:
      env: staging
---

import Footer from '@catalog/components/footer.astro';

## Overview

The Payment Complete event is triggered when a user successfully completes a payment through the Payment Service. This event signifies the end of the payment process and confirms that the payment has been processed successfully.

<NodeGraph />

### Payload Example

```json title="Payload example"
{
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "orderId": "789e1234-b56c-78d9-e012-3456789fghij",
  "amount": 100.50,
  "paymentMethod": "CreditCard",
  "timestamp": "2024-07-04T14:48:00Z",
  "status": "Completed"
}
```

### Security Considerations

- **Authentication**: Ensure that only authenticated users can complete a payment, and the userId in the payload matches the authenticated user.
- **Data Validation**: Validate all input data to prevent injection attacks or other malicious input.
- **Sensitive Data Handling**: Avoid including sensitive information (e.g., credit card numbers) in the event payload. Use secure channels and encryption for such data.

<Footer />
---
id: PaymentInitiated
name: Payment Initiated
version: 0.0.1
summary: Event is triggered when a user initiates a payment through the Payment Service
owners:
    - dboyne
channels:
  - id: payments.{env}.events
    parameters:
      env: staging
---

import Footer from '@catalog/components/footer.astro';

## Overview

The Payment Initiated event is triggered when a user initiates a payment through the Payment Service. This event signifies the beginning of the payment process and contains all necessary information to process the payment.

<NodeGraph />

### Payload Example

```json title="Payload example"
{
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "orderId": "789e1234-b56c-78d9-e012-3456789fghij",
  "amount": 100.50,
  "paymentMethod": "CreditCard",
  "timestamp": "2024-07-04T14:48:00Z"
}
```

### Security Considerations

- **Authentication**: Ensure that only authenticated users can initiate a payment, and the userId in the payload matches the authenticated user.
- **Data Validation**: Validate all input data to prevent injection attacks or other malicious input.
- **Sensitive Data Handling**: Avoid including sensitive information (e.g., credit card numbers) in the event payload. Use secure channels and encryption for such data.

<Footer />
---
id: PaymentProcessed
name: Payment Processed
version: 1.0.0
summary: Event is triggered after the payment has been successfully processed
owners:
    - dboyne
channels:
  - id: payments.{env}.events
    parameters:
      env: staging
---

import Footer from '@catalog/components/footer.astro';

## Overview

The PaymentProcessed event is triggered after the payment has been successfully processed by the Payment Service. This event signifies that a payment has been confirmed, and it communicates the outcome to other services and components within the system.

<NodeGraph />

### Payload Example

```json title="Payload example"
{
  "transactionId": "123e4567-e89b-12d3-a456-426614174000",
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "orderId": "789e1234-b56c-78d9-e012-3456789fghij",
  "amount": 100.50,
  "paymentMethod": "CreditCard",
  "status": "confirmed",
  "confirmationDetails": {
    "gatewayResponse": "Approved",
    "transactionId": "abc123"
  },
  "timestamp": "2024-07-04T14:48:00Z"
}
```

### Security Considerations

- **Data Validation**: Ensure that all data in the event payload is validated before publishing to prevent injection attacks or other malicious activities.
- **Sensitive Data Handling**: Avoid including sensitive information (e.g., full credit card numbers) in the event payload. Use secure channels and encryption for such data.
- **Authentication and Authorization**: Ensure that only authorized services can publish or consume PaymentProcessed events.

<Footer />
---
id: SubscriptionPaymentDue
version: 0.0.1
name: Subscription Payment Due
summary: Emitted when a subscription payment is due for collection
tags:
  - billing
  - payment
  - cross-domain
badges:
  - content: Cross-Domain
    backgroundColor: purple
    textColor: white
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro'

## Overview

The `SubscriptionPaymentDue` event is emitted by the Billing Service when a subscription's billing cycle is due for payment. This event triggers the payment collection process in the Payment domain.

## Cross-Domain Communication

This event facilitates communication between:
- **Source**: Subscriptions Domain (BillingService)
- **Target**: Payment Domain (PaymentService, FraudDetectionService)

## Schema

<SchemaViewer title="SubscriptionPaymentDue Schema" schemaPath={frontmatter.schemaPath} />

## Event Flow

1. BillingService calculates when payment is due
2. Emits `SubscriptionPaymentDue` event
3. PaymentService receives and initiates payment
4. FraudDetectionService performs risk assessment
5. Payment is processed through PaymentGatewayService

## Example Payload

```json
{
  "subscriptionId": "sub_ABC123",
  "customerId": "cust_XYZ789",
  "invoiceId": "inv_123456",
  "amount": 49.99,
  "currency": "USD",
  "dueDate": "2024-02-01T00:00:00Z",
  "billingPeriod": {
    "start": "2024-02-01",
    "end": "2024-02-29"
  },
  "planId": "pro-monthly",
  "retryAttempt": 0
}
```

<Footer />

 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "subscriptionId": {
      "type": "string",
      "description": "Unique identifier for the subscription"
    },
    "customerId": {
      "type": "string",
      "description": "Unique identifier for the customer"
    },
    "invoiceId": {
      "type": "string",
      "description": "Unique identifier for the invoice"
    },
    "amount": {
      "type": "number",
      "description": "Amount due for payment"
    },
    "currency": {
      "type": "string",
      "description": "Currency code (ISO 4217)"
    },
    "dueDate": {
      "type": "string",
      "format": "date-time",
      "description": "When the payment is due"
    },
    "billingPeriod": {
      "type": "object",
      "properties": {
        "start": {
          "type": "string",
          "format": "date"
        },
        "end": {
          "type": "string",
          "format": "date"
        }
      },
      "required": ["start", "end"]
    },
    "planId": {
      "type": "string",
      "description": "Subscription plan identifier"
    },
    "retryAttempt": {
      "type": "integer",
      "description": "Number of retry attempts for failed payments"
    }
  },
  "required": ["subscriptionId", "customerId", "invoiceId", "amount", "currency", "dueDate"]
}
---
id: UserSubscriptionCancelled
name: User subscription cancelled
version: 0.0.1
summary: |
  An event that is triggered when a users subscription has been cancelled
owners:
    - subscriptions-management
badges:
    - content: New!
      backgroundColor: green
      textColor: green
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `UserSubscriptionCancelled` event is triggered when a users subscription has been cancelled.

## Architecture diagram

<NodeGraph />

<Footer />
---
id: UserSubscriptionStarted
name: User subscription started
version: 0.0.1
summary: |
  An event that is triggered when a new user subscription has started
owners:
    - subscriptions-management
badges:
    - content: New!
      backgroundColor: green
      textColor: green
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `UserSubscriptionStarted` event is triggered when a user starts a new subscription with our service.

## Architecture diagram

<NodeGraph />

<Footer />
---
id: InventoryAdjusted
name: Inventory adjusted
version: 0.0.1
summary: |
  Indicates a change in inventory level
owners:
    - dboyne
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
---

:::warning
When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.
:::

### Details

<NodeGraph />

---
id: InventoryAdjusted
name: Inventory adjusted
version: 1.0.0
summary: |
  Indicates a change in inventory level
owners:
    - dboyne
    - msmith
    - asmith
    - full-stack
    - mobile-devs
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
    - content: Broker:Apache Kafka
      backgroundColor: yellow
      textColor: yellow
      icon: kafka
---

## Overview

The `Inventory Adjusted` event is triggered whenever there is a change in the inventory levels of a product. This could occur due to various reasons such as receiving new stock, sales, returns, or manual adjustments by the inventory management team. The event ensures that all parts of the system that rely on inventory data are kept up-to-date with the latest inventory levels.

<NodeGraph />

## Event Details

### Event Name
`inventory.adjusted`

### Description
This event indicates that the inventory count for one or more products has been adjusted. The event carries the updated inventory details including the product ID, the new quantity, and the reason for the adjustment.

### Payload
The payload of the `Inventory Adjusted` event includes the following fields:

```json title="Example of payload" frame="terminal"
{
  "event_id": "string",
  "timestamp": "ISO 8601 date-time",
  "product_id": "string",
  "adjusted_quantity": "integer",
  "new_quantity": "integer",
  "adjustment_reason": "string",
  "adjusted_by": "string"
}
```

### Producing the Event

To produce an Inventory Adjusted event, use the following example Kafka producer configuration in Python:

```python title="Produce event in Python" frame="terminal"
from kafka import KafkaProducer
import json
from datetime import datetime

# Kafka configuration
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Event data
event_data = {
  "event_id": "abc123",
  "timestamp": datetime.utcnow().isoformat() + 'Z',
  "product_id": "prod987",
  "adjusted_quantity": 10,
  "new_quantity": 150,
  "adjustment_reason": "restock",
  "adjusted_by": "user123"
}

# Send event to Kafka topic
producer.send('inventory.adjusted', event_data)
producer.flush()
```

### Consuming the Event

To consume an Inventory Adjusted event, use the following example Kafka consumer configuration in Python:

```python title="Consuming the event with python" frame="terminal"
from kafka import KafkaConsumer
import json

# Kafka configuration
consumer = KafkaConsumer(
    'inventory.adjusted',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='inventory_group',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Consume events
for message in consumer:
    event_data = json.loads(message.value)
    print(f"Received Inventory Adjusted event: {event_data}")
```
---
id: OutOfStock
name: Inventory out of stock
version: 0.0.1
summary: |
  Indicates inventory is out of stock
owners:
    - dboyne
    - msmith
    - asmith
    - full-stack
    - mobile-devs
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
    - content: Broker:Apache Kafka
      backgroundColor: yellow
      textColor: yellow
      icon: kafka
---

## Overview

The `Inventory Adjusted` event is triggered whenever there is a change in the inventory levels of a product. This could occur due to various reasons such as receiving new stock, sales, returns, or manual adjustments by the inventory management team. The event ensures that all parts of the system that rely on inventory data are kept up-to-date with the latest inventory levels.

<NodeGraph />

### Payload
The payload of the `Inventory Adjusted` event includes the following fields:

```json title="Example of payload" frame="terminal"
{
  "event_id": "string",
  "timestamp": "ISO 8601 date-time",
  "product_id": "string",
  "adjusted_quantity": "integer",
  "new_quantity": "integer",
  "adjustment_reason": "string",
  "adjusted_by": "string"
}
```

### Producing the Event

To produce an Inventory Adjusted event, use the following example Kafka producer configuration in Python:

```python title="Produce event in Python" frame="terminal"
from kafka import KafkaProducer
import json
from datetime import datetime

# Kafka configuration
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Event data
event_data = {
  "event_id": "abc123",
  "timestamp": datetime.utcnow().isoformat() + 'Z',
  "product_id": "prod987",
  "adjusted_quantity": 10,
  "new_quantity": 150,
  "adjustment_reason": "restock",
  "adjusted_by": "user123"
}

# Send event to Kafka topic
producer.send('inventory.adjusted', event_data)
producer.flush()
```

### Consuming the Event

To consume an Inventory Adjusted event, use the following example Kafka consumer configuration in Python:

```python title="Consuming the event with python" frame="terminal"
from kafka import KafkaConsumer
import json

# Kafka configuration
consumer = KafkaConsumer(
    'inventory.adjusted',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='inventory_group',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Consume events
for message in consumer:
    event_data = json.loads(message.value)
    print(f"Received Inventory Adjusted event: {event_data}")
```
---
id: PaymentProcessed
name: Payment Processed
version: 0.0.1
summary: Event is triggered after the payment has been successfully processed
owners:
    - dboyne
---

import Footer from '@catalog/components/footer.astro';

## Overview

The PaymentProcessed event is triggered after the payment has been successfully processed by the Payment Service. This event signifies that a payment has been confirmed, and it communicates the outcome to other services and components within the system.

<NodeGraph />

### Payload Example

```json title="Payload example"
{
  "transactionId": "123e4567-e89b-12d3-a456-426614174000",
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "orderId": "789e1234-b56c-78d9-e012-3456789fghij",
  "amount": 100.50,
  "paymentMethod": "CreditCard",
  "status": "confirmed",
  "confirmationDetails": {
    "gatewayResponse": "Approved",
    "transactionId": "abc123"
  },
  "timestamp": "2024-07-04T14:48:00Z"
}
```

### Security Considerations

- **Data Validation**: Ensure that all data in the event payload is validated before publishing to prevent injection attacks or other malicious activities.
- **Sensitive Data Handling**: Avoid including sensitive information (e.g., full credit card numbers) in the event payload. Use secure channels and encryption for such data.
- **Authentication and Authorization**: Ensure that only authorized services can publish or consume PaymentProcessed events.

<Footer />
---
id: DeleteInventory
name: Delete Inventory
version: 0.0.3
summary: |
  Command that will delete a given inventory item from the system
owners:
    - dboyne
    - msmith
    - asmith
    - full-stack
    - mobile-devs
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
channels:
  - id: inventory.{env}.events
    parameters:
      env: staging
schemaPath: "schema.json"
sidebar:
  badge: 'DELETE'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The DeleteInventory command is issued to remove a product from the inventory system. This command is used by the inventory management system when a product needs to be completely removed from the warehouse or store catalog, typically due to discontinuation or permanent removal of the item.

## Architecture diagram

<NodeGraph />

<Footer />
---
id: UpdateInventory
name: Update inventory
version: 0.0.3
summary: |
  Command that will update a given inventory item
owners:
    - dboyne
    - msmith
    - asmith
    - full-stack
    - mobile-devs
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
channels:
  - id: inventory.{env}.events
    parameters:
      env: staging
schemaPath: "schema.json"
sidebar:
  badge: 'PUT'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The UpdateInventory command is issued to update the existing stock levels of a product in the inventory. This command is used by the inventory management system to adjust the quantity of products available in the warehouse or store, either by increasing or decreasing the current stock levels.

## Architecture diagram

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

## Payload example

```json title="Payload example"
{
  "productId": "789e1234-b56c-78d9-e012-3456789fghij",
  "quantityChange": -10,
  "warehouseId": "456e7891-c23d-45f6-b78a-123456789abc",
  "timestamp": "2024-07-04T14:48:00Z"
}
```

## Schema (JSON schema)

<Schema file="schema.json"/>

<Footer />

 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "UpdateInventoryCommand",
  "type": "object",
  "properties": {
    "productId": {
      "type": "string",
      "format": "uuid",
      "description": "The unique identifier of the product whose inventory is being updated."
    },
    "quantityChange": {
      "type": "integer",
      "description": "The change in quantity of the product in the inventory. Positive values indicate an increase, while negative values indicate a decrease."
    },
    "warehouseId": {
      "type": "string",
      "format": "uuid",
      "description": "The unique identifier of the warehouse where the inventory is being updated."
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "The date and time when the inventory update occurred."
    }
  },
  "required": ["productId", "quantityChange", "warehouseId", "timestamp"],
  "additionalProperties": false
}

---
id: AddInventory
name: Add inventory
version: 0.0.3
summary: |
  Command that will add item to a given inventory id
owners:
    - dboyne
    - asmith
    - full-stack
    - mobile-devs
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
channels:
  - id: inventory.{env}.events
    parameters:
      env: staging
schemaPath: 'schema.json'
sidebar:
  badge: 'POST'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The AddInventory command is issued to add new stock to the inventory. This command is used by the inventory management system to update the quantity of products available in the warehouse or store.

## Architecture diagram

<NodeGraph/>

## Payload example

```json title="Payload example"
{
  "productId": "789e1234-b56c-78d9-e012-3456789fghij",
  "quantity": 50,
  "warehouseId": "456e7891-c23d-45f6-b78a-123456789abc",
  "timestamp": "2024-07-04T14:48:00Z"
}

```

## Schema

<Schema file="schema.json"/>

<Footer />




 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "AddInventoryCommand",
    "type": "object",
    "properties": {
      "productId": {
        "type": "string",
        "format": "uuid",
        "description": "The unique identifier of the product being added to the inventory."
      },
      "quantity": {
        "type": "integer",
        "description": "The quantity of the product being added to the inventory."
      },
      "warehouseId": {
        "type": "string",
        "format": "uuid",
        "description": "The unique identifier of the warehouse where the inventory is being added."
      },
      "timestamp": {
        "type": "string",
        "format": "date-time",
        "description": "The date and time when the inventory was added."
      }
    },
    "required": ["productId", "quantity", "warehouseId", "timestamp"],
    "additionalProperties": false
  }
  
---
id: PlaceOrder
name: Place Order
version: 0.0.1
summary: |
  Command that will place an order
owners:
    - dboyne
    - msmith
    - asmith
    - full-stack
    - mobile-devs
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
schemaPath: 'schema.json'
sidebar:
  badge: 'POST'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The Order Placement Command is a versatile and robust system designed to streamline the process of placing an order. This command takes care of all the essential details needed to complete a purchase, ensuring a smooth and efficient transaction from start to finish.

## Architecture diagram

<NodeGraph/>

## Schema

<SchemaViewer file="schema.json"/>

<Footer />




 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Order",
  "description": "A schema representing an order placed by a customer",
  "type": "object",
  "properties": {
    "orderId": {
      "description": "Unique identifier for the order",
      "type": "string"
    },
    "customer": {
      "description": "Information about the customer placing the order",
      "type": "object",
      "properties": {
        "customerId": {
          "description": "Unique identifier for the customer",
          "type": "string"
        },
        "name": {
          "description": "Name of the customer",
          "type": "string"
        },
        "email": {
          "description": "Email address of the customer",
          "type": "string",
          "format": "email"
        },
        "phone": {
          "description": "Phone number of the customer",
          "type": "string",
          "pattern": "^[+]?[0-9]{10,15}$"
        }
      },
      "required": ["customerId", "name", "email"]
    },
    "items": {
      "description": "List of items in the order",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "itemId": {
            "description": "Unique identifier for the item",
            "type": "string"
          },
          "name": {
            "description": "Name of the item",
            "type": "string"
          },
          "quantity": {
            "description": "Quantity of the item ordered",
            "type": "integer",
            "minimum": 1
          },
          "price": {
            "description": "Price per unit of the item",
            "type": "number",
            "minimum": 0
          }
        },
        "required": ["itemId", "name", "quantity", "price"]
      }
    },
    "shippingAddress": {
      "description": "Address where the order will be shipped",
      "type": "object",
      "properties": {
        "street": {
          "description": "Street address",
          "type": "string"
        },
        "city": {
          "description": "City",
          "type": "string"
        },
        "state": {
          "description": "State or province",
          "type": "string"
        },
        "zip": {
          "description": "ZIP or postal code",
          "type": "string"
        },
        "country": {
          "description": "Country",
          "type": "string"
        }
      },
      "required": ["street", "city", "state", "zip", "country"]
    },
    "payment": {
      "description": "Payment information for the order",
      "type": "object",
      "properties": {
        "paymentMethod": {
          "description": "Payment method used",
          "type": "string",
          "enum": ["Credit Card", "PayPal", "Bank Transfer"]
        },
        "transactionId": {
          "description": "Transaction ID for the payment",
          "type": "string"
        },
        "amount": {
          "description": "Total amount paid",
          "type": "number",
          "minimum": 0
        }
      },
      "required": ["paymentMethod", "transactionId", "amount"]
    },
    "orderDate": {
      "description": "Date when the order was placed",
      "type": "string",
      "format": "date-time"
    },
    "status": {
      "description": "Current status of the order",
      "type": "string",
      "enum": ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]
    }
  },
  "required": ["orderId", "customer", "items", "shippingAddress", "payment", "orderDate", "status"]
}

---
id: CancelShipment
name: Cancel shipment
version: 0.0.1
summary: |
  POST request that will cancel a shipment, identified by its shipmentId.
owners:
    - dboyne
schemaPath: schema.json
sidebar:
  badge: 'POST'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `CancelShipment` message is a command used to cancel a shipment, identified by its `shipmentId`. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This command can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time shipment data for tracking, auditing, or managing customer purchases.

<SchemaViewer file="schema.json" title="Schema" maxHeight="500" />

<NodeGraph />



 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "CancelShipment",
    "description": "Schema for cancelling a shipment",
    "properties": {
        "shipmentId": {
            "type": "string",
            "description": "Unique identifier for the shipment"
        }
    },
    "required": ["shipmentId"]
}
---
id: CreateReturnLabel
name: Create return label
version: 0.0.1
summary: |
  POST request that will create a return label for a specific shipment, identified by its shipmentId.
owners:
    - dboyne
schemaPath: schema.json
sidebar:
  badge: 'POST'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `CreateReturnLabel` message is a command used to create a return label for a specific shipment, identified by its `shipmentId`. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This command can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time shipment data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "CreateReturnLabel",
    "description": "Schema for creating a return shipping label",
    "properties": {
        "CreateReturnLabel": {
            "type": "object",
            "properties": {
                "shipmentId": {
                    "type": "string",
                    "description": "Unique identifier for the shipment"
                }
            },
            "required": ["shipmentId"]
        }
    },
    "required": ["CreateReturnLabel"]
}
---
id: CreateShipment
name: Create shipment
version: 0.0.1
summary: |
  POST request that will create a shipment for a specific order, identified by its orderId.
owners:
    - dboyne
schemaPath: schema.json
sidebar:
  badge: 'POST'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `CreateShipment` message is a command used to create a shipment for a specific order, identified by its `orderId`. It provides information such as the order status (e.g., pending, completed, shipped), the items within the order, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This command can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time order data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "shipmentId": {
      "type": "string",
      "description": "Unique identifier for the shipment"
    },
    "orderId": {
      "type": "string",
      "description": "Identifier for the associated order"
    },
    "address": {
      "type": "object",
      "properties": {
        "street": {
          "type": "string",
          "description": "Street address for the shipment"
        },
        "city": {
          "type": "string",
          "description": "City for the shipment"
        },
        "state": {
          "type": "string",
          "description": "State for the shipment"
        },
        "postalCode": {
          "type": "string",
          "description": "Postal code for the shipment"
        },
        "country": {
          "type": "string",
          "description": "Country for the shipment"
        }
      },
      "required": ["street", "city", "state", "postalCode", "country"]
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "itemId": {
            "type": "string",
            "description": "Identifier for the item"
          },
          "quantity": {
            "type": "integer",
            "description": "Quantity of the item"
          }
        },
        "required": ["itemId", "quantity"]
      }
    },
    "shippingMethod": {
      "type": "string",
      "description": "Method of shipping (e.g., standard, express)"
    }
  },
  "required": ["shipmentId", "orderId", "address", "items", "shippingMethod"]
}

---
id: UpdateShipmentStatus
name: Update shipment status
version: 0.0.1
summary: |
  POST request that will update the status of a shipment, identified by its shipmentId.
owners:
    - dboyne
schemaPath: schema.json
sidebar:
  badge: 'POST'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `UpdateShipmentStatus` message is a command used to update the status of a shipment, identified by its `shipmentId`. It provides information such as the shipment status (e.g., pending, completed, shipped), the items within the shipment, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This command can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time shipment data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "UpdateShipmentStatus",
    "description": "Schema for updating a shipment's status",
    "properties": {
        "UpdateShipmentStatus": {
            "type": "object",
            "properties": {
                "shipmentId": {
                    "type": "string",
                    "description": "Unique identifier for the shipment"
                },
                "status": {
                    "type": "string",
                    "enum": ["pending", "shipped", "delivered", "returned"],
                    "description": "Current status of the shipment"
                },
                "updatedAt": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Timestamp when the status was last updated"
                }
            },
            "required": ["shipmentId", "status"]
        }
    },
    "required": ["UpdateShipmentStatus"]
}

---
id: ProcessPayment
version: 0.0.1
name: Process Payment
summary: Command to process a payment through the payment gateway
tags:
  - payment
  - command
  - cross-domain
badges:
  - content: Command
    backgroundColor: blue
    textColor: white
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro'

## Overview

The `ProcessPayment` command is used to initiate payment processing through the payment gateway. This command can be triggered by various sources including the Billing Service for subscription payments.

## Command Sources

This command can be triggered by:
- **BillingService** (Subscriptions Domain) - For recurring subscription payments
- **OrdersService** (Orders Domain) - For one-time order payments
- **PaymentService** (Payment Domain) - For payment retries

## Command Flow

```mermaid
sequenceDiagram
    participant BS as BillingService
    participant PGS as PaymentGatewayService
    participant FDS as FraudDetectionService
    participant EXT as External Gateway
    
    BS->>PGS: ProcessPayment
    PGS->>FDS: Check Fraud
    FDS-->>PGS: Risk Assessment
    PGS->>EXT: Process Payment
    EXT-->>PGS: Payment Result
    PGS-->>BS: PaymentProcessed/Failed
```

## Schema

<SchemaViewer title="ProcessPayment Schema" schemaPath={frontmatter.schemaPath} />

## Example Request

```json
{
  "paymentId": "pay_123456",
  "amount": 49.99,
  "currency": "USD",
  "paymentMethod": {
    "type": "card",
    "token": "tok_visa_4242"
  },
  "metadata": {
    "subscriptionId": "sub_ABC123",
    "invoiceId": "inv_123456",
    "customerId": "cust_XYZ789"
  },
  "idempotencyKey": "sub_ABC123_2024_02",
  "captureImmediately": true
}
```

<Footer />

 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "paymentId": {
      "type": "string",
      "description": "Unique identifier for this payment"
    },
    "amount": {
      "type": "number",
      "description": "Payment amount"
    },
    "currency": {
      "type": "string",
      "description": "Currency code (ISO 4217)"
    },
    "paymentMethod": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": ["card", "bank_transfer", "paypal", "digital_wallet"]
        },
        "token": {
          "type": "string",
          "description": "Payment method token"
        }
      },
      "required": ["type", "token"]
    },
    "metadata": {
      "type": "object",
      "properties": {
        "subscriptionId": {
          "type": "string"
        },
        "invoiceId": {
          "type": "string"
        },
        "customerId": {
          "type": "string"
        },
        "orderId": {
          "type": "string"
        }
      }
    },
    "idempotencyKey": {
      "type": "string",
      "description": "Key to prevent duplicate payments"
    },
    "captureImmediately": {
      "type": "boolean",
      "description": "Whether to capture payment immediately or just authorize"
    }
  },
  "required": ["paymentId", "amount", "currency", "paymentMethod", "idempotencyKey"]
}
---
id: CancelSubscription
name: Cancel subscription
version: 0.0.1
summary: |
  Command that will try and cancel a users subscription
owners:
    - subscriptions-management
badges:
    - content: New!
      backgroundColor: green
      textColor: green
sidebar:
  badge: 'POST'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `CancelSubscription` command will try and cancel a subscription for the user.

## Architecture diagram

<NodeGraph />

<Footer />
---
id: SubscribeUser
name: Subscribe user
version: 0.0.1
summary: |
  Command that will try and subscribe a given user
owners:
    - subscriptions-management
badges:
    - content: New!
      backgroundColor: green
      textColor: green
sidebar:
  badge: 'POST'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `SubscribeUser` command represents when a new user wants to subscribe to our service.

## Architecture diagram

<NodeGraph />

<Footer />
---
id: GetInventoryList
name: List inventory list
version: 0.0.1
summary: |
  GET request that will return inventory list
owners:
    - dboyne
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The GetInventoryList message is a query used to retrieve a comprehensive list of all available inventory items within a system. It is designed to return detailed information about each item, such as product names, quantities, availability status, and potentially additional metadata like categories or locations. This query is typically utilized by systems or services that require a real-time view of current stock, ensuring that downstream applications or users have accurate and up-to-date information for decision-making or operational purposes. The GetInventoryList is ideal for use cases such as order processing, stock management, or reporting, providing visibility into the full range of inventory data.

<NodeGraph />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "GetInventoryList",
    "description": "A query to retrieve a list of all available inventory items with their details.",
    "type": "object",
    "properties": {
      "filters": {
        "type": "object",
        "description": "Optional filters to narrow down the inventory search.",
        "properties": {
          "category": {
            "type": "string",
            "description": "Filter items by category (e.g., electronics, clothing, etc.)."
          },
          "location": {
            "type": "string",
            "description": "Filter items by storage location or warehouse."
          },
          "minStockLevel": {
            "type": "integer",
            "description": "Filter items with a stock level greater than or equal to this value."
          },
          "inStock": {
            "type": "boolean",
            "description": "Filter items that are currently in stock (true) or out of stock (false)."
          }
        },
        "additionalProperties": false
      },
      "pagination": {
        "type": "object",
        "description": "Pagination options for the query.",
        "properties": {
          "page": {
            "type": "integer",
            "description": "The current page of results.",
            "minimum": 1,
            "default": 1
          },
          "pageSize": {
            "type": "integer",
            "description": "The number of items per page.",
            "minimum": 1,
            "default": 10
          }
        },
        "required": ["page", "pageSize"]
      }
    },
    "required": [],
    "additionalProperties": false
  }
  
---
id: GetInventoryStatus
name: Get inventory status
version: 0.0.1
summary: |
  GET request that will return the current stock status for a specific product.
owners:
    - dboyne
badges:
    - content: GET Request
      backgroundColor: green
      textColor: green
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The GetInventoryStatus message is a query designed to retrieve the current stock status for a specific product. 

This query provides detailed information about the available quantity, reserved quantity, and the warehouse location where the product is stored. It is typically used by systems or services that need to determine the real-time availability of a product, enabling efficient stock management, order fulfillment, and inventory tracking processes. 

This query is essential for ensuring accurate stock levels are reported to downstream systems, including e-commerce platforms, warehouse management systems, and sales channels.

<NodeGraph />

<SchemaViewer file="schema.json" title="Schema" expand="true" maxHeight="500" search="true" />


### Query using CURL

Use this snippet to query the inventory status

```sh title="Example CURL command"
curl -X GET "https://api.yourdomain.com/inventory/status" \
-H "Content-Type: application/json" \
-d '{
  "productId": "12345"
}'
```

 ## Raw Schema:schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GetInventoryStatusResponse",
  "type": "object",
  "definitions": {
    "Coordinates": {
      "type": "object",
      "properties": {
        "latitude": {
          "type": "number",
          "minimum": -90,
          "maximum": 90,
          "description": "Latitude coordinate"
        },
        "longitude": {
          "type": "number",
          "minimum": -180,
          "maximum": 180,
          "description": "Longitude coordinate"
        }
      },
      "required": ["latitude", "longitude"],
      "additionalProperties": false
    },
    "LocationDetails": {
      "type": "object",
      "properties": {
        "facilityId": {
          "type": "string",
          "pattern": "^[A-Z]{2}[0-9]{4}$",
          "description": "Facility identifier in format CC0000"
        },
        "name": {
          "type": "string",
          "description": "Facility name"
        },
        "zone": {
          "type": "string",
          "enum": ["north", "south", "east", "west", "central"],
          "description": "Geographic zone"
        },
        "coordinates": {
          "$ref": "#/definitions/Coordinates"
        },
        "operatingHours": {
          "type": "object",
          "properties": {
            "openTime": {
              "type": "string",
              "pattern": "^([01]?[0-9]|2[0-3]):[0-5][0-9]$",
              "description": "Opening time in HH:MM format"
            },
            "closeTime": {
              "type": "string",
              "pattern": "^([01]?[0-9]|2[0-3]):[0-5][0-9]$",
              "description": "Closing time in HH:MM format"
            },
            "timeZone": {
              "type": "string",
              "description": "Time zone identifier"
            }
          },
          "required": ["openTime", "closeTime", "timeZone"],
          "additionalProperties": false
        }
      },
      "required": ["facilityId", "name", "zone", "coordinates", "operatingHours"],
      "additionalProperties": false
    },
    "SupplierInfo": {
      "type": "object",
      "properties": {
        "supplierId": {
          "type": "string",
          "description": "Unique supplier identifier"
        },
        "companyName": {
          "type": "string",
          "description": "Supplier company name"
        },
        "tier": {
          "type": "string",
          "enum": ["primary", "secondary", "backup"],
          "description": "Supplier tier level"
        },
        "performance": {
          "type": "object",
          "properties": {
            "onTimeDelivery": {
              "type": "number",
              "minimum": 0,
              "maximum": 100,
              "description": "On-time delivery percentage"
            },
            "qualityRating": {
              "type": "number",
              "minimum": 1,
              "maximum": 5,
              "description": "Quality rating (1-5 stars)"
            },
            "lastDeliveryDate": {
              "type": "string",
              "format": "date",
              "description": "Date of last delivery"
            }
          },
          "required": ["onTimeDelivery", "qualityRating"],
          "additionalProperties": false
        },
        "contractTerms": {
          "type": "object",
          "properties": {
            "minimumOrderQuantity": {
              "type": "integer",
              "minimum": 1,
              "description": "Minimum order quantity"
            },
            "pricePerUnit": {
              "type": "number",
              "minimum": 0,
              "description": "Price per unit in USD"
            },
            "currency": {
              "type": "string",
              "enum": ["USD", "EUR", "GBP", "CAD", "JPY"],
              "description": "Currency code"
            }
          },
          "required": ["minimumOrderQuantity", "pricePerUnit", "currency"],
          "additionalProperties": false
        }
      },
      "required": ["supplierId", "companyName", "tier", "performance", "contractTerms"],
      "additionalProperties": false
    },
    "InventoryMovement": {
      "type": "object",
      "properties": {
        "movementId": {
          "type": "string",
          "description": "Unique movement identifier"
        },
        "type": {
          "type": "string",
          "enum": ["inbound", "outbound", "transfer", "adjustment"],
          "description": "Type of inventory movement"
        },
        "quantity": {
          "type": "integer",
          "description": "Quantity moved (positive for inbound, negative for outbound)"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "When the movement occurred"
        },
        "reason": {
          "type": "string",
          "description": "Reason for the movement"
        },
        "reference": {
          "type": "object",
          "properties": {
            "orderId": {
              "type": "string",
              "description": "Related order ID if applicable"
            },
            "transferId": {
              "type": "string",
              "description": "Related transfer ID if applicable"
            },
            "userId": {
              "type": "string",
              "description": "User who initiated the movement"
            }
          },
          "additionalProperties": false
        }
      },
      "required": ["movementId", "type", "quantity", "timestamp", "reason"],
      "additionalProperties": false
    },
    "QualityMetrics": {
      "type": "object",
      "properties": {
        "inspectionDate": {
          "type": "string",
          "format": "date",
          "description": "Date of last quality inspection"
        },
        "grade": {
          "type": "string",
          "enum": ["A", "B", "C", "D", "F"],
          "description": "Quality grade"
        },
        "defectRate": {
          "type": "number",
          "minimum": 0,
          "maximum": 100,
          "description": "Defect rate percentage"
        },
        "expirationTracking": {
          "type": "object",
          "properties": {
            "hasExpiration": {
              "type": "boolean",
              "description": "Whether product has expiration date"
            },
            "nearExpiryCount": {
              "type": "integer",
              "minimum": 0,
              "description": "Count of items near expiration"
            },
            "expiredCount": {
              "type": "integer",
              "minimum": 0,
              "description": "Count of expired items"
            }
          },
          "required": ["hasExpiration"],
          "additionalProperties": false
        }
      },
      "required": ["inspectionDate", "grade", "defectRate", "expirationTracking"],
      "additionalProperties": false
    }
  },
  "properties": {
    "productId": {
      "type": "string",
      "description": "The unique identifier for the product"
    },
    "productMetadata": {
      "type": "object",
      "properties": {
        "sku": {
          "type": "string",
          "description": "Stock keeping unit"
        },
        "barcode": {
          "type": "string",
          "pattern": "^[0-9]{12,13}$",
          "description": "Product barcode (UPC/EAN)"
        },
        "category": {
          "type": "object",
          "properties": {
            "primary": {
              "type": "string",
              "description": "Primary category"
            },
            "secondary": {
              "type": "string",
              "description": "Secondary category"
            },
            "tags": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Category tags"
            }
          },
          "required": ["primary"],
          "additionalProperties": false
        },
        "dimensions": {
          "type": "object",
          "properties": {
            "length": {
              "type": "number",
              "minimum": 0,
              "description": "Length in centimeters"
            },
            "width": {
              "type": "number",
              "minimum": 0,
              "description": "Width in centimeters"
            },
            "height": {
              "type": "number",
              "minimum": 0,
              "description": "Height in centimeters"
            },
            "weight": {
              "type": "number",
              "minimum": 0,
              "description": "Weight in grams"
            }
          },
          "required": ["length", "width", "height", "weight"],
          "additionalProperties": false
        }
      },
      "required": ["sku", "barcode", "category", "dimensions"],
      "additionalProperties": false
    },
    "aggregatedInventory": {
      "type": "object",
      "properties": {
        "totalAvailable": {
          "type": "integer",
          "minimum": 0,
          "description": "Total available quantity across all locations"
        },
        "totalReserved": {
          "type": "integer",
          "minimum": 0,
          "description": "Total reserved quantity across all locations"
        },
        "totalInTransit": {
          "type": "integer",
          "minimum": 0,
          "description": "Total quantity in transit between locations"
        },
        "safetyStock": {
          "type": "integer",
          "minimum": 0,
          "description": "Safety stock level"
        },
        "reorderLevel": {
          "type": "integer",
          "minimum": 0,
          "description": "Reorder point threshold"
        }
      },
      "required": ["totalAvailable", "totalReserved", "totalInTransit", "safetyStock", "reorderLevel"],
      "additionalProperties": false
    },
    "locationBreakdown": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "location": {
            "$ref": "#/definitions/LocationDetails"
          },
          "inventory": {
            "type": "object",
            "properties": {
              "availableQuantity": {
                "type": "integer",
                "minimum": 0,
                "description": "Available quantity at this location"
              },
              "reservedQuantity": {
                "type": "integer",
                "minimum": 0,
                "description": "Reserved quantity at this location"
              },
              "lastCountDate": {
                "type": "string",
                "format": "date",
                "description": "Date of last physical count"
              }
            },
            "required": ["availableQuantity", "reservedQuantity", "lastCountDate"],
            "additionalProperties": false
          },
          "qualityMetrics": {
            "$ref": "#/definitions/QualityMetrics"
          }
        },
        "required": ["location", "inventory", "qualityMetrics"],
        "additionalProperties": false
      },
      "minItems": 1,
      "description": "Inventory breakdown by location"
    },
    "supplierInformation": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/SupplierInfo"
      },
      "description": "Information about suppliers for this product"
    },
    "recentMovements": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/InventoryMovement"
      },
      "maxItems": 10,
      "description": "Recent inventory movements (last 10)"
    },
    "alerts": {
      "type": "object",
      "properties": {
        "lowStock": {
          "type": "boolean",
          "description": "Whether product is below reorder level"
        },
        "qualityIssues": {
          "type": "boolean",
          "description": "Whether there are quality concerns"
        },
        "supplierDelays": {
          "type": "boolean",
          "description": "Whether there are supplier delivery delays"
        },
        "messages": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "severity": {
                "type": "string",
                "enum": ["info", "warning", "error", "critical"],
                "description": "Alert severity level"
              },
              "message": {
                "type": "string",
                "description": "Alert message"
              },
              "timestamp": {
                "type": "string",
                "format": "date-time",
                "description": "When the alert was generated"
              }
            },
            "required": ["severity", "message", "timestamp"],
            "additionalProperties": false
          },
          "description": "Alert messages"
        }
      },
      "required": ["lowStock", "qualityIssues", "supplierDelays", "messages"],
      "additionalProperties": false
    },
    "lastUpdated": {
      "type": "string",
      "format": "date-time",
      "description": "Timestamp when this data was last updated"
    }
  },
  "required": [
    "productId",
    "productMetadata",
    "aggregatedInventory",
    "locationBreakdown",
    "supplierInformation",
    "recentMovements",
    "alerts",
    "lastUpdated"
  ],
  "additionalProperties": false
}
  
---
id: GetUserNotifications
name: Get user notifications
version: 0.0.1
summary: |
  GET request that will return a list of notifications for a specific user, with options to filter by status (unread or all).
owners:
    - dboyne
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
schemaPath: schema.json
sidebar:
  badge: 'GET'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `GetUserNotifications` message is a query used to retrieve a list of notifications for a specific user. It allows filtering by notification status, such as unread or all notifications. This query is typically utilized by notification services to display user-specific messages, such as order updates, promotional offers, or system notifications. It supports pagination through `limit` and `offset` parameters, ensuring that only a manageable number of notifications are retrieved at once. This query helps users stay informed about important events or updates related to their account, orders, or the platform.

Use cases include delivering notifications for order updates, promotional campaigns, or general system messages to keep the user informed.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />



 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "GetUserNotificationsResponse",
    "type": "object",
    "properties": {
      "userId": {
        "type": "string",
        "description": "The unique identifier for the user."
      },
      "notifications": {
        "type": "array",
        "description": "A list of notifications for the user.",
        "items": {
          "type": "object",
          "properties": {
            "notificationId": {
              "type": "string",
              "description": "The unique identifier for the notification."
            },
            "title": {
              "type": "string",
              "description": "The title or subject of the notification."
            },
            "message": {
              "type": "string",
              "description": "The message body of the notification."
            },
            "status": {
              "type": "string",
              "enum": ["unread", "read"],
              "description": "The read status of the notification."
            },
            "createdAt": {
              "type": "string",
              "format": "date-time",
              "description": "The date and time when the notification was created."
            }
          },
          "required": ["notificationId", "title", "message", "status", "createdAt"],
          "additionalProperties": false
        }
      }
    },
    "required": ["userId", "notifications"],
    "additionalProperties": false
  }
  
---
id: GetNotificationDetails
name: Get notification details
version: 0.0.1
summary: |
  GET request that will return detailed information about a specific notification, identified by its notificationId.
owners:
    - dboyne
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
schemaPath: schema.json
sidebar:
  badge: 'GET'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `GetNotificationDetails` message is a query used to retrieve detailed information about a specific notification identified by its `notificationId`. It provides a comprehensive overview of the notification, including the title, message content, status (read/unread), the date it was created, and any additional metadata related to the notification, such as associated orders or system events. This query is helpful in scenarios where users or systems need detailed insights into a particular notification, such as retrieving full messages or auditing notifications sent to users.

Use cases include viewing detailed information about order updates, system notifications, or promotional messages, allowing users to view their full notification history and details.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />


 ## Raw Schema:schema.json


{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GetNotificationDetailsResponse",
  "type": "object",
  "properties": {
    "notificationId": {
      "type": "string",
      "description": "The unique identifier for the notification."
    },
    "title": {
      "type": "string",
      "description": "The title or subject of the notification."
    },
    "message": {
      "type": "string",
      "description": "The content or message body of the notification."
    },
    "status": {
      "type": "string",
      "enum": ["unread", "read"],
      "description": "The read status of the notification."
    },
    "userId": {
      "type": "string",
      "description": "The unique identifier for the user who received the notification."
    },
    "createdAt": {
      "type": "string",
      "format": "date-time",
      "description": "The date and time when the notification was created."
    },
    "type": {
      "type": "string",
      "description": "The type of the notification, such as order or system."
    },
    "metadata": {
      "type": "object",
      "description": "Additional metadata related to the notification, such as order details.",
      "properties": {
        "orderId": {
          "type": "string",
          "description": "The associated order ID, if applicable."
        },
        "shippingProvider": {
          "type": "string",
          "description": "The shipping provider for the associated order, if applicable."
        }
      },
      "required": ["orderId"],
      "additionalProperties": false
    }
  },
  "required": ["notificationId", "title", "message", "status", "userId", "createdAt", "type"],
  "additionalProperties": false
}

---
id: GetOrder
name: Get order details
version: 0.0.1
summary: |
  GET request that will return detailed information about a specific order, identified by its orderId.
owners:
    - order-management
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
schemaPath: schema.json
sidebar:
  badge: 'GET'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `GetOrder` message is a query used to retrieve detailed information about a specific order, identified by its `orderId`. It provides information such as the order status (e.g., pending, completed, shipped), the items within the order, billing and shipping details, payment information, and the order's total amount. This query is commonly used by systems managing order processing, customer service, or order tracking functionalities.

This query can be applied in e-commerce systems, marketplaces, or any platform where users and systems need real-time order data for tracking, auditing, or managing customer purchases.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json

{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "GetOrderQuery",
    "type": "object",
    "properties": {
      "orderId": {
        "type": "string",
        "format": "uuid",
        "description": "The unique identifier of the order being retrieved."
      }
    },
    "required": ["orderId"],
    "additionalProperties": false
  }
  
---
id: GetPaymentStatus
name: Get payment status
version: 0.0.1
summary: |
  GET request that will return the payment status for a specific order, identified by its orderId.
owners:
    - dboyne
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
schemaPath: schema.json
sidebar:
  badge: 'GET'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `GetPaymentStatus` message is a query used to retrieve the payment status for a specific order, identified by its `orderId`. This query returns the current status of the payment, such as whether it is pending, completed, failed, or refunded. It is used by systems that need to track the lifecycle of payments associated with orders, ensuring that the payment has been successfully processed or identifying if any issues occurred during the transaction.

This query is useful in scenarios such as order management, refund processing, or payment auditing, ensuring that users or systems have real-time visibility into the payment status for a given order.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json


{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GetPaymentStatusResponse",
  "type": "object",
  "properties": {
    "orderId": {
      "type": "string",
      "description": "The unique identifier for the order."
    },
    "paymentStatus": {
      "type": "string",
      "enum": ["pending", "completed", "failed", "refunded"],
      "description": "The current payment status of the order."
    },
    "amount": {
      "type": "number",
      "description": "The amount paid for the order."
    },
    "currency": {
      "type": "string",
      "description": "The currency in which the payment was made (e.g., USD, EUR)."
    },
    "paymentMethod": {
      "type": "string",
      "description": "The payment method used for the transaction (e.g., Credit Card, PayPal)."
    },
    "transactionId": {
      "type": "string",
      "description": "The unique identifier for the payment transaction."
    },
    "paymentDate": {
      "type": "string",
      "format": "date-time",
      "description": "The date and time when the payment was processed."
    }
  },
  "required": ["orderId", "paymentStatus", "amount", "currency", "paymentMethod", "transactionId", "paymentDate"],
  "additionalProperties": false
}

---
id: GetSubscriptionStatus
name: Get subscription status
version: 0.0.2
summary: |
  GET request that will return the current subscription status for a specific user, identified by their userId.
owners:
    - subscriptions-management
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
schemaPath: schema.json
sidebar:
  badge: 'GET'
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `GetSubscriptionStatus` message is a query used to retrieve the current subscription status for a specific user, identified by their `userId`. This query returns detailed information about the user's subscription, such as its current status (active, canceled, expired), the subscription tier or plan, and the next billing date. It is typically used by systems that manage user subscriptions, billing, and renewal processes to ensure that users are aware of their subscription details and any upcoming renewals.

This query is particularly useful in managing subscriptions for SaaS products, media services, or any recurring payment-based services where users need to manage and view their subscription information.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json


{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GetSubscriptionStatusResponse",
  "type": "object",
  "properties": {
    "userId": {
      "type": "string",
      "description": "The unique identifier for the user."
    },
    "subscriptionStatus": {
      "type": "string",
      "enum": ["active", "canceled", "expired", "pending"],
      "description": "The current status of the user's subscription."
    },
    "subscriptionPlan": {
      "type": "string",
      "description": "The name or tier of the subscription plan."
    },
    "nextBillingDate": {
      "type": "string",
      "format": "date-time",
      "description": "The date and time of the next billing or renewal."
    },
    "billingFrequency": {
      "type": "string",
      "enum": ["monthly", "yearly"],
      "description": "The frequency of the billing cycle."
    },
    "amount": {
      "type": "number",
      "description": "The amount to be billed for the subscription."
    },
    "currency": {
      "type": "string",
      "description": "The currency in which the subscription is billed (e.g., USD, EUR)."
    },
    "lastPaymentDate": {
      "type": "string",
      "format": "date-time",
      "description": "The date and time when the last payment was processed."
    }
  },
  "required": ["userId", "subscriptionStatus", "subscriptionPlan", "nextBillingDate", "billingFrequency", "amount", "currency", "lastPaymentDate"],
  "additionalProperties": false
}

---
id: GetSubscriptionStatus
name: Get subscription status
version: 0.0.1
summary: |
  GET request that will return the current subscription status for a specific user, identified by their userId.
owners:
    - dboyne
badges:
    - content: Recently updated!
      backgroundColor: green
      textColor: green
schemaPath: schema.json
---

import Footer from '@catalog/components/footer.astro';

## Overview

The `GetSubscriptionStatus` message is a query used to retrieve the current subscription status for a specific user, identified by their `userId`. This query returns detailed information about the user's subscription, such as its current status (active, canceled, expired), the subscription tier or plan, and the next billing date. It is typically used by systems that manage user subscriptions, billing, and renewal processes to ensure that users are aware of their subscription details and any upcoming renewals.

This query is particularly useful in managing subscriptions for SaaS products, media services, or any recurring payment-based services where users need to manage and view their subscription information.

<NodeGraph />

<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" />

 ## Raw Schema:schema.json


{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GetSubscriptionStatusResponse",
  "type": "object",
  "properties": {
    "userId": {
      "type": "string",
      "description": "The unique identifier for the user."
    },
    "subscriptionStatus": {
      "type": "string",
      "enum": ["active", "canceled", "expired", "pending"],
      "description": "The current status of the user's subscription."
    },
    "subscriptionPlan": {
      "type": "string",
      "description": "The name or tier of the subscription plan."
    },
    "nextBillingDate": {
      "type": "string",
      "format": "date-time",
      "description": "The date and time of the next billing or renewal."
    },
    "billingFrequency": {
      "type": "string",
      "enum": ["monthly", "yearly"],
      "description": "The frequency of the billing cycle."
    },
    "amount": {
      "type": "number",
      "description": "The amount to be billed for the subscription."
    },
    "currency": {
      "type": "string",
      "description": "The currency in which the subscription is billed (e.g., USD, EUR)."
    },
    "lastPaymentDate": {
      "type": "string",
      "format": "date-time",
      "description": "The date and time when the last payment was processed."
    }
  },
  "required": ["userId", "subscriptionStatus", "subscriptionPlan", "nextBillingDate", "billingFrequency", "amount", "currency", "lastPaymentDate"],
  "additionalProperties": false
}

---
id: InventoryService
version: 0.0.2
name: Inventory Service
summary: |
  Service that handles the inventory
owners:
    - order-management
receives:
  - id: OrderConfirmed
  - id: GetInventoryList
  - id: OrderAmended
  - id: UpdateInventory
  - id: AddInventory
  - id: GetInventoryStatus
  - id: DeleteInventory
sends:
  - id: InventoryAdjusted
  - id: OutOfStock
  - id: GetOrder
repository:
  language: JavaScript
  url: https://github.com/event-catalog/pretend-shipping-service
deprecated:
  date: 2026-05-01
  message: | 
    This service is **being deprecated** and replaced by the new service **InventoryServiceV2**.
    Please contact the [team for more information](mailto:inventory-team@example.com) or visit our [website](https://eventcatalog.dev).
---

import Footer from '@catalog/components/footer.astro';

## Overview

The Inventory Service is a critical component of the system responsible for managing product stock levels, tracking inventory movements, and ensuring product availability. It interacts with other services to maintain accurate inventory records and supports operations such as order fulfillment, restocking, and inventory audits.

<Tiles >
    <Tile icon="DocumentIcon" href={`/docs/services/${frontmatter.id}/${frontmatter.version}/changelog`}  title="View the changelog" description="Want to know the history of this service? View the change logs" />
    <Tile icon="UserGroupIcon" href="/docs/teams/full-stack" title="Contact the team" description="Any questions? Feel free to contact the owners" />
    <Tile icon="BoltIcon" href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Sends ${frontmatter.sends.length} messages`} description="This service sends messages to downstream consumers" />
    <Tile icon="BoltIcon"  href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Receives ${frontmatter.receives.length} messages`} description="This service receives messages from other services" />
</Tiles>

## Core features

| Feature | Description |
|---------|-------------|
| Real-time Stock Tracking | Monitors inventory levels across all warehouses in real-time |
| Automated Reordering | Triggers purchase orders when stock levels fall below defined thresholds |
| Multi-warehouse Support | Manages inventory across multiple warehouse locations |
| Batch Processing | Handles bulk inventory updates and adjustments efficiently |

## Architecture diagram

<NodeGraph title="Hello world" />

<MessageTable format="all" limit={4} />

# Infrastructure

The Inventory Service is hosted on AWS.

The diagram below shows the infrastructure of the Inventory Service. The service is hosted on AWS and uses AWS Lambda to handle the inventory requests. The inventory is stored in an AWS Aurora database and the inventory metadata is stored in an AWS S3 bucket.

```mermaid
architecture-beta
    group api(logos:aws)

    service db(logos:aws-aurora)[Inventory DB] in api
    service disk1(logos:aws-s3)[Inventory Metadata] in api
    service server(logos:aws-lambda)[Inventory Handler] in api

    db:L -- R:server
    disk1:T -- B:server
```

You can find more information about the Inventory Service infrastructure in the [Inventory Service documentation](https://github.com/event-catalog/pretend-shipping-service/blob/main/README.md).



<Steps title="How to connect to Inventory Service">
  <Step title="Obtain API credentials">
    Request API credentials from the Inventory Service team.
  </Step>
  <Step title="Install the SDK">
    Run the following command in your project directory:
    ```bash
    npm install inventory-service-sdk
    ```
  </Step>
  <Step title="Initialize the client">
  Use the following code to initialize the Inventory Service client:

  ```js
  const InventoryService = require('inventory-service-sdk');
  const client = new InventoryService.Client({
    clientId: 'YOUR_CLIENT_ID',
    clientSecret: 'YOUR_CLIENT_SECRET',
    apiUrl: 'https://api.inventoryservice.com/v1'
  });
```
  </Step>
  <Step title="Make API calls">
  
  You can now use the client to make API calls. For example, to get all products:

  ```js
  client.getProducts()
    .then(products => console.log(products))
    .catch(error => console.error(error));
  ```
  </Step>
</Steps>

<Footer />
---
id: NotificationService
version: 0.0.2
name: Notifications
summary: |
  Service that handles orders
owners:
    - order-management
receives:
  - id: InventoryAdjusted
    version: ">1.0.0"
  - id: PaymentProcessed
    version: ^1.0.0
  - id: GetUserNotifications
    version: x
  - id: GetNotificationDetails
    version: x
sends:
  - id: OutOfStock
    version: latest
  - id: GetInventoryList
    version: 0.0.x
repository:
  language: JavaScript
  url: https://github.com/event-catalog/pretend-shipping-service
---

import Footer from '@catalog/components/footer.astro';

## Overview

The Notification Service is responsible for managing and delivering notifications to users and other services. It supports various notification channels such as email, SMS, push notifications, and in-app notifications. The service ensures reliable and timely delivery of messages and integrates with other services to trigger notifications based on specific events.

<Tiles >
    <Tile icon="DocumentIcon" href={`/docs/services/${frontmatter.id}/${frontmatter.version}/changelog`}  title="View the changelog" description="Want to know the history of this service? View the change logs" />
    <Tile icon="UserGroupIcon" href="/docs/teams/full-stack" title="Contact the team" description="Any questions? Feel free to contact the owners" />
    <Tile icon="BoltIcon" href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Sends ${frontmatter.sends.length} messages`} description="This service sends messages to downstream consumers" />
    <Tile icon="BoltIcon"  href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Receives ${frontmatter.receives.length} messages`} description="This service receives messages from other services" />
</Tiles>

### Core features

| Feature | Description |
|---------|-------------|
| Multi-Channel Delivery | Supports notifications via email, SMS, push notifications, and in-app messages |
| Template Management | Customizable notification templates with dynamic content placeholders |
| Delivery Status Tracking | Real-time tracking and monitoring of notification delivery status |
| Rate Limiting | Prevents notification flooding through configurable rate limits |
| Priority Queue | Handles urgent notifications with priority delivery mechanisms |
| Batch Processing | Efficiently processes and sends bulk notifications |
| Retry Mechanism | Automatic retry logic for failed notification deliveries |
| Event-Driven Notifications | Triggers notifications based on system events and user actions |



## Architecture diagram

<NodeGraph />

<MessageTable format="all" limit={4} />

## Core Concepts

<AccordionGroup>
  <Accordion title="Notification">
    - Description: A message that is sent to a user or a service.
    - Attributes: notificationId, type, recipient, content, channel, status, timestamp
  </Accordion>
  <Accordion title="Channel">
    - Description: The medium through which the notification is delivered (e.g., email, SMS, push notification).
    - Attributes: channelId, name, provider, configuration 
  </Accordion>
</AccordionGroup>

## Infrastructure

The Notification Service is hosted on AWS.

The diagram below shows the infrastructure of the Notification Service. The service is hosted on AWS and uses AWS Lambda to handle the notification requests. The notification is stored in an AWS Aurora database and the notification metadata is stored in an AWS S3 bucket.

```mermaid
architecture-beta
    group api(logos:aws)

    service db(logos:aws-aurora)[Notification DB] in api
    service disk1(logos:aws-s3)[Notification Metadata] in api
    service server(logos:aws-lambda)[Notification Handler] in api

    db:L -- R:server
    disk1:T -- B:server
```

You can find more information about the Notification Service infrastructure in the [Notification Service documentation](https://github.com/event-catalog/pretend-shipping-service/blob/main/README.md).

<Footer />
---
id: OrdersService
version: 0.0.3
name: Orders Service
summary: |
  Service that handles orders
owners:
    - order-management
receives:
  - id: InventoryAdjusted
  - id: GetOrder
  - id: PlaceOrder
  - id: UserSubscriptionCancelled
sends:
  - id: OrderAmended
  - id: OrderCancelled
  - id: OrderConfirmed
  - id: AddInventory
    version: 0.0.3
repository:
  language: JavaScript
  url: https://github.com/event-catalog/pretend-shipping-service
schemaPath: "openapi-v1.yml"
specifications:
  - type: asyncapi
    path: order-service-asyncapi.yaml
  - type: openapi
    path: openapi-v1.yml
    name: v1 API
  - type: openapi
    path: openapi-v2.yml
    name: v2 API
---

import Footer from '@catalog/components/footer.astro';

## Overview

The Orders Service is responsible for managing customer orders within the system. It handles order creation, updating, status tracking, and interactions with other services such as Inventory, Payment, and Notification services to ensure smooth order processing and fulfillment.

<Tiles >
    <Tile icon="DocumentIcon" href={`/docs/services/${frontmatter.id}/${frontmatter.version}/changelog`}  title="View the changelog" description="Want to know the history of this service? View the change logs" />
    <Tile icon="UserGroupIcon" href="/docs/teams/full-stack" title="Contact the team" description="Any questions? Feel free to contact the owners" />
    <Tile icon="BoltIcon" href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Sends ${frontmatter.sends.length} messages`} description="This service sends messages to downstream consumers" />
    <Tile icon="BoltIcon"  href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Receives ${frontmatter.receives.length} messages`} description="This service receives messages from other services" />
</Tiles>

### Core features

| Feature | Description |
|---------|-------------|
| Order Management | Handles order creation, updates, and status tracking |
| Inventory Integration | Validates and processes inventory for incoming orders |
| Payment Processing | Integrates with payment gateways to handle payment transactions |
| Notification Integration | Sends notifications to users and other services |

## Architecture diagram 

<NodeGraph />

<MessageTable format="all" limit={4} />

## Infrastructure

The Orders Service is hosted on AWS.

The diagram below shows the infrastructure of the Orders Service. The service is hosted on AWS and uses AWS Lambda to handle the order requests. The order is stored in an AWS Aurora database and the order metadata is stored in an AWS S3 bucket.

```mermaid
architecture-beta
    group api(logos:aws)

    service db(logos:aws-aurora)[Order DB] in api
    service disk1(logos:aws-s3)[Order Metadata] in api
    service server(logos:aws-lambda)[Order Handler] in api

    db:L -- R:server
    disk1:T -- B:server
```

You can find more information about the Orders Service infrastructure in the [Orders Service documentation](https://github.com/event-catalog/pretend-shipping-service/blob/main/README.md).

<Footer />


 ## Raw Schema:order-service-asyncapi.yaml

asyncapi: 3.0.0

info:
  title: Order service
  description: | 
    This service is in charge of processing order events.
  version: '1.0.0'

servers: 
  topic:
    host: https://mytopic.com
    description: Custom Topic.
    protocol: HTTPS

defaultContentType: application/json

channels:
  orderEventsChannel:
    address: 'orders.{orderId}'
    description: All Order related events are distributed and broadcasted for the interested consumers.
    title: Order events channel
    messages:
      OrderConfirmed:
        summary: Order confirmed event
        $ref: '#/components/messages/OrderConfirmed'
      OrderPlaced:
        summary: Order placed event
        $ref: '#/components/messages/OrderPlaced'

operations: 
  onOrderConfirmation:
    summary: Action to confirm an order.
    description: The product availability of an order will lead to the confirmation of the order.
    title: Order Confirmed
    channel:
      $ref: '#/channels/orderEventsChannel'
    action: send
  onOrderPlacement:
    summary: Action to place an order.
    description: The reception and validation of an order will lead to the placement of the order.
    title: Order Placed
    channel:
      $ref: '#/channels/orderEventsChannel'
    action: send

components:
  messages:
    OrderConfirmed:
      payload:
        $ref: '#/components/schemas/OrderConfirmed'

    OrderPlaced:
      payload:
        $ref: '#/components/schemas/OrderPlaced'

  schemas:
    orderId:
      description: The unique identifier of an order
      type: string
      pattern: ^([A-Za-z0-9_-]{21})$

    userId:
      description: The unique identifier of a user
      type: string
      pattern: ^([A-Za-z0-9_-]{21})$

    productId:
      description: The product unique identifier
      type: string
      pattern: ^([A-Za-z0-9_-]{21})$

    Order:
      required:
        - orderId
        - userId
        - productId
        - price
        - quantity
        - orderDate
      type: object
      description: order model
      properties:
        orderId:
          "$ref": "#/components/schemas/orderId"
        orderDate:
          description: Date of order submition.
          type: string
          format: date-time
        userId:
          "$ref": "#/components/schemas/userId"
        productId:
          "$ref": "#/components/schemas/productId"
        price:
          type: number
        quantity:
          type: integer
      title: Order

    EventEnvelope:
      type: object
      allOf:
      - $ref: 'https://raw.githubusercontent.com/cloudevents/spec/v1.0.1/spec.json'
      properties:
        id:
          type: string
          format: uuid
        idempotencykey:
          type: string
          format: uuid
        correlationid:
          type: string
          format: uuid
        causationid:
          type: string
          format: uuid

    EventType:
      type: string
      enum: 
        - "order.placed" 
        - "order.confirmed"

    OrderConfirmed:
      type: object
      additionalProperties: false
      allOf:
        - $ref: '#/components/schemas/EventEnvelope'  
      properties:
        data:
          $ref: '#/components/schemas/Order'
        type:
          $ref: '#/components/schemas/EventType'

      required:
        - data

    OrderPlaced:
      type: object
      additionalProperties: false
      allOf:
        - $ref: '#/components/schemas/EventEnvelope'
      properties:
        data:
          $ref: '#/components/schemas/Order'
        type:
          $ref: '#/components/schemas/EventType'
      required:
        - data


 ## Raw Schema:openapi-v1.yml

openapi: 3.0.3
info:
  title: Orders Service API
  description: API for managing customer orders
  version: 1.0.0

servers:
  - url: https://api.example.com/v1
    description: Production server
  - url: https://staging-api.example.com/v1
    description: Staging server

paths:
  /orders:
    get:
      summary: List all orders
      description: Retrieve a list of orders with optional filtering
      parameters:
        - name: status
          in: query
          description: Filter orders by status
          schema:
            type: string
            enum: [pending, processing, completed, cancelled]
        - name: customerId
          in: query
          description: Filter orders by customer ID
          schema:
            type: string
        - name: page
          in: query
          description: Page number for pagination
          schema:
            type: integer
            minimum: 1
            default: 1
        - name: limit
          in: query
          description: Number of items per page
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
      responses:
        '200':
          description: Successfully retrieved orders
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderList'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'

    post:
      summary: Create a new order
      description: Create a new order for a customer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrderCreate'
      responses:
        '201':
          description: Order created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /orders/{orderId}:
    get:
      summary: Get order by ID
      description: Retrieve detailed information about a specific order
      parameters:
        - name: orderId
          in: path
          required: true
          description: Unique identifier of the order
          schema:
            type: string
      responses:
        '200':
          description: Order found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '404':
          $ref: '#/components/responses/NotFound'
        '401':
          $ref: '#/components/responses/Unauthorized'

    patch:
      summary: Update order status
      description: Update the status of an existing order
      parameters:
        - name: orderId
          in: path
          required: true
          description: Unique identifier of the order
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrderUpdate'
      responses:
        '200':
          description: Order updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '400':
          $ref: '#/components/responses/BadRequest'
        '404':
          $ref: '#/components/responses/NotFound'
        '401':
          $ref: '#/components/responses/Unauthorized'

components:
  schemas:
    OrderCreate:
      type: object
      required:
        - customerId
        - items
      properties:
        customerId:
          type: string
          description: Unique identifier of the customer
        items:
          type: array
          items:
            $ref: '#/components/schemas/OrderItem'
        shippingAddress:
          $ref: '#/components/schemas/Address'
        billingAddress:
          $ref: '#/components/schemas/Address'

    OrderUpdate:
      type: object
      required:
        - status
      properties:
        status:
          type: string
          enum: [pending, processing, completed, cancelled]
          description: New status of the order

    Order:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the order
        customerId:
          type: string
          description: Unique identifier of the customer
        status:
          type: string
          enum: [pending, processing, completed, cancelled]
        items:
          type: array
          items:
            $ref: '#/components/schemas/OrderItem'
        totalAmount:
          type: number
          format: float
        shippingAddress:
          $ref: '#/components/schemas/Address'
        billingAddress:
          $ref: '#/components/schemas/Address'
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

    OrderList:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/Order'
        pagination:
          $ref: '#/components/schemas/Pagination'

    OrderItem:
      type: object
      required:
        - productId
        - quantity
      properties:
        productId:
          type: string
        quantity:
          type: integer
          minimum: 1
        price:
          type: number
          format: float
        name:
          type: string

    Address:
      type: object
      required:
        - street
        - city
        - country
        - postalCode
      properties:
        street:
          type: string
        city:
          type: string
        state:
          type: string
        country:
          type: string
        postalCode:
          type: string

    Pagination:
      type: object
      properties:
        totalItems:
          type: integer
        totalPages:
          type: integer
        currentPage:
          type: integer
        itemsPerPage:
          type: integer

    Error:
      type: object
      properties:
        code:
          type: string
        message:
          type: string
        details:
          type: array
          items:
            type: string

  responses:
    BadRequest:
      description: Invalid request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - BearerAuth: []

 ## Raw Schema:openapi-v2.yml

openapi: 3.0.3
info:
  title: Orders Service API
  description: API for managing customer orders
  version: 2.0.0

servers:
  - url: https://api.example.com/v1
    description: Production server
  - url: https://staging-api.example.com/v1
    description: Staging server

paths:
  /orders:
    post:
      summary: Create a new order
      description: Create a new order for a customer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrderCreate'
      responses:
        '201':
          description: Order created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /orders/{orderId}:
    get:
      summary: Get order by ID
      description: Retrieve detailed information about a specific order
      parameters:
        - name: orderId
          in: path
          required: true
          description: Unique identifier of the order
          schema:
            type: string
      responses:
        '200':
          description: Order found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '404':
          $ref: '#/components/responses/NotFound'
        '401':
          $ref: '#/components/responses/Unauthorized'

    patch:
      summary: Update order status
      description: Update the status of an existing order
      parameters:
        - name: orderId
          in: path
          required: true
          description: Unique identifier of the order
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrderUpdate'
      responses:
        '200':
          description: Order updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '400':
          $ref: '#/components/responses/BadRequest'
        '404':
          $ref: '#/components/responses/NotFound'
        '401':
          $ref: '#/components/responses/Unauthorized'

components:
  schemas:
    OrderCreate:
      type: object
      required:
        - customerId
        - items
      properties:
        customerId:
          type: string
          description: Unique identifier of the customer
        items:
          type: array
          items:
            $ref: '#/components/schemas/OrderItem'
        shippingAddress:
          $ref: '#/components/schemas/Address'
        billingAddress:
          $ref: '#/components/schemas/Address'

    OrderUpdate:
      type: object
      required:
        - status
      properties:
        status:
          type: string
          enum: [pending, processing, completed, cancelled]
          description: New status of the order

    Order:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the order
        customerId:
          type: string
          description: Unique identifier of the customer
        status:
          type: string
          enum: [pending, processing, completed, cancelled]
        items:
          type: array
          items:
            $ref: '#/components/schemas/OrderItem'
        totalAmount:
          type: number
          format: float
        shippingAddress:
          $ref: '#/components/schemas/Address'
        billingAddress:
          $ref: '#/components/schemas/Address'
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

    OrderList:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/Order'
        pagination:
          $ref: '#/components/schemas/Pagination'

    OrderItem:
      type: object
      required:
        - productId
        - quantity
      properties:
        productId:
          type: string
        quantity:
          type: integer
          minimum: 1
        price:
          type: number
          format: float
        name:
          type: string

    Address:
      type: object
      required:
        - street
        - city
        - country
        - postalCode
      properties:
        street:
          type: string
        city:
          type: string
        state:
          type: string
        country:
          type: string
        postalCode:
          type: string

    Pagination:
      type: object
      properties:
        totalItems:
          type: integer
        totalPages:
          type: integer
        currentPage:
          type: integer
        itemsPerPage:
          type: integer

    Error:
      type: object
      properties:
        code:
          type: string
        message:
          type: string
        details:
          type: array
          items:
            type: string

  responses:
    BadRequest:
      description: Invalid request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - BearerAuth: []
---
id: ShippingService
version: 0.0.1
name: Shipping Service
summary: |
  Service that handles shipping
owners:
    - dboyne
receives:
  - id: CancelShipment
  - id: CreateReturnLabel
  - id: CreateShipment
  - id: UpdateShipmentStatus
  - id: PaymentProcessed
sends:
  - id: ShipmentCreated
  - id: ReturnInitiated
  - id: ShipmentDispatched
  - id: ShipmentInTransit
  - id: ShipmentDelivered
  - id: DeliveryFailed
repository:
  language: JavaScript
  url: https://github.com/event-catalog/pretend-shipping-service
---

import Footer from '@catalog/components/footer.astro';

## Overview

The Shipping Service is responsible for managing shipping within the system. It handles order creation, updating, status tracking, and interactions with other services such as Inventory, Payment, and Notification services to ensure smooth order processing and fulfillment.

<Tiles >
    <Tile icon="BoltIcon" href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Sends ${frontmatter.sends.length} messages`} description="This service sends messages to downstream consumers" />
    <Tile icon="BoltIcon"  href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Receives ${frontmatter.receives.length} messages`} description="This service receives messages from other services" />
</Tiles>

### Core features

The Shipping Service is responsible for managing shipping within the system. It handles order creation, updating, status tracking, and interactions with other services such as Inventory, Payment, and Notification services to ensure smooth order processing and fulfillment.


## Architecture diagram 

<NodeGraph />

<MessageTable format="all" limit={4} />

<Footer />
---
id: FraudDetectionService
version: 0.0.1
name: Fraud Detection Service
summary: Analyzes payment transactions for fraudulent activity and risk assessment
repository:
  url: https://github.com/eventcatalog/fraud-detection-service
receives:
  - id: PaymentInitiated
    version: 0.0.1
  - id: PaymentProcessed
    version: 0.0.1
  - id: SubscriptionPaymentDue
    version: 0.0.1
sends:
  - id: FraudCheckCompleted
    version: 0.0.1
  - id: FraudDetected
    version: 0.0.1
  - id: RiskScoreCalculated
    version: 0.0.1
owners:
  - dboyne
---

import Footer from '@catalog/components/footer.astro'

## Overview

The Fraud Detection Service is responsible for analyzing payment transactions in real-time to detect potential fraudulent activity. It uses machine learning models and rule-based systems to assess risk and prevent financial losses.

## Key Features

- **Real-time Transaction Analysis**: Analyzes transactions as they occur
- **Machine Learning Models**: Uses ML to identify suspicious patterns
- **Risk Scoring**: Calculates risk scores for each transaction
- **Automated Blocking**: Can automatically block high-risk transactions
- **Manual Review Queue**: Flags medium-risk transactions for manual review

## API Endpoints

### REST API
- `POST /api/fraud/check` - Submit transaction for fraud check
- `GET /api/fraud/risk-score/{transactionId}` - Get risk score for transaction
- `PUT /api/fraud/override/{transactionId}` - Manual override of fraud decision

## Configuration

```yaml
fraud_detection:
  risk_thresholds:
    high: 80
    medium: 50
    low: 20
  auto_block_threshold: 90
  ml_model_version: "2.3.1"
```

<Footer />
---
id: PaymentGatewayService
version: 0.0.1
name: Payment Gateway Service
summary: Manages integration with external payment processors (Stripe, PayPal, etc.)
tags:
  - payment
  - gateway
  - integration
repository:
  url: https://github.com/eventcatalog/payment-gateway-service
receives:
  - id: ProcessPayment
    version: 0.0.1
  - id: FraudCheckCompleted
    version: 0.0.1
sends:
  - id: PaymentFailed
    version: 0.0.1
owners:
  - dboyne
---

import Footer from '@catalog/components/footer.astro'

## Overview

The Payment Gateway Service acts as an abstraction layer between our payment system and external payment processors. It handles the complexity of integrating with multiple payment providers and provides a unified interface for payment operations.

<NodeGraph />

## Supported Payment Providers

- **Stripe**: Credit/debit cards, digital wallets
- **PayPal**: PayPal accounts, PayPal Credit
- **Square**: In-person and online payments
- **Adyen**: Global payment processing
- **Braintree**: Multiple payment methods

## Key Features

- **Multi-provider Support**: Switch between providers seamlessly
- **Retry Logic**: Automatic retry for failed transactions
- **Tokenization**: Secure card data handling
- **Webhook Management**: Handles provider webhooks
- **Currency Conversion**: Support for 150+ currencies

## API Endpoints

### REST API
- `POST /api/gateway/authorize` - Authorize a payment
- `POST /api/gateway/capture` - Capture an authorized payment
- `POST /api/gateway/refund` - Process a refund
- `GET /api/gateway/status/{transactionId}` - Get transaction status

## Configuration

```yaml
payment_gateway:
  providers:
    stripe:
      api_key: ${STRIPE_API_KEY}
      webhook_secret: ${STRIPE_WEBHOOK_SECRET}
    paypal:
      client_id: ${PAYPAL_CLIENT_ID}
      client_secret: ${PAYPAL_CLIENT_SECRET}
  retry:
    max_attempts: 3
    backoff_ms: 1000
```

<Footer />
---
id: PaymentService
name: Payment Service
version: 0.0.1
summary: |
  Service that handles payments
owners:
    - dboyne
receives:
  - id: PaymentInitiated
    version: 0.0.1
  - id: GetPaymentStatus
  - id: UserSubscriptionStarted
  - id: InventoryAdjusted
sends:
  - id: PaymentProcessed
    version: 0.0.1
  - id: GetOrder
repository:
  language: JavaScript
  url: https://github.com/event-catalog/pretend-shipping-service
---

The Payment Service is a crucial component of our system that handles all payment-related operations. It processes payments, manages transactions, and communicates with other services through events. Using an event-driven architecture, it ensures that all actions are asynchronous, decoupled, and scalable.

### Core features

| Feature | Description |
|---------|-------------|
| Payment Processing | Processes payments and manages transactions |
| Event-Driven Architecture | Ensures asynchronous, decoupled, and scalable operations |
| Integration with Payment Gateways | Interfaces with external payment providers |

<NodeGraph />

<MessageTable format="all" limit={4} />

## Infrastructure

The Payment Service is hosted on AWS.

The diagram below shows the infrastructure of the Payment Service. The service is hosted on AWS and uses AWS Lambda to handle the payment requests. The payment is stored in an AWS Aurora database and the payment metadata is stored in an AWS S3 bucket.

```mermaid
architecture-beta
    group api(logos:aws)

    service db(logos:aws-aurora)[Payment DB] in api
    service disk1(logos:aws-s3)[Payment Metadata] in api
    service server(logos:aws-lambda)[Payment Handler] in api

    db:L -- R:server
    disk1:T -- B:server
```

You can find more information about the Payment Service infrastructure in the [Payment Service documentation](https://github.com/event-catalog/pretend-payment-service/blob/main/README.md).

### Key Components
- Payment API: Exposes endpoints for initiating payments and querying payment status.
- Payment Processor: Handles the core payment processing logic.
- Event Bus: Manages the communication between services using events.
- Payment Gateway: Interfaces with external payment providers.
- Transaction Service: Manages transaction records and states.
- Notification Service: Sends notifications related to payment status changes.
- Database: Stores transaction data and payment status.
---
id: BillingService
version: 0.0.1
name: Billing Service
summary: Manages billing cycles, invoice generation, and payment scheduling for subscriptions
tags:
  - billing
  - subscriptions
  - invoicing
repository:
  url: https://github.com/eventcatalog/billing-service
receives:
  - id: PaymentProcessed
    version: 0.0.1
  - id: PaymentFailed
    version: 0.0.1
sends:
  - id: SubscriptionPaymentDue
    version: 0.0.1
  - id: ProcessPayment
    version: 0.0.1
owners:
  - dboyne
---

import Footer from '@catalog/components/footer.astro'

## Overview

The Billing Service is responsible for managing all billing-related operations for subscriptions. It calculates billing cycles, generates invoices, and coordinates with payment services to ensure timely payment collection.

## Key Features

- **Billing Cycle Management**: Handles daily, weekly, monthly, quarterly, and annual billing cycles
- **Invoice Generation**: Creates detailed invoices with line items and tax calculations
- **Payment Scheduling**: Schedules recurring payments based on billing cycles
- **Proration**: Calculates prorated charges for mid-cycle changes
- **Dunning Management**: Handles failed payment retry logic

## API Endpoints

### REST API
- `GET /api/billing/invoice/{subscriptionId}` - Get current invoice
- `GET /api/billing/history/{subscriptionId}` - Get billing history
- `POST /api/billing/preview` - Preview upcoming charges
- `PUT /api/billing/retry/{invoiceId}` - Retry failed payment

## Billing Cycle States

```mermaid
stateDiagram-v2
    [*] --> Scheduled
    Scheduled --> Processing
    Processing --> Paid
    Processing --> Failed
    Failed --> Retrying
    Retrying --> Paid
    Retrying --> Suspended
    Paid --> [*]
    Suspended --> [*]
```

## Configuration

```yaml
billing_service:
  cycles:
    - daily
    - weekly
    - monthly
    - quarterly
    - annual
  retry_attempts: 3
  retry_interval_days: [1, 3, 7]
  invoice_generation_lead_days: 7
```

<Footer />
---
id: SubscriptionService
version: 0.0.1
name: Subscription Service
summary: |
  Service that handles subscriptions
owners:
    - subscriptions-management
receives:
  - id: SubscribeUser
    version: 0.0.1
  - id: CancelSubscription
    version: 0.0.1
  - id: GetSubscriptionStatus  
  - id: PaymentProcessed
    version: 0.0.1
sends:
  - id: UserSubscriptionStarted
    version: 0.0.1
  - id: UserSubscriptionCancelled  
    version: 0.0.1
repository:
  language: JavaScript
  url: https://github.com/event-catalog/pretend-subscription-service
---

import Footer from '@catalog/components/footer.astro';

## Overview

The subscription Service is responsible for handling customer subscriptions in our system. It handles new subscriptions, cancelling subscriptions and updating them.

<Tiles >
    <Tile icon="DocumentIcon" href={`/docs/services/${frontmatter.id}/${frontmatter.version}/changelog`}  title="View the changelog" description="Want to know the history of this service? View the change logs" />
    <Tile icon="UserGroupIcon" href="/docs/teams/full-stack" title="Contact the team" description="Any questions? Feel free to contact the owners" />
    <Tile icon="BoltIcon" href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Sends ${frontmatter.sends.length} messages`} description="This service sends messages to downstream consumers" />
    <Tile icon="BoltIcon"  href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Receives ${frontmatter.receives.length} messages`} description="This service receives messages from other services" />
</Tiles>

### Core features

| Feature | Description |
|---------|-------------|
| Subscription Management | Handles subscription creation, updates, and status tracking |
| Payment Processing | Integrates with payment gateways to handle payment transactions |
| Notification Integration | Sends notifications to users and other services |
| Multi-Channel Fulfillment | Supports multiple fulfillment channels (e.g., shipping, in-store pickup) |

## Architecture diagram 

<NodeGraph />

<MessageTable format="all" limit={4} />

## Infrastructure

The Subscription Service is hosted on AWS.

The diagram below shows the infrastructure of the Subscription Service. The service is hosted on AWS and uses AWS Lambda to handle the subscription requests. The subscription is stored in an AWS Aurora database and the subscription metadata is stored in an AWS S3 bucket.

```mermaid
architecture-beta
    group api(logos:aws)

    service db(logos:aws-aurora)[Subscription DB] in api
    service disk1(logos:aws-s3)[Subscription Metadata] in api
    service server(logos:aws-lambda)[Subscription Handler] in api

    db:L -- R:server
    disk1:T -- B:server
```

You can find more information about the Subscription Service infrastructure in the [Subscription Service documentation](https://github.com/event-catalog/pretend-subscription-service/blob/main/README.md).

<Footer />
---
id: InventoryService
version: 0.0.1
name: Inventory Service
summary: |
  Service that handles the inventory
owners:
    - dboyne
    - full-stack
    - mobile-devs
receives:
  - id: OrderConfirmed
  - id: OrderCancelled
  - id: OrderAmended
  - id: UpdateInventory
sends:
  - id: InventoryAdjusted
  - id: OutOfStock
repository:
  language: JavaScript
  url: https://github.com/event-catalog/pretend-shipping-service
---

## Overview

The Inventory Service is a critical component of the system responsible for managing product stock levels, tracking inventory movements, and ensuring product availability. It interacts with other services to maintain accurate inventory records and supports operations such as order fulfillment, restocking, and inventory audits.

## Architecture diagram

<NodeGraph title="Hello world" />
---
id: OrdersService
version: 0.0.2
name: Orders Service
summary: |
  Service that handles orders
owners:
    - dboyne
receives:
  - id: InventoryAdjusted
sends:
  - id: AddInventory  
    version: 0.0.3
repository:
  language: JavaScript
  url: https://github.com/event-catalog/pretend-shipping-service
schemaPath: "openapi.yml"
specifications:
  asyncapiPath: order-service-asyncapi.yaml
  openapiPath: openapi.yml
---

import Footer from '@catalog/components/footer.astro';

## Overview

The Orders Service is responsible for managing customer orders within the system. It handles order creation, updating, status tracking, and interactions with other services such as Inventory, Payment, and Notification services to ensure smooth order processing and fulfillment.

## Architecture diagram 

<NodeGraph />

<Footer />

 ## Raw Schema:openapi.yml

openapi: 3.1.0
info:
  title: Simple Task - API
  version: 1.0.0
  description: Simple Api
  contact: {}
  license:
    name: apache 2.0
    identifier: apache-2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html

servers:
  - url: https://example.com/
    
paths:
  /v1/task/{id}:
    put:
      summary: Do Simple Task
      operationId: DoSimpleTask
      responses:
        '200':
          description: do a task by id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
        '204':
          description: No content
        '400':
          description: Problem with data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Not Authorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unauthorized'
        '404':
          description: not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      description: Allows to do a simple task
      security:
        - authorization: []
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string

components:
  schemas:
    Task:
      properties:
        comments:
          type: string
        creationDate:
          type: string
        taskId:
          type: string
        description:
          type: string
        lastUpdate:
          type: string
      type: object
      additionalProperties: false
    Error:
      properties:
        error:
          type: string
      required:
        - error
      type: object
    Unauthorized:
      properties:
        message:
          type: string
      required:
        - message
      type: object
  securitySchemes:
    authorization:
      type: http
      scheme: bearer

---
id: E-Commerce
name: E-Commerce
version: 1.0.0
owners:
  - dboyne
  - full-stack
domains:
  - id: Orders
  - id: Payment
  - id: Subscriptions
  - id: MySubdomain
badges:
  - content: Core domain
    backgroundColor: blue
    textColor: blue
    icon: RectangleGroupIcon
  - content: Business Critical
    backgroundColor: yellow
    textColor: yellow
    icon: ShieldCheckIcon
resourceGroups:
  - id: related-resources
    title: Core FlowMart Services
    items:
      - id: InventoryService
        type: service
      - id: OrdersService
        type: service
      - id: NotificationService
        type: service
      - id: ShippingService
        type: service
      - id: CustomerService
        type: service
      - id: PaymentService
        type: service
      - id: AnalyticsService
        type: service
---

import Footer from '@catalog/components/footer.astro';

The E-Commerce domain is the core business domain of FlowMart, our modern digital marketplace. This domain orchestrates all critical business operations from product discovery to order fulfillment, handling millions of transactions monthly across our global customer base.



<Tiles>
    <Tile 
        icon="UserGroupIcon" 
        href="/docs/teams/full-stack" 
        title="Engineering Support" 
        description="Questions? Contact our full-stack team for technical support" 
    />
    <Tile 
        icon="RectangleGroupIcon" 
        href={`/visualiser/domains/${frontmatter.id}/${frontmatter.version}`} 
        title="Domain Architecture" 
        description="Explore our domain structure and service interactions" 
    />
    <Tile 
        icon="CircleStackIcon" 
        href={`#flowmart-e-commerce-database-schema`} 
        title="Database Schema" 
        description="Explore our database schema for the E-Commerce domain" 
    />
    <Tile 
        icon="RectangleGroupIcon" 
        href={`#target-architecture-event-storming-results`} 
        title="Target Architecture" 
        description="Explore our target architecture for the E-Commerce domain" 
    />
</Tiles>

## Domain Overview

The E-Commerce domain encapsulates all the core business logic for the FlowMart e-commerce platform. It is built on event-driven microservices architecture.

<NodeGraph mode="full" search="false" legend="false" />

FlowMart's E-Commerce domain is built on event-driven microservices architecture, enabling:
- Real-time inventory management across multiple warehouses
- Seamless payment processing with multiple providers
- Smart order routing and fulfillment
- Personalized customer notifications
- Subscription-based shopping experiences
- Advanced fraud detection and prevention

## Core Domains for E-Commerce

The <ResourceLink id="Orders" type="domain">Orders</ResourceLink> and <ResourceLink id="Subscriptions" type="domain">Subscription</ResourceLink> domains are core domains for the E-Commerce domain.

<span class="not-prose">They are used to manage the orders and subscriptions for the E-Commerce domain.</span>

<div class="grid grid-cols-2 gap-4 not-prose">
  <NodeGraph id="Orders" version="0.0.3" type="domain" />
  <NodeGraph id="Subscriptions" version="0.0.1" type="domain" />
</div>

The E-Commerce domain is built on the following sub domains:

- <ResourceLink id="Orders" type="domain">Orders</ResourceLink> - Core domain for order management
- <ResourceLink id="Payment" type="domain">Payment</ResourceLink> - A generic domain for payment processing using Stripe as a payment provider
- <ResourceLink id="Subscriptions" type="domain">Subscription</ResourceLink> - Generic subscription domain handling users subscriptions


### FlowMart E-Commerce Database Schema

This diagram represents the core relational data model behind FlowMart, a fictional event-driven e-commerce platform. It captures the main business entities and their relationships, including customers, orders, products, inventory events, and payments.

The schema is designed to support a distributed microservices architecture with event-sourced patterns, enabling services like OrderService, InventoryService, and PaymentService to operate independently while maintaining data consistency through asynchronous events.

```plantuml
@startuml
!define Table(name,desc) class name as "desc" << (T,#E5E7EB) >>
!define PK(x) <u>x</u>
!define FK(x) <i>x</i>

' ===== Core Tables =====

Table(Customers, "Customers") {
  PK(customerId): UUID
  firstName: VARCHAR
  lastName: VARCHAR
  email: VARCHAR
  phone: VARCHAR
  dateRegistered: TIMESTAMP
}

Table(Orders, "Orders") {
  PK(orderId): UUID
  FK(customerId): UUID
  orderDate: TIMESTAMP
  status: VARCHAR
  totalAmount: DECIMAL
}

Table(Products, "Products") {
  PK(productId): UUID
  name: VARCHAR
  description: TEXT
  price: DECIMAL
  stockQuantity: INT
}

Table(OrderItems, "Order Items") {
  PK(id): UUID
  FK(orderId): UUID
  FK(productId): UUID
  quantity: INT
  unitPrice: DECIMAL
}

Table(Payments, "Payments") {
  PK(paymentId): UUID
  FK(orderId): UUID
  amount: DECIMAL
  method: VARCHAR
  status: VARCHAR
  paidAt: TIMESTAMP
}

Table(InventoryEvents, "Inventory Events") {
  PK(eventId): UUID
  FK(productId): UUID
  eventType: VARCHAR
  quantityChange: INT
  eventTime: TIMESTAMP
}

Table(Subscription, "Subscriptions") {
  PK(subscriptionId): UUID
  FK(customerId): UUID
  plan: VARCHAR
  status: VARCHAR
  startDate: TIMESTAMP
  endDate: TIMESTAMP
}

' ===== Relationships =====

Customers ||--o{ Orders : places
Orders ||--o{ OrderItems : contains
Products ||--o{ OrderItems : includes
Orders ||--o{ Payments : paid_by
Products ||--o{ InventoryEvents : logs
Customers ||--o{ Subscription : subscribes

@enduml

```

## Target Architecture (Event Storming Results)

Our target architecture was defined through collaborative event storming sessions with product, engineering, and business stakeholders. This represents our vision for FlowMart's commerce capabilities.

<Miro boardId="uXjVIHCImos=/" moveToWidget="3074457347671667709" edit={false} />


### Order Processing Flow

```mermaid
sequenceDiagram
    participant Customer
    participant OrdersService
    participant InventoryService
    participant PaymentService
    participant NotificationService
    participant ShippingService

    Customer->>OrdersService: Place Order
    OrdersService->>InventoryService: Check Stock Availability
    InventoryService-->>OrdersService: Stock Confirmed
    OrdersService->>PaymentService: Process Payment
    PaymentService-->>OrdersService: Payment Successful
    OrdersService->>InventoryService: Reserve Inventory
    OrdersService->>ShippingService: Create Shipping Label
    ShippingService-->>OrdersService: Shipping Label Generated
    OrdersService->>NotificationService: Send Order Confirmation
    NotificationService-->>Customer: Order & Tracking Details
```

## Key Business Flows

### Subscription Management
Our subscription service powers FlowMart's popular "Subscribe & Save" feature:

<Flow id="CancelSubscription" version="latest" includeKey={false} mode="full" walkthrough={false} search={false} />

### Payment Processing
Secure, multi-provider payment processing with fraud detection:

<Flow id="PaymentFlow" version="latest" includeKey={false} />

## Core Services

These services form the backbone of FlowMart's e-commerce operations:

<ResourceGroupTable 
    id="related-resources" 
    limit={7} 
    showOwners={true} 
    description="Essential services powering our e-commerce platform" 
/>

## Performance SLAs

- Order Processing: < 2 seconds
- Payment Processing: < 3 seconds
- Inventory Updates: Real-time
- Notification Delivery: < 30 seconds

## Monitoring & Alerts

- Real-time order volume monitoring
- Payment gateway health checks
- Inventory level alerts
- Customer experience metrics
- System performance dashboards

<Footer />

---
id: Orders
name: Orders
version: 0.0.3
owners:
  - dboyne
  - full-stack
services:
  - id: InventoryService
  - id: OrdersService
  - id: NotificationService
  - id: ShippingService
badges:
  - content: Subdomain
    backgroundColor: blue
    textColor: blue
    icon: RectangleGroupIcon
entities:
  - id: Order
  - id: OrderItem
  - id: Customer
  - id: ShoppingCart
  - id: CartItem
resourceGroups:
  - id: related-resources
    title: Core resources
    items:
      - id: InventoryService
        type: service
      - id: OrdersService
        type: service
      - id: NotificationService
        type: service
      - id: ShippingService
        type: service
---

import Footer from '@catalog/components/footer.astro';



:::warning

Please ensure all services are **updated** to the latest version for compatibility and performance improvements.
:::

The Orders domain handles all operations related to customer orders, from creation to fulfillment. This documentation provides an overview of the events and services involved in the Orders domain, helping developers and stakeholders understand the event-driven architecture

<Tiles >
    <Tile icon="UserGroupIcon" href="/docs/teams/full-stack" title="Contact the team" description="Any questions? Feel free to contact the owners" />
    <Tile icon="RectangleGroupIcon" href={`/visualiser/domains/${frontmatter.id}/${frontmatter.version}`} title={`${frontmatter.services.length} services`} description="This domain contains the following services." />
</Tiles>

### Architecture for the Orders domain

<NodeGraph />

### Entity Map

This is an entity map for the Orders domain. It shows the entities and their relationships with external entities in this domain.

<EntityMap title="Orders Entity Map"/>

<MessageTable format="all" limit={4} showChannels={true} title="Messages in/out of the domain" />

### Order example (sequence diagram)

```mermaid
sequenceDiagram
    participant Customer
    participant OrdersService
    participant InventoryService
    participant NotificationService

    Customer->>OrdersService: Place Order
    OrdersService->>InventoryService: Check Inventory
    InventoryService-->>OrdersService: Inventory Available
    OrdersService->>InventoryService: Reserve Inventory
    OrdersService->>NotificationService: Send Order Confirmation
    NotificationService-->>Customer: Order Confirmation
    OrdersService->>Customer: Order Placed Successfully
    OrdersService->>InventoryService: Update Inventory
```

## Flows

### Cancel Subscription flow
Documented flow when a user cancels their subscription.

<Flow id="CancelSubscription" version="latest" includeKey={false} />

### Payment processing flow
Documented flow when a user makes a payment within the order domain

<Flow id="PaymentFlow" version="latest" includeKey={false} />

<ResourceGroupTable id="related-resources" limit={4} showOwners={true} title="Core resources for the Orders domain" description="Resources that are related to the Orders domain, you may find them useful" />

<Footer />

---
id: Payment
name: Payment
version: 0.0.1
summary: |
  Domain that contains payment related services and messages for processing financial transactions.
owners:
    - dboyne
services:
  - id: PaymentService
    version: 0.0.1
  - id: FraudDetectionService
    version: 0.0.1
  - id: PaymentGatewayService
    version: 0.0.1
entities:
  - id: Invoice
  - id: Payment
  - id: PaymentMethod
  - id: Transaction
  - id: Address
badges:
    - content: Subdomain
      backgroundColor: blue
      textColor: blue
      icon: BoltIcon
---

## Overview

The Payment Domain encompasses all services and components related to handling financial transactions within the system. It is responsible for managing payments, transactions, billing, fraud detection, and financial records. The domain ensures secure, reliable, and efficient processing of all payment-related activities.

## Services

### PaymentService
Core payment orchestration service that coordinates payment workflows and maintains payment state.

### FraudDetectionService
Analyzes transactions in real-time to detect fraudulent activity using machine learning models and rule-based systems.

### PaymentGatewayService
Manages integrations with external payment processors (Stripe, PayPal, etc.) and provides a unified interface for payment operations.

## Cross-Domain Integration

The Payment domain integrates with:

- **Subscriptions Domain**: Processes recurring payments for subscriptions
- **Orders Domain**: Handles payments for customer orders
- **Inventory Domain**: Updates based on successful payments

## Bounded context

<NodeGraph mode="full" />

<MessageTable format="all" limit={6} />

---
id: ProductCatalog
name: Product Catalog
version: 0.0.1
summary: Manages product information, categories, inventory, and customer reviews in the e-commerce system.
owners:
  - dboyne
entities:
  - id: Product
  - id: Category
  - id: Inventory
  - id: Review
services:
  - id: InventoryService
---

## Overview

The Product Catalog subdomain is responsible for managing all product-related information in the e-commerce system. This includes product details, hierarchical categorization, inventory tracking, and customer reviews.

## Core Responsibilities

### Product Management
- Maintain product information including pricing, descriptions, and specifications
- Support product variants (size, color, style)
- Handle product lifecycle (active, discontinued, draft)
- Manage product relationships and cross-selling

### Category Management  
- Organize products into hierarchical categories
- Support multi-level category structures
- Maintain category metadata and SEO information
- Handle category navigation and filtering

### Inventory Management
- Track stock levels and availability
- Manage reorder points and stock alerts  
- Handle inventory reservations and allocations
- Support warehouse and location management

### Review Management
- Collect and manage customer product reviews
- Calculate review metrics and ratings
- Moderate review content
- Support review helpfulness and responses

## Key Entities

- **Product**: Central aggregate containing all product information
- **Category**: Hierarchical product categorization system
- **Inventory**: Stock tracking and availability management  
- **Review**: Customer feedback and rating system

## Business Rules

- Products must belong to an active category
- Inventory levels affect product availability
- Reviews require verified purchases
- Category hierarchies have maximum depth limits
---
id: Subscriptions
name: Subscriptions
version: 0.0.1
summary: |
  Manages subscription lifecycle, billing cycles, and plan management for recurring revenue streams.
owners:
    - subscriptions-management
services:
    - id: BillingService
      version: 0.0.1
entities:
    - id: BillingProfile
    - id: SubscriptionPeriod
badges:
    - content: Subdomain
      backgroundColor: blue
      textColor: blue
---

## Overview

The Subscriptions Domain is responsible for managing all aspects of subscription-based services within our e-commerce platform. This includes subscription lifecycle management, recurring billing, plan management, and integration with payment systems.

## Core Capabilities

- **Subscription Lifecycle**: Create, update, pause, resume, and cancel subscriptions
- **Billing Cycles**: Manage monthly, quarterly, and annual billing cycles
- **Plan Management**: Define and manage subscription plans and pricing
- **Trial Periods**: Support free trials and promotional periods
- **Usage-based Billing**: Track and bill based on usage metrics

## Services

### BillingService
Handles billing cycle calculations, invoice generation, and payment scheduling. Coordinates with the Payment domain for processing recurring payments.


## Cross-Domain Integration

The Subscriptions domain integrates closely with:

- **Payment Domain**: For processing recurring payments and handling payment failures
- **Orders Domain**: For managing subscription-based product orders
- **Customer Domain**: For customer account and profile management

## Domain Events

Key events in the Subscriptions domain:
- `SubscriptionPaymentDue` - Triggers payment collection
- `PlanMigrationCompleted` - Subscription plan changed

## Bounded context

<NodeGraph />

<MessageTable format="all" limit={6} />
---
id: Orders
name: Orders
version: 0.0.1
summary: |
  Domain for everything shopping
owners:
    - dboyne
    - full-stack
services:
    - id: InventoryService
      version: 0.0.2
badges:
    - content: New domain
      backgroundColor: blue
      textColor: blue
---

## Overview

<NodeGraph />

---
id: Orders
name: Orders
version: 0.0.2
owners:
  - dboyne
services:
  - id: InventoryService
    version: 0.0.2
  - id: NotificationService
    version: 0.0.2
  - id: OrdersService
    version: 0.0.2
badges:
  - content: New domain
    backgroundColor: blue
    textColor: blue
---

## Overview

The Orders domain handles all operations related to customer orders, from creation to fulfillment. This documentation provides an overview of the events and services involved in the Orders domain, helping developers and stakeholders understand the event-driven architecture.

:::warning
Please ensure all services are updated to the latest version for compatibility and performance improvements.
:::

## Bounded context

<NodeGraph />

### Order example (sequence diagram)

```mermaid
sequenceDiagram
    participant Customer
    participant OrdersService
    participant InventoryService
    participant NotificationService

    Customer->>OrdersService: Place Order
    OrdersService->>InventoryService: Check Inventory
    InventoryService-->>OrdersService: Inventory Available
    OrdersService->>InventoryService: Reserve Inventory
    OrdersService->>NotificationService: Send Order Confirmation
    NotificationService-->>Customer: Order Confirmation
    OrdersService->>Customer: Order Placed Successfully
    OrdersService->>InventoryService: Update Inventory
```

 

---
id: full-stack
name: Full stackers
summary: Full stack developers based in London, UK
members:
    - dboyne
    - rthomas
    - lkim
    - lnguyen
    - kpatel
    - dkim
email: test@test.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/boyney123
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/channel/<Your Channel Id>/<Your team chat name>?groupId=<Your group Id>&tenantId=<Your tenant Id>
---

## Overview

The Full Stack Team is responsible for developing and maintaining both the front-end and back-end components of our applications. This team ensures that the user interfaces are intuitive and responsive, and that the server-side logic and database interactions are efficient and secure. The Full Stack Team handles the entire lifecycle of web applications, from initial development to deployment and ongoing maintenance.

## Responsibilities

### Key Responsibilities
- **Front-End Development**: Design and implement user interfaces using modern web technologies (e.g., HTML, CSS, JavaScript, React).
- **Back-End Development**: Develop and maintain server-side logic, APIs, and database interactions (e.g., Node.js, Express, SQL/NoSQL databases).
- **Integration**: Ensure seamless communication between the front-end and back-end components.
- **Performance Optimization**: Optimize the performance and scalability of web applications.
- **Testing and Debugging**: Write and maintain unit, integration, and end-to-end tests to ensure the quality and reliability of the applications.
- **Deployment**: Manage the deployment of applications to production environments using CI/CD pipelines.


---
id: mobile-devs
name: The mobile devs
members:
    - msmith
    - rsingh
    - jbrown
    - mwang
    - jchen
---

The Mobile Devs team is responsible for the development and maintenance of the mobile applications for our company. This includes the iOS and Android apps that customers use to interact with our services, make purchases, and manage their accounts. The team ensures that the mobile apps are user-friendly, secure, and performant.

## Responsibilities

### 1. Mobile Application Development
- **Platform Support**: Developing and maintaining apps for iOS and Android platforms.
- **Feature Implementation**: Implementing new features based on product requirements and user feedback.
- **User Interface Design**: Ensuring a consistent and intuitive user interface across all mobile platforms.
- **Performance Optimization**: Optimizing the performance of mobile apps to ensure fast and smooth user experiences.

### 2. Integration with Backend Services
- **API Integration**: Integrating mobile apps with backend services using RESTful APIs and other communication protocols.
- **Real-time Updates**: Implementing real-time data updates and synchronization with backend services.
---
id: order-management
name: The order management team
members:
    - asmith
    - mchen
    - nshah
    - slee
    - spatel
---

The order management team is responsible for overseeing and optimizing the entire order lifecycle within our organization. Their key responsibilities include:

- Processing and validating incoming customer orders
- Managing order fulfillment workflows and inventory allocation
- Coordinating with warehouse and shipping teams
- Handling order modifications and cancellations
- Resolving order-related customer issues and disputes
- Monitoring order processing metrics and KPIs
- Implementing and maintaining order management systems
- Developing strategies to improve order accuracy and efficiency

The team works closely with sales, customer service, and logistics departments to ensure smooth order processing and customer satisfaction.


---
id: subscriptions-management
name: The subscriptions management team
members:
    - tgarcia
    - alee
    - rjohnson
    - azhang
    - rjones
    - jmiller
---

The subscriptions management team is responsible for overseeing and optimizing the entire subscription lifecycle within our organization. Their key responsibilities include:

- Processing and validating incoming customer orders
- Managing order fulfillment workflows and inventory allocation
- Coordinating with warehouse and shipping teams
- Handling order modifications and cancellations
- Resolving order-related customer issues and disputes

The team works closely with sales, customer service, and logistics departments to ensure smooth order processing and customer satisfaction.
---
id: asmith
name: Amy Smith
avatarUrl: https://randomuser.me/api/portraits/women/48.jpg
role: Product owner
---

Hello! I'm Amy Smith, the Product Owner of the innovative Full Stackers team. With a strong focus on delivering exceptional value, I specialize in connecting business objectives with technical solutions to create products that users love.

### About Me

With a comprehensive background in product management and a solid understanding of software development, I bring a unique perspective to the table. My career has been driven by a passion for understanding user needs, defining clear product visions, and leading teams to successful product deliveries.

### What I Do

As the Product Owner for Full Stackers, my role involves a wide range of responsibilities aimed at ensuring our products are both high-quality and user-centric. Key aspects of my role include:

- **Product Vision & Strategy**: Defining and communicating the long-term vision and strategy for our products, ensuring alignment with the company's objectives and market demands.
- **Roadmap Planning**: Developing and maintaining a product roadmap that highlights key features and milestones, prioritizing tasks based on their business value and user feedback.
- **Stakeholder Management**: Engaging with stakeholders across the organization to gather requirements, provide updates, and ensure everyone is aligned on the product's direction.
- **User-Centric Design**: Championing the end-users by conducting user research, analyzing feedback, and ensuring our products effectively solve their problems.
- **Agile Leadership**: Leading the development process using Agile methodologies, facilitating sprint planning, and ensuring the team has clear priorities and objectives.

My mission is to deliver products that not only meet but exceed customer expectations. I thrive on the challenge of translating complex requirements into simple, intuitive solutions.

If you’re interested in product management, user experience, or discussing the latest trends in technology, feel free to reach out!


---
id: alee
name: Alice Lee
avatarUrl: https://randomuser.me/api/portraits/women/91.jpg
role: Technical Writer
---

As a Technical Writer on the Documentation team, I create clear, comprehensive documentation for our products and APIs. My focus is on making complex technical concepts accessible to developers and end-users alike. I collaborate with engineering teams to ensure our documentation stays current and accurate. 
---
id: azhang
name: Alice Zhang
avatarUrl: https://randomuser.me/api/portraits/women/97.jpg
role: Data Engineer
email: azhang@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/azhang
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=azhang@company.com
---

Building and maintaining data pipelines and infrastructure... 
---
id: dboyne
name: David Boyne
avatarUrl: "https://pbs.twimg.com/profile_images/1262283153563140096/DYRDqKg6_400x400.png"
role: Lead developer
email: test@test.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/boyney123
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=test@test.com
---

Hello! I'm David Boyne, the Tech Lead of an amazing team called Full Stackers. With a passion for building robust and scalable systems, I specialize in designing and implementing event-driven architectures that power modern, responsive applications.

### About Me

With over a decade of experience in the tech industry, I have honed my skills in full-stack development, cloud computing, and distributed systems. My journey has taken me through various roles, from software engineer to architect, and now as a tech lead, I am committed to driving innovation and excellence within my team.

### What I Do

At Full Stackers, we focus on creating seamless and efficient event-driven architectures that enhance the performance and scalability of our applications. My role involves:

- **Architecture Design**: Crafting scalable and resilient system architectures using event-driven paradigms.
- **Team Leadership**: Guiding a talented team of developers, fostering a collaborative and innovative environment.
- **Code Reviews & Mentorship**: Ensuring code quality and sharing knowledge to help the team grow.
- **Stakeholder Collaboration**: Working closely with other teams and stakeholders to align our technical solutions with business goals.
- **Continuous Improvement**: Advocating for best practices in software development, deployment, and monitoring.

I am passionate about leveraging the power of events to build systems that are not only highly responsive but also easier to maintain and extend. In an ever-evolving tech landscape, I strive to stay ahead of the curve, continuously learning and adapting to new technologies and methodologies.

Feel free to connect with me to discuss all things tech, event-driven architectures, or to exchange ideas on building better software systems!

---
*David Boyne*
*Tech Lead, Full Stackers*

---
id: dkim
name: David Kim
avatarUrl: https://randomuser.me/api/portraits/men/96.jpg
role: Performance Engineer
email: dkim@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/dkim
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=dkim@company.com
---

Optimizing application performance and user experience... 
---
id: jbrown
name: Jessica Brown
avatarUrl: https://randomuser.me/api/portraits/women/95.jpg
role: UI/UX Designer
email: jbrown@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/jbrown
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=jbrown@company.com
---

Creating intuitive and engaging user interfaces... 
---
id: jchen
name: Julia Chen
avatarUrl: https://randomuser.me/api/portraits/women/23.jpg
role: DevOps Engineer
---

As a DevOps Engineer on the Platform Engineering team, I specialize in building and maintaining our cloud infrastructure and deployment pipelines. My focus is on automating processes, improving system reliability, and ensuring smooth continuous integration and deployment (CI/CD). I work closely with development teams to streamline their workflows and implement robust monitoring and alerting solutions. 
---
id: jmiller
name: James Miller
avatarUrl: https://randomuser.me/api/portraits/men/18.jpg
role: Systems Architect
---

I'm a Systems Architect on the Infrastructure team, responsible for designing and evolving our technical architecture. My expertise includes cloud architecture, system integration, and scalability planning. I work closely with various teams to ensure our technical solutions align with business needs while maintaining technical excellence. 
---
id: kpatel
name: Kiran Patel
avatarUrl: https://randomuser.me/api/portraits/men/92.jpg
role: Cloud Architect
email: kpatel@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/kpatel
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=kpatel@company.com
---

As a Cloud Architect, I design and implement scalable cloud infrastructure solutions... 
---
id: lkim
name: Lisa Kim
avatarUrl: https://randomuser.me/api/portraits/women/89.jpg
role: Backend Engineer
---

As a Backend Engineer on the API Platform team, I design and implement 
---
id: lnguyen
name: Lily Nguyen
avatarUrl: https://randomuser.me/api/portraits/women/1.jpg
role: Frontend Developer
email: lnguyen@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/lnguyen
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=lnguyen@company.com
---

Developing responsive web applications... 
---
id: msmith
name: Martin Smith
avatarUrl: "https://randomuser.me/api/portraits/men/51.jpg"
role: Senior software engineer
---

As a Senior Mobile Developer on The Mobile Devs team, I play a key role in designing, developing, and maintaining our company’s mobile applications. My focus is on creating a seamless and intuitive user experience for our customers on both iOS and Android platforms. I work closely with cross-functional teams, including backend developers, UX/UI designers, and product managers, to deliver high-quality mobile solutions that meet business objectives and exceed user expectations.
---
id: mchen
name: Michelle Chen
avatarUrl: https://randomuser.me/api/portraits/women/93.jpg
role: Site Reliability Engineer
email: mchen@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/mchen
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=mchen@company.com
---

Specializing in maintaining system reliability and performance... 
---
id: mwang
name: Michael Wang
avatarUrl: https://randomuser.me/api/portraits/men/98.jpg
role: ML Engineer
email: mwang@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/mwang
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=mwang@company.com
---

Developing and deploying machine learning models... 
---
id: mwilson
name: Mike Wilson
avatarUrl: https://randomuser.me/api/portraits/men/77.jpg
role: QA Engineer
---

I'm a QA Engineer on the Quality Assurance team, ensuring our products meet the highest standards of quality and reliability. My focus includes automated testing, performance testing, and developing comprehensive test strategies. I work closely with development teams to implement effective testing practices throughout the development lifecycle. 
---
id: nshah
name: Nina Shah
avatarUrl: https://randomuser.me/api/portraits/women/33.jpg
role: Scrum Master
---

As a Scrum Master for the Platform team, I facilitate agile processes and help remove obstacles to team productivity. My focus is on improving team dynamics, sprint planning, and process optimization. I work closely with product owners and development teams to ensure smooth project delivery. 
---
id: rjohnson
name: Robert Johnson
avatarUrl: https://randomuser.me/api/portraits/men/32.jpg
role: UX Designer
---

I'm a UX Designer on the Design Systems team, passionate about creating intuitive and accessible user experiences. With a background in cognitive psychology and human-computer interaction, I focus on user research, wireframing, and prototyping. I collaborate closely with product teams to ensure our solutions meet both user needs and business objectives. 
---
id: rjones
name: Robert Jones
avatarUrl: https://randomuser.me/api/portraits/men/100.jpg
role: Security Analyst
email: rjones@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/rjones
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=rjones@company.com
---

Analyzing and improving system security... 
---
id: rsingh
name: Raj Singh
avatarUrl: https://randomuser.me/api/portraits/men/94.jpg
role: Mobile Developer
email: rsingh@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/rsingh
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=rsingh@company.com
---

Focused on developing cross-platform mobile applications... 
---
id: rthomas
name: Ray Thomas
avatarUrl: https://randomuser.me/api/portraits/men/62.jpg
role: Frontend Engineer
---

I'm a Frontend Engineer on the Web Platform team, specializing in building responsive and accessible web applications. My expertise includes modern JavaScript frameworks, CSS architecture, and web performance optimization. I work closely with designers and backend teams to deliver exceptional user experiences. 
---
id: slee
name: Sarah Lee
avatarUrl: https://randomuser.me/api/portraits/women/99.jpg
role: Product Manager
email: slee@company.com
slackDirectMessageUrl: https://yourteam.slack.com/channels/slee
msTeamsDirectMessageUrl: https://teams.microsoft.com/l/chat/0/0?users=slee@company.com
---

Managing product development and strategy... 
---
id: spatel
name: Sanya Patel
avatarUrl: https://randomuser.me/api/portraits/women/67.jpg
role: Data Scientist
---

As a Data Scientist on the Analytics team, I leverage machine learning and statistical analysis to derive meaningful insights from our data. My expertise includes predictive modeling, A/B testing, and developing data-driven solutions. I work closely with product and engineering teams to implement data-driven features and optimize user experiences. 
---
id: tgarcia
name: Tom Garcia
avatarUrl: https://randomuser.me/api/portraits/men/41.jpg
role: Security Engineer
---

I'm a Security Engineer on the InfoSec team, responsible for maintaining and enhancing our organization's security posture. My focus includes vulnerability assessment, security architecture review, and implementing security best practices. I work closely with development teams to ensure security is built into our products from the ground up. 
---
id: CartItem
name: CartItem
version: 1.0.0
identifier: cartItemId
summary: Represents an individual item within a shopping cart.
properties:
  - name: cartItemId
    type: UUID
    required: true
    description: Unique identifier for the cart item
  - name: cartId
    type: UUID
    required: true
    description: Shopping cart this item belongs to
    references: ShoppingCart
    referencesIdentifier: cartId
    relationType: hasOne
  - name: productId
    type: UUID
    required: true
    description: Product being added to cart
    references: Product
    referencesIdentifier: productId
    relationType: hasOne
  - name: sku
    type: string
    required: true
    description: Product SKU at time of adding to cart
  - name: productName
    type: string
    required: true
    description: Product name snapshot at time of adding to cart
  - name: productImage
    type: string
    required: false
    description: Product image URL snapshot
  - name: quantity
    type: integer
    required: true
    description: Quantity of this product in the cart
  - name: unitPrice
    type: decimal
    required: true
    description: Unit price at time of adding to cart
  - name: totalPrice
    type: decimal
    required: true
    description: Total price for this line item (quantity × unit price)
  - name: originalPrice
    type: decimal
    required: false
    description: Original product price before any discounts
  - name: discountAmount
    type: decimal
    required: false
    description: Discount applied to this line item
  - name: productVariant
    type: object
    required: false
    description: Product variant details (size, color, etc.)
    properties:
      - name: size
        type: string
        description: Product size if applicable
      - name: color
        type: string
        description: Product color if applicable
      - name: style
        type: string
        description: Product style if applicable
  - name: isAvailable
    type: boolean
    required: true
    description: Whether the product is still available
  - name: notes
    type: string
    required: false
    description: Customer notes for this item
  - name: addedAt
    type: DateTime
    required: true
    description: Date and time when item was added to cart
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when item was last updated
---

## Overview

The CartItem entity represents individual products within a customer's shopping cart. It maintains snapshots of product information and pricing to ensure consistency during the shopping session.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **ShoppingCart:** Each cart item belongs to one `ShoppingCart` (identified by `cartId`).
* **Product:** Each cart item references one `Product` (identified by `productId`).

## Price Calculations

* **Total Price** = Quantity × Unit Price - Discount Amount
* **Savings** = Original Price - Unit Price (if applicable)

## Examples

* **CartItem #1:** iPhone 15 Pro, quantity 1, $999.99 unit price, no discount.
* **CartItem #2:** Running Shoes Size 9, quantity 2, $64.99 unit price (was $129.99).
* **CartItem #3:** T-Shirt Large/Blue, quantity 3, $19.99 unit price.

## Business Rules

* Quantity must be greater than zero
* Unit price is captured at time of adding to maintain consistency
* Product availability is checked when cart is accessed
* Unavailable items are marked but not automatically removed
* Total price is recalculated when quantity changes
* Product snapshots prevent price changes from affecting active carts
* Maximum quantity limits may apply per product type
---
id: Order
name: Order
version: 1.0.0
identifier: orderId
aggregateRoot: true
summary: Represents a customer's request to purchase products or services.
properties:
  - name: orderId
    type: UUID
    required: true
    description: Unique identifier for the order
  - name: orderNumber
    type: string
    required: true
    description: Unique identifier for the order
  - name: customerId
    type: UUID
    required: false
    description: Identifier for the customer placing the order test
    references: Customer
    referencesIdentifier: customerId
    relationType: hasOne
  - name: orderDate
    type: DateTime
    required: true
    description: Date and time when the order was placed
  - name: status
    type: string
    required: true
    description: Current status of the order (e.g., Pending, Processing, Shipped, Delivered, Cancelled)
    enum: ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']
  - name: orderItems
    type: array
    items:
      type: OrderItem # Assuming an OrderItem entity exists
    required: true
    references: OrderItem
    referencesIdentifier: orderItemId
    relationType: hasMany
    description: List of items included in the order
  - name: totalAmount
    type: decimal
    required: true
    description: Total monetary value of the order
  - name: shippingAddress
    type: Address
    required: true
    description: Address where the order should be shipped
    references: Address
    referencesIdentifier: addressId
    relationType: hasOne
  - name: billingAddress
    type: Address
    required: true
    description: Address for billing purposes
    references: Address
    referencesIdentifier: addressId
    relationType: hasOne
  - name: payment
    type: Payment
    required: false
    description: Payment associated with this order
    references: Payment
    referencesIdentifier: orderId
    relationType: hasOne
  - name: convertedFromCartId
    type: UUID
    required: false
    description: Shopping cart that was converted to this order
    references: ShoppingCart
    referencesIdentifier: cartId
    relationType: hasOne
---

## Overview

The Order entity captures all details related to a customer's purchase request. It serves as the central aggregate root within the Orders domain, coordinating information about the customer, products ordered, payment, and shipping.

### Entity Properties
<EntityPropertiesTable />

## Relationships

*   **Customer:** Each order belongs to one `Customer` (identified by `customerId`).
*   **OrderItem:** An order contains one or more `OrderItem` entities detailing the specific products and quantities.
*   **Address:** Each order has shipping and billing `Address` entities (identified by `shippingAddress` and `billingAddress`).
*   **Payment:** An order is associated with one `Payment` entity for transaction processing.
*   **ShoppingCart:** An order can be converted from a `ShoppingCart` (identified by `convertedFromCartId`).
*   **Shipment:** An order may lead to one or more `Shipment` entities (not detailed here).

## Examples

*   **Order #12345:** A customer orders 2 units of Product A and 1 unit of Product B, to be shipped to their home address. Status is 'Processing'.
*   **Order #67890:** A customer places a large order for multiple items, requiring special shipping arrangements. Status is 'Pending' until payment confirmation.


---
id: Customer
name: Customer
version: 1.0.0
identifier: customerId
summary: Represents an individual or organization that places orders.

properties:
  - name: customerId
    type: UUID
    required: true
    description: Unique identifier for the customer
  - name: firstName
    type: string
    required: true
    description: Customer's first name
  - name: lastName
    type: string
    required: true
    description: Customer's last name
  - name: email
    type: string
    required: true
    description: Customer's primary email address (unique)
  - name: phone
    type: string
    required: false
    description: Customer's phone number
  - name: addresses
    type: array
    items:
      type: Address # Assuming an Address value object or entity exists
    required: false
    description: List of addresses associated with the customer (e.g., shipping, billing)
  - name: dateRegistered
    type: DateTime
    required: true
    description: Date and time when the customer registered
---
## Overview

The Customer entity holds information about the individuals or organizations who interact with the system, primarily by placing orders. It stores contact details, addresses, and other relevant personal or business information.

### Entity Properties
<EntityPropertiesTable />

## Relationships

*   **Order:** A customer can have multiple `Order` entities. The `Order` entity holds a reference (`customerId`) back to the `Customer`.
*   **Address:** A customer can have multiple associated `Address` value objects or entities.

## Examples

*   **Customer A:** Jane Doe, registered on 2023-01-15, with a primary shipping address and a billing address.
*   **Customer B:** John Smith, a long-time customer with multiple past orders.


---
id: OrderItem
name: OrderItem
version: 1.0.0
identifier: orderItemId
summary: Represents a single item within a customer's order.

properties:
  - name: orderItemId
    type: UUID
    required: true
    description: Unique identifier for the order item
  - name: orderId
    type: UUID
    required: true
    description: Identifier for the parent Order
    references: Order
    relationType: hasOne
  - name: productId
    type: UUID
    required: true
    description: Identifier for the product being ordered
    references: Product
    referencesIdentifier: productId
    relationType: hasOne 
  - name: productName
    type: string
    required: false # Often denormalized for performance/display
    description: Name of the product at the time of order
  - name: quantity
    type: integer
    required: true
    description: Number of units of the product ordered
  - name: unitPrice
    type: decimal
    required: true
    description: Price per unit of the product at the time of order
  - name: totalPrice
    type: decimal
    required: true
    description: Total price for this item line (quantity * unitPrice)
---

## Overview

The OrderItem entity details a specific product and its quantity requested within an `Order`. It holds information about the product, the quantity ordered, and the price calculation for that line item. OrderItems are part of the `Order` aggregate.

### Entity Properties
<EntityPropertiesTable />

## Relationships

*   **Order:** Each `OrderItem` belongs to exactly one `Order` (identified by `orderId`). It is a constituent part of the Order aggregate.
*   **Product:** Each `OrderItem` refers to one `Product` (identified by `productId`).

## Examples

*   **OrderItem A (for Order #12345):** Product ID: P001, Quantity: 2, Unit Price: $50.00, Total Price: $100.00
*   **OrderItem B (for Order #12345):** Product ID: P002, Quantity: 1, Unit Price: $75.00, Total Price: $75.00

---
id: ShoppingCart
name: ShoppingCart
version: 1.0.0
identifier: cartId
aggregateRoot: true
summary: Represents a customer's shopping cart containing products before checkout.
properties:
  - name: cartId
    type: UUID
    required: true
    description: Unique identifier for the shopping cart
  - name: customerId
    type: UUID
    required: false
    description: Customer who owns this cart (null for guest carts)
    references: Customer
    referencesIdentifier: customerId
    relationType: hasOne
  - name: sessionId
    type: string
    required: false
    description: Session identifier for guest carts
  - name: status
    type: string
    required: true
    description: Current status of the cart
    enum: ['active', 'abandoned', 'converted', 'expired']
  - name: cartItems
    type: array
    items:
      type: CartItem
    required: false
    description: Items in the shopping cart
    references: CartItem
    referencesIdentifier: cartId
    relationType: hasMany
  - name: subtotal
    type: decimal
    required: true
    description: Subtotal amount before taxes and shipping
  - name: taxAmount
    type: decimal
    required: false
    description: Calculated tax amount
  - name: shippingAmount
    type: decimal
    required: false
    description: Calculated shipping amount
  - name: discountAmount
    type: decimal
    required: false
    description: Total discount amount applied
  - name: totalAmount
    type: decimal
    required: true
    description: Final total amount including taxes and shipping
  - name: currency
    type: string
    required: true
    description: Currency code for all amounts
  - name: appliedCoupons
    type: array
    items:
      type: string
    required: false
    description: Coupon codes applied to this cart
  - name: shippingAddress
    type: Address
    required: false
    description: Selected shipping address
    references: Address
    referencesIdentifier: addressId
    relationType: hasOne
  - name: billingAddress
    type: Address
    required: false
    description: Selected billing address
    references: Address
    referencesIdentifier: addressId
    relationType: hasOne
  - name: notes
    type: string
    required: false
    description: Customer notes or special instructions
  - name: abandonedAt
    type: DateTime
    required: false
    description: Date and time when cart was abandoned
  - name: convertedToOrderId
    type: UUID
    required: false
    description: Order ID if cart was successfully converted
    references: Order
    referencesIdentifier: orderId
    relationType: hasOne
  - name: expiresAt
    type: DateTime
    required: false
    description: Date and time when cart expires
  - name: createdAt
    type: DateTime
    required: true
    description: Date and time when the cart was created
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when the cart was last updated
---

## Overview

The ShoppingCart entity manages the customer's shopping experience before checkout. It tracks selected products, quantities, pricing, and supports both registered customer and guest shopping scenarios.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **Customer:** A cart can belong to one `Customer` (identified by `customerId`).
* **CartItem:** A cart contains multiple `CartItem` entities with product details.
* **Address:** A cart can reference shipping and billing `Address` entities.
* **Order:** A cart can be converted to one `Order` (identified by `convertedToOrderId`).

## Cart States

```
active → abandoned
   ↓       ↓
converted  expired
```

## Examples

* **Cart #1:** Customer cart with 3 items, $299.99 total, active status.
* **Cart #2:** Guest cart abandoned after 24 hours, contains 1 high-value item.
* **Cart #3:** Converted cart that became Order #12345, marked as converted.

## Business Rules

* Guest carts are identified by session ID when customer ID is null
* Cart totals are recalculated when items are added/removed
* Abandoned carts trigger marketing automation after configured time
* Expired carts are cleaned up after retention period
* Cart conversion creates an order and marks cart as converted
* Inventory is not reserved until checkout begins
* Applied coupons are validated on each cart update
* Cart items maintain snapshot of product prices at time of addition
---
id: Address
name: Address
version: 1.0.0
identifier: addressId
summary: Represents shipping and billing addresses for customers and orders.
properties:
  - name: addressId
    type: UUID
    required: true
    description: Unique identifier for the address
  - name: customerId
    type: UUID
    required: false
    description: Customer this address belongs to
    references: Customer
    referencesIdentifier: customerId
    relationType: hasOne
  - name: type
    type: string
    required: true
    description: Type of address
    enum: ['billing', 'shipping', 'both']
  - name: firstName
    type: string
    required: true
    description: First name of the recipient
  - name: lastName
    type: string
    required: true
    description: Last name of the recipient
  - name: company
    type: string
    required: false
    description: Company name if applicable
  - name: addressLine1
    type: string
    required: true
    description: Primary address line (street address)
  - name: addressLine2
    type: string
    required: false
    description: Secondary address line (apartment, suite, etc.)
  - name: city
    type: string
    required: true
    description: City name
  - name: state
    type: string
    required: true
    description: State or province
  - name: postalCode
    type: string
    required: true
    description: Postal or ZIP code
  - name: country
    type: string
    required: true
    description: Country code (ISO 3166-1 alpha-2)
  - name: phone
    type: string
    required: false
    description: Phone number for delivery contact
  - name: isDefault
    type: boolean
    required: true
    description: Whether this is the default address for the customer
  - name: isValidated
    type: boolean
    required: true
    description: Whether the address has been validated
  - name: validationDetails
    type: object
    required: false
    description: Address validation details
    properties:
      - name: validatedAt
        type: DateTime
        description: When the address was validated
      - name: validationService
        type: string
        description: Service used for validation
      - name: confidence
        type: decimal
        description: Validation confidence score
  - name: geocoordinates
    type: object
    required: false
    description: Geographic coordinates for the address
    properties:
      - name: latitude
        type: decimal
        description: Latitude coordinate
      - name: longitude
        type: decimal
        description: Longitude coordinate
  - name: deliveryInstructions
    type: string
    required: false
    description: Special delivery instructions
  - name: orders
    type: array
    items:
      type: Order
    required: false
    description: Orders using this address
    references: Order
    referencesIdentifier: shippingAddress
    relationType: hasMany
  - name: payments
    type: array
    items:
      type: Payment
    required: false
    description: Payments using this as billing address
    references: Payment
    referencesIdentifier: billingAddress
    relationType: hasMany
  - name: createdAt
    type: DateTime
    required: true
    description: Date and time when the address was created
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when the address was last updated
---

## Overview

The Address entity stores shipping and billing addresses for customers, orders, and payments. It supports address validation, geocoding, and delivery instructions to ensure accurate order fulfillment.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **Customer:** An address can belong to one `Customer` (identified by `customerId`).
* **Order:** An address can be used by multiple `Order` entities for shipping.
* **Payment:** An address can be used by multiple `Payment` entities for billing.

## Address Types

* **Billing:** Used for payment processing and invoicing
* **Shipping:** Used for order delivery
* **Both:** Can be used for both billing and shipping

## Examples

* **Address #1:** John Doe's home address - default shipping and billing address.
* **Address #2:** Corporate office address - billing only, validated with high confidence.
* **Address #3:** Gift recipient address - shipping only, with special delivery instructions.

## Business Rules

* Each customer can have only one default address per type
* Addresses must be validated before being marked as default
* International addresses require country-specific validation
* Geocoordinates are automatically populated when available
* Address changes should create new versions for audit trail
* PO Box addresses may have shipping restrictions
* Address validation improves delivery success rates
---
id: Invoice
name: Invoice
version: 1.0.0
identifier: invoiceId
summary: Represents a bill issued to a customer, detailing charges for products or services.

properties:
  - name: invoiceId
    type: UUID
    required: true
    description: Unique identifier for the invoice.
  - name: customerId
    type: UUID
    required: true
    description: Identifier of the customer being invoiced
    references: Customer
    relationType: hasOne
  - name: orderId # Optional, if invoice is directly tied to a single order
    type: UUID
    required: false
    description: Identifier of the associated order, if applicable.
  - name: subscriptionId # Optional, if invoice is for a subscription period
    type: UUID
    required: false
    description: Identifier of the associated subscription, if applicable.
  - name: invoiceNumber
    type: string
    required: true
    description: Human-readable, sequential identifier for the invoice (may have specific format).
  - name: issueDate
    type: Date
    required: true
    description: Date the invoice was generated and issued.
  - name: dueDate
    type: Date
    required: true
    description: Date by which the payment for the invoice is due.
  - name: totalAmount
    type: decimal
    required: true
    description: The total amount due on the invoice.
  - name: currency
    type: string # ISO 4217 code
    required: true
    description: Currency of the invoice amount.
  - name: status
    type: string # (e.g., Draft, Sent, Paid, Overdue, Void)
    required: true
    description: Current status of the invoice.
  - name: billingAddressId # Address used for this specific invoice
    type: UUID
    required: true
    description: Identifier for the billing address used on this invoice.
  - name: lineItems
    type: array
    items:
      type: InvoiceLineItem # Assuming a value object or separate entity for line items
    required: true
    description: List of individual items or services being charged on the invoice.
  - name: createdAt
    type: DateTime
    required: true
    description: Timestamp when the invoice record was created.
  - name: paidAt # Timestamp when payment was confirmed
    type: DateTime
    required: false
    description: Timestamp when the invoice was marked as paid.
---

## Overview

The Invoice entity represents a formal request for payment issued by the business to a customer. It details the products, services, quantities, prices, taxes, and total amount due, along with payment terms.

### Entity Properties
<EntityPropertiesTable />

## Relationships

*   **Customer:** An invoice is issued to one `Customer`.
*   **Order/Subscription:** An invoice may be related to one or more `Order`s or a specific `Subscription` period.
*   **Payment:** An invoice is settled by one or more `Payment` transactions.
*   **InvoiceLineItem:** An invoice contains multiple `InvoiceLineItem`s detailing the charges.
*   **BillingProfile:** Invoice generation often uses details from the customer's `BillingProfile`.

## Examples

*   Invoice #INV-00123 issued to Jane Doe for her monthly subscription renewal, due in 15 days.
*   Invoice #INV-00124 issued to Acme Corp for consulting services rendered in the previous month, status Paid. 
---
id: Payment
name: Payment
version: 1.0.0
identifier: paymentId
aggregateRoot: true
summary: Represents payment transactions for orders in the e-commerce system.
properties:
  - name: paymentId
    type: UUID
    required: true
    description: Unique identifier for the payment
  - name: orderId
    type: UUID
    required: true
    description: Order this payment is associated with
    references: Order
    referencesIdentifier: orderId
    relationType: hasOne
  - name: customerId
    type: UUID
    required: true
    description: Customer who made the payment
    references: Customer
    referencesIdentifier: customerId
    relationType: hasOne
  - name: amount
    type: decimal
    required: true
    description: Payment amount
  - name: currency
    type: string
    required: true
    description: Currency code (e.g., USD, EUR, GBP)
  - name: paymentMethod
    type: string
    required: true
    description: Payment method used
    enum: ['credit_card', 'debit_card', 'paypal', 'stripe', 'bank_transfer', 'apple_pay', 'google_pay']
  - name: paymentMethodDetails
    type: object
    required: false
    description: Additional payment method specific details
    properties:
      - name: cardLast4
        type: string
        description: Last 4 digits of card number
      - name: cardType
        type: string
        description: Card type (Visa, MasterCard, etc.)
      - name: expiryMonth
        type: integer
        description: Card expiry month
      - name: expiryYear
        type: integer
        description: Card expiry year
  - name: status
    type: string
    required: true
    description: Current payment status
    enum: ['pending', 'processing', 'completed', 'failed', 'cancelled', 'refunded', 'partially_refunded']
  - name: transactionId
    type: string
    required: false
    description: External payment processor transaction ID
  - name: gatewayResponse
    type: object
    required: false
    description: Raw response from payment gateway
  - name: billingAddress
    type: Address
    required: true
    description: Billing address for the payment
    references: Address
    referencesIdentifier: addressId
    relationType: hasOne
  - name: processedAt
    type: DateTime
    required: false
    description: Date and time when payment was processed
  - name: failureReason
    type: string
    required: false
    description: Reason for payment failure if applicable
  - name: refunds
    type: array
    items:
      type: PaymentRefund
    required: false
    description: Refunds associated with this payment
    references: PaymentRefund
    referencesIdentifier: paymentId
    relationType: hasMany
  - name: createdAt
    type: DateTime
    required: true
    description: Date and time when the payment record was created
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when the payment record was last updated
---

## Overview

The Payment entity manages all payment transactions in the e-commerce system. It tracks payment details, status, and relationships with orders and customers, supporting various payment methods and refund scenarios.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **Order:** Each payment belongs to one `Order` (identified by `orderId`).
* **Customer:** Each payment is made by one `Customer` (identified by `customerId`).
* **Address:** Each payment has a billing `Address` (identified by `billingAddress`).
* **PaymentRefund:** A payment can have multiple `PaymentRefund` entities for partial or full refunds.

## Payment States

```
pending → processing → completed
    ↓         ↓           ↓
cancelled  failed    refunded/partially_refunded
```

## Examples

* **Payment #1:** $299.99 credit card payment for Order #12345, completed successfully.
* **Payment #2:** $150.00 PayPal payment for Order #67890, failed due to insufficient funds.
* **Payment #3:** $500.00 bank transfer, completed with $50.00 partial refund.

## Business Rules

* Payment amount must match the order total
* Payment status transitions must follow valid state machine
* Failed payments should include failure reason
* Completed payments cannot be cancelled
* Refunds cannot exceed the original payment amount
* Payment method details are encrypted and PCI compliant
* Transaction IDs from payment gateways must be stored for reconciliation
---
id: PaymentMethod
name: PaymentMethod
version: 1.0.0
identifier: paymentMethodId
summary: Represents a payment instrument a customer can use, like a credit card or bank account.

properties:
  - name: paymentMethodId
    type: UUID
    required: true
    description: Unique identifier for the payment method.
  - name: customerId
    type: UUID
    required: true
    description: Identifier of the customer who owns this payment method.
    references: Customer
    relationType: hasOne
  - name: type
    type: string # (e.g., CreditCard, BankAccount, PayPal, ApplePay)
    required: true
    description: The type of payment method.
  - name: details # Contains type-specific details (masked, tokenized)
    type: object
    required: true
    description: Contains type-specific, often sensitive details (e.g., last 4 digits of card, card brand, bank name, account type, token). **Never store raw PANs or sensitive data.**
    # Example structure for CreditCard:
    # details:
    #   brand: "Visa"
    #   last4: "1234"
    #   expiryMonth: 12
    #   expiryYear: 2025
    #   cardholderName: "Jane Doe"
    #   gatewayToken: "tok_abc123xyz"
  - name: isDefault
    type: boolean
    required: true
    description: Indicates if this is the customer's default payment method.
  - name: billingAddressId # Link to the billing address associated with this method
    type: UUID
    required: true
    description: Identifier for the billing address verified for this payment method.
  - name: status
    type: string # (e.g., Active, Expired, Invalid, Removed)
    required: true
    description: Current status of the payment method.
  - name: createdAt
    type: DateTime
    required: true
    description: Timestamp when the payment method was added.
  - name: updatedAt
    type: DateTime
    required: true
    description: Timestamp when the payment method was last updated.
---

## Overview

The PaymentMethod entity represents a specific payment instrument registered by a customer, such as a credit card or a linked bank account. It stores necessary (non-sensitive) details required to initiate payments and links to the associated customer and billing address.

**Security Note:** Sensitive details like full card numbers or bank account numbers should **never** be stored directly. Rely on tokenization provided by payment gateways.

### Entity Properties
<EntityPropertiesTable />

## Relationships

*   **Customer:** A payment method belongs to one `Customer`.
*   **Address:** Linked to a specific billing `Address`.
*   **Payment:** Used to make `Payment` transactions.
*   **Subscription:** May be designated as the payment method for a `Subscription`.

## Examples

*   Jane Doe's default Visa card ending in 1234, expiring 12/2025, status Active.
*   John Smith's linked bank account (Chase, Checking), status Active.
*   An old MasterCard ending in 5678 belonging to Jane Doe, status Expired. 
---
id: PaymentRefunded
name: PaymentRefunded
version: 1.0.0
identifier: refundId
aggregateRoot: true
summary: Represents refunded payment transactions for orders in the e-commerce system.
properties:
  - name: refundId
    type: UUID
    required: true
    description: Unique identifier for the refund
  - name: paymentId
    type: UUID
    required: true
    description: Payment this refund is associated with
    references: Payment
    referencesIdentifier: paymentId
    relationType: hasOne
  - name: amount
    type: decimal
    required: true
    description: Refund amount
  - name: currency
    type: string
    required: true
    description: Currency code (e.g., USD, EUR, GBP)
  - name: status
    type: string
    required: true
    description: Current refund status
    enum: ['pending', 'processing', 'completed', 'failed', 'cancelled']
  - name: processedAt
    type: DateTime
    required: false
    description: Date and time when refund was processed
  - name: failureReason
    type: string
    required: false
    description: Reason for refund failure if applicable
  - name: createdAt
    type: DateTime
    required: true
    description: Date and time when the refund record was created
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when the refund record was last updated
---

## Overview

The PaymentRefunded entity manages all refund transactions in the e-commerce system. It tracks refund details, status, and relationships with payments, supporting various refund scenarios.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **Payment:** Each refund belongs to one `Payment` (identified by `paymentId`).

## Refund States

```
pending → processing → completed
    ↓         ↓           ↓
cancelled  failed
```

## Examples

* **Refund #1:** $50.00 refund for Payment #12345, completed successfully.
* **Refund #2:** $20.00 refund for Payment #67890, failed due to processing error.

## Business Rules

* Refund amount cannot exceed the original payment amount
* Refund status transitions must follow valid state machine
* Failed refunds should include failure reason
* Completed refunds cannot be cancelled
---
id: Transaction
name: Transaction
version: 1.0.0
identifier: transactionId
summary: Represents a low-level interaction with a payment gateway or processor (e.g., authorize, capture, refund, void).

properties:
  - name: transactionId
    type: UUID
    required: true
    description: Unique identifier for this specific gateway transaction.
  - name: paymentId
    type: UUID
    required: true
    references: Payment
    relationType: hasOne
    description: Identifier of the parent Payment this transaction belongs to.
  - name: type
    type: string # (e.g., Authorize, Capture, Sale, Refund, Void, Verify)
    required: true
    description: The type of operation performed with the payment gateway.
  - name: gatewayReferenceId
    type: string
    required: true
    description: Unique transaction ID provided by the external payment gateway.
  - name: amount
    type: decimal
    required: true
    description: The amount associated with this specific transaction operation.
  - name: currency
    type: string # ISO 4217 code
    required: true
    description: Currency of the transaction amount.
  - name: status
    type: string # (e.g., Success, Failure, Pending)
    required: true
    description: Status reported by the gateway for this specific operation.
  - name: responseCode # Gateway-specific code
    type: string
    required: false
    description: Response code returned by the payment gateway.
  - name: responseMessage # Gateway-specific message
    type: string
    required: false
    description: Detailed message or reason returned by the gateway.
  - name: processedAt
    type: DateTime
    required: true
    description: Timestamp when the transaction was processed by the gateway.
  - name: rawRequest # Optional, for debugging - consider security implications
    type: text
    required: false
    description: Raw request payload sent to the gateway (use with caution).
  - name: rawResponse # Optional, for debugging - consider security implications
    type: text
    required: false
    description: Raw response payload received from the gateway (use with caution).
---

## Overview

The Transaction entity logs the individual interactions with an external payment processor (like Stripe, PayPal, Adyen) that occur as part of processing a `Payment`. This provides a detailed audit trail of gateway operations, including authorizations, captures, refunds, and any associated success or failure responses.

### Entity Properties
<EntityPropertiesTable />

## Relationships

*   **Payment:** A transaction is part of one `Payment`.

## Examples

*   **Authorization Success:** Type: Authorize, PaymentID: PAY-98765, GatewayRef: auth_abc, Amount: $19.99, Status: Success.
*   **Capture Success:** Type: Capture, PaymentID: PAY-98765, GatewayRef: ch_def, Amount: $19.99, Status: Success (following the authorization).
*   **Authorization Failure:** Type: Authorize, PaymentID: PAY-98766, GatewayRef: auth_ghi, Amount: $50.00, Status: Failure, ResponseCode: 'declined', ResponseMessage: 'Insufficient Funds'.
*   **Refund Success:** Type: Refund, PaymentID: PAY-98760, GatewayRef: re_jkl, Amount: $25.00, Status: Success. 
---
id: Category
name: Category
version: 1.0.0
identifier: categoryId
aggregateRoot: true
summary: Represents a product category with hierarchical structure support.
properties:
  - name: categoryId
    type: UUID
    required: true
    description: Unique identifier for the category
  - name: name
    type: string
    required: true
    description: Name of the category
  - name: description
    type: string
    required: false
    description: Description of the category
  - name: slug
    type: string
    required: true
    description: URL-friendly identifier for the category
  - name: parentCategoryId
    type: UUID
    required: false
    description: Parent category for hierarchical structure
    references: Category
    referencesIdentifier: categoryId
    relationType: hasOne
  - name: childCategories
    type: array
    items:
      type: Category
    required: false
    description: Subcategories under this category
    references: Category
    referencesIdentifier: parentCategoryId
    relationType: hasMany
  - name: level
    type: integer
    required: true
    description: Depth level in the category hierarchy (0 = root)
  - name: isActive
    type: boolean
    required: true
    description: Whether the category is currently active
  - name: sortOrder
    type: integer
    required: false
    description: Display order within the same level
  - name: icon
    type: string
    required: false
    description: Icon URL or identifier for the category
  - name: imageUrl
    type: string
    required: false
    description: Category banner or thumbnail image
  - name: seoTitle
    type: string
    required: false
    description: SEO-optimized title for the category page
  - name: seoDescription
    type: string
    required: false
    description: SEO meta description for the category page
  - name: products
    type: array
    items:
      type: Product
    required: false
    description: Products belonging to this category
    references: Product
    referencesIdentifier: categoryId
    relationType: hasMany
  - name: createdAt
    type: DateTime
    required: true
    description: Date and time when the category was created
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when the category was last updated
---

## Overview

The Category entity organizes products into a hierarchical structure, supporting multi-level categorization. It enables efficient product discovery and navigation through the e-commerce catalog.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **Parent Category:** Each category can have one parent `Category` (identified by `parentCategoryId`).
* **Child Categories:** A category can have multiple child `Category` entities creating a hierarchy.
* **Products:** A category contains multiple `Product` entities (identified by `categoryId`).

## Hierarchy Examples

```
Electronics (Level 0)
├── Computers (Level 1)
│   ├── Laptops (Level 2)
│   ├── Desktops (Level 2)
│   └── Tablets (Level 2)
├── Mobile Phones (Level 1)
│   ├── Smartphones (Level 2)
│   └── Feature Phones (Level 2)
└── Audio (Level 1)
    ├── Headphones (Level 2)
    └── Speakers (Level 2)
```

## Business Rules

* Root categories have `parentCategoryId` as null and `level` as 0
* Child categories must have a valid `parentCategoryId`
* Category slugs must be unique across the entire catalog
* Categories cannot be deleted if they contain products or subcategories
* Inactive categories should hide all associated products from public view
* Maximum hierarchy depth should be limited (e.g., 5 levels)
---
id: Inventory
name: Inventory
version: 1.0.0
identifier: inventoryId
summary: Tracks stock levels and availability for products.
properties:
  - name: inventoryId
    type: UUID
    required: true
    description: Unique identifier for the inventory record
  - name: productId
    type: UUID
    required: true
    description: Product this inventory record tracks
    references: Product
    referencesIdentifier: productId
    relationType: hasOne
  - name: sku
    type: string
    required: true
    description: Stock Keeping Unit matching the product SKU
  - name: quantityOnHand
    type: integer
    required: true
    description: Current available stock quantity
  - name: quantityReserved
    type: integer
    required: true
    description: Quantity reserved for pending orders
  - name: quantityAvailable
    type: integer
    required: true
    description: Calculated available quantity (onHand - reserved)
  - name: minimumStockLevel
    type: integer
    required: true
    description: Minimum stock level before reorder alert
  - name: maximumStockLevel
    type: integer
    required: false
    description: Maximum stock level for inventory management
  - name: reorderPoint
    type: integer
    required: true
    description: Stock level that triggers reorder process
  - name: reorderQuantity
    type: integer
    required: true
    description: Quantity to order when restocking
  - name: unitCost
    type: decimal
    required: false
    description: Cost per unit for inventory valuation
  - name: warehouseLocation
    type: string
    required: false
    description: Physical location or bin where item is stored
  - name: lastRestockedAt
    type: DateTime
    required: false
    description: Date and time of last restock
  - name: lastSoldAt
    type: DateTime
    required: false
    description: Date and time of last sale
  - name: isTrackingEnabled
    type: boolean
    required: true
    description: Whether inventory tracking is enabled for this product
  - name: backorderAllowed
    type: boolean
    required: true
    description: Whether backorders are allowed when out of stock
  - name: createdAt
    type: DateTime
    required: true
    description: Date and time when the inventory record was created
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when the inventory record was last updated
---

## Overview

The Inventory entity manages stock levels and availability for products in the e-commerce system. It tracks current quantities, reserved stock, and provides reorder management capabilities.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **Product:** Each inventory record belongs to one `Product` (identified by `productId`).
* **OrderItem:** Inventory quantities are affected by `OrderItem` entities when orders are placed.

## Stock Calculations

* **Available Quantity** = Quantity On Hand - Quantity Reserved
* **Reorder Needed** = Quantity Available &lt;= Reorder Point
* **Stock Value** = Quantity On Hand × Unit Cost

## Examples

* **Inventory #1:** iPhone 15 Pro - 25 on hand, 5 reserved, 20 available, reorder at 10 units.
* **Inventory #2:** Running Shoes Size 9 - 0 on hand, 2 reserved, backorder allowed.

## Business Rules

* Quantity on hand cannot be negative
* Quantity reserved cannot exceed quantity on hand
* Available quantity is automatically calculated
* Reorder alerts are triggered when available = reorder point
* Stock reservations are created when orders are placed
* Stock is decremented when orders are shipped
* Inventory adjustments must be logged for audit trail
---
id: Product
name: Product
version: 1.0.0
identifier: productId
aggregateRoot: true
summary: Represents a product or service available for purchase in the e-commerce system.
properties:
  - name: productId
    type: UUID
    required: true
    description: Unique identifier for the product
  - name: name
    type: string
    required: true
    description: Name of the product
  - name: description
    type: string
    required: false
    description: Detailed description of the product
  - name: sku
    type: string
    required: true
    description: Stock Keeping Unit - unique product identifier
  - name: price
    type: decimal
    required: true
    description: Current selling price of the product
  - name: categoryId
    type: UUID
    required: true
    description: Category this product belongs to
    references: Category
    referencesIdentifier: categoryId
    relationType: hasOne
  - name: brand
    type: string
    required: false
    description: Brand name of the product
  - name: weight
    type: decimal
    required: false
    description: Weight of the product in kilograms
  - name: dimensions
    type: object
    required: false
    description: Product dimensions (length, width, height)
    properties:
      - name: length
        type: decimal
      - name: width
        type: decimal
      - name: height
        type: decimal
  - name: isActive
    type: boolean
    required: true
    description: Whether the product is currently available for sale
  - name: createdAt
    type: DateTime
    required: true
    description: Date and time when the product was created
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when the product was last updated
  - name: images
    type: array
    items:
      type: string
    required: false
    description: URLs of product images
  - name: inventory
    type: Inventory
    required: false
    description: Inventory information for this product
    references: Inventory
    referencesIdentifier: productId
    relationType: hasOne
  - name: reviews
    type: array
    items:
      type: Review
    required: false
    description: Customer reviews for this product
    references: Review
    referencesIdentifier: productId
    relationType: hasMany
---

## Overview

The Product entity represents items or services available for purchase in the e-commerce system. It serves as an aggregate root containing all product-related information including pricing, categorization, inventory details, and customer reviews.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **Category:** Each product belongs to one `Category` (identified by `categoryId`).
* **Inventory:** Each product has one `Inventory` record tracking stock levels.
* **Review:** A product can have multiple `Review` entities from customers.
* **OrderItem:** Products are referenced in `OrderItem` entities when included in orders.

## Examples

* **Product #1:** "iPhone 15 Pro" - Electronics category, $999.99, with 50 units in stock and 4.5-star reviews.
* **Product #2:** "Running Shoes" - Sports category, $129.99, various sizes available, with detailed size chart.

## Business Rules

* Products must have a unique SKU across the entire catalog
* Products cannot be deleted if they have associated order items
* Price changes should be tracked for audit purposes
* Products must belong to an active category to be purchasable
---
id: Review
name: Review
version: 1.0.0
identifier: reviewId
summary: Represents customer reviews and ratings for products.
properties:
  - name: reviewId
    type: UUID
    required: true
    description: Unique identifier for the review
  - name: productId
    type: UUID
    required: true
    description: Product being reviewed
    references: Product
    referencesIdentifier: productId
    relationType: hasOne
  - name: customerId
    type: UUID
    required: true
    description: Customer who wrote the review
    references: Customer
    referencesIdentifier: customerId
    relationType: hasOne
  - name: orderId
    type: UUID
    required: false
    description: Order associated with this review (for verified purchases)
    references: Order
    referencesIdentifier: orderId
    relationType: hasOne
  - name: rating
    type: integer
    required: true
    description: Rating given by customer (1-5 stars)
    minimum: 1
    maximum: 5
  - name: title
    type: string
    required: false
    description: Review title or headline
  - name: content
    type: string
    required: true
    description: Review content and comments
  - name: isVerifiedPurchase
    type: boolean
    required: true
    description: Whether this review is from a verified purchase
  - name: isRecommended
    type: boolean
    required: false
    description: Whether customer recommends this product
  - name: helpfulVotes
    type: integer
    required: true
    description: Number of helpful votes received
  - name: totalVotes
    type: integer
    required: true
    description: Total number of votes received
  - name: status
    type: string
    required: true
    description: Current review status
    enum: ['pending', 'approved', 'rejected', 'flagged']
  - name: moderationNotes
    type: string
    required: false
    description: Internal moderation notes
  - name: images
    type: array
    items:
      type: string
    required: false
    description: URLs of images uploaded with the review
  - name: pros
    type: array
    items:
      type: string
    required: false
    description: List of positive aspects mentioned
  - name: cons
    type: array
    items:
      type: string
    required: false
    description: List of negative aspects mentioned
  - name: merchantResponse
    type: object
    required: false
    description: Response from merchant to this review
    properties:
      - name: content
        type: string
        description: Merchant response content
      - name: respondedAt
        type: DateTime
        description: When merchant responded
      - name: respondedBy
        type: string
        description: Who responded for the merchant
  - name: createdAt
    type: DateTime
    required: true
    description: Date and time when the review was created
  - name: updatedAt
    type: DateTime
    required: false
    description: Date and time when the review was last updated
  - name: moderatedAt
    type: DateTime
    required: false
    description: Date and time when the review was moderated
---

## Overview

The Review entity captures customer feedback and ratings for products. It supports verified purchase validation, content moderation, community voting, and merchant responses to build trust and provide valuable product insights.

### Entity Properties
<EntityPropertiesTable />

## Relationships

* **Product:** Each review belongs to one `Product` (identified by `productId`).
* **Customer:** Each review is written by one `Customer` (identified by `customerId`).
* **Order:** Each review can be linked to one `Order` for purchase verification (identified by `orderId`).

## Review Lifecycle

```
submitted → pending → approved → published
              ↓         ↓
           rejected   flagged
```

## Examples

* **Review #1:** 5-star review for iPhone 15 Pro, verified purchase, "Excellent camera quality!"
* **Review #2:** 3-star review for Running Shoes, helpful votes: 15/20, includes photos
* **Review #3:** 1-star review flagged for inappropriate content, pending moderation

## Business Rules

* Reviews can only be submitted by customers who purchased the product
* Rating must be between 1-5 stars
* Verified purchase reviews are given higher weight in calculations
* Inappropriate content is flagged and requires moderation
* Customers can only review the same product once per purchase
* Helpful votes help surface most valuable reviews
* Merchant responses are limited to one per review
* Reviews older than 2 years may have reduced weight in calculations
---
id: BillingProfile
name: BillingProfile
version: 1.0.0
identifier: billingProfileId
summary: Stores billing-related contact information and preferences for a customer, often used for invoices and communication.

properties:
  - name: billingProfileId
    type: UUID
    required: true
    description: Unique identifier for the billing profile.
  - name: customerId
    type: UUID
    required: true
    description: Identifier of the customer this billing profile belongs to.
    references: Customer
    referencesIdentifier: customerId
    relationType: hasOne
  - name: billingEmail
    type: string
    required: false # May default to customer's primary email
    description: Specific email address for sending invoices and billing notifications
  - name: companyName # Optional, for B2B
    type: string
    required: false
    description: Company name for billing purposes.
  - name: taxId # Optional, for B2B or specific regions
    type: string
    required: false
    description: Tax identification number (e.g., VAT ID, EIN).
  - name: billingAddressId
    type: UUID
    required: true
    description: Identifier for the primary billing address associated with this profile.
  - name: preferredPaymentMethodId # Optional default for invoices/subscriptions
    type: UUID
    required: false
    description: Customer's preferred payment method for charges related to this profile.
  - name: createdAt
    type: DateTime
    required: true
    description: Timestamp when the billing profile was created.
  - name: updatedAt
    type: DateTime
    required: true
    description: Timestamp when the billing profile was last updated.
---

## Overview

The BillingProfile entity consolidates billing-specific details for a customer, such as the billing address, contact email for invoices, tax information, and potentially preferred payment methods. This might be distinct from the customer's general contact information or shipping addresses.

### Entity Properties
<EntityPropertiesTable />

## Relationships

*   **Customer:** A billing profile belongs to one `Customer`. A customer might potentially have multiple profiles in complex scenarios, but often just one.
*   **Address:** Linked to a primary billing `Address`.
*   **PaymentMethod:** May specify a preferred `PaymentMethod`.
*   **Invoice:** Invoices are typically generated using information from the BillingProfile.
*   **Subscription:** Subscriptions may use the associated customer's BillingProfile for charging.

## Examples

*   Jane Doe's personal billing profile with her home address and primary email.
*   Acme Corp's billing profile with their HQ address, VAT ID, and accounts payable email address. 
---
id: SubscriptionPeriod
name: SubscriptionPeriod
version: 1.0.0
identifier: subscriptionPeriodId
summary: Represents a single billing cycle or interval within a subscription's lifetime.

properties:
  - name: subscriptionPeriodId
    type: UUID
    required: true
    description: Unique identifier for this specific subscription period.
  - name: subscriptionId
    type: UUID
    required: true
    description: Identifier of the parent Subscription this period belongs to.
  - name: planId # Denormalized for easier lookup?
    type: UUID
    required: true
    description: Identifier of the Plan active during this period
  - name: startDate
    type: Date
    required: true
    description: The start date of this billing period.
  - name: endDate
    type: Date
    required: true
    description: The end date of this billing period.
  - name: invoiceId # Optional, links to the invoice generated for this period
    type: UUID
    required: false
    description: Identifier of the invoice created for this period's charge.
  - name: paymentId # Optional, links to the payment made for this period's invoice
    type: UUID
    required: false
    description: Identifier of the payment that settled the invoice for this period.
  - name: status
    type: string # (e.g., Active, Billed, Paid, Unpaid, PastDue)
    required: true
    description: Status specific to this period (reflects invoicing/payment state).
  - name: amountBilled
    type: decimal
    required: false # May only be set once invoiced
    description: The actual amount billed for this period (could differ from plan due to promotions, usage, etc.).
  - name: currency
    type: string # ISO 4217 code
    required: false
    description: Currency of the billed amount.
  - name: createdAt
    type: DateTime
    required: true
    description: Timestamp when this period record was created (often at the start of the period).
---

## Overview

The SubscriptionPeriod entity tracks the state and details of a specific billing cycle within a `Subscription`. It links the subscription to the relevant invoice and payment for that interval and records the exact dates and amount billed.

### Entity Properties
<EntityPropertiesTable />

## Relationships

*   **Subscription:** A subscription period belongs to one `Subscription`.
*   **Plan:** Reflects the `Plan` active during this period.
*   **Invoice:** May be associated with one `Invoice` generated for this period.
*   **Payment:** May be associated with one `Payment` that settled the period's invoice.

## Examples

*   Period for Jane Doe's 'Pro Plan' from 2024-05-01 to 2024-05-31, invoiced via #INV-00123, status Paid.
*   Period for Acme Corp's 'Enterprise Plan' from 2024-04-15 to 2024-05-14, status Billed, awaiting payment.
*   The first period (trial) for a new subscription from 2024-05-20 to 2024-06-19, status Active, amountBilled $0.00. 
---
id: inventory.{env}.events
name: Inventory Events Channel
version: 1.0.0
summary: |
  Central event stream for all inventory-related events including stock updates, allocations, and adjustments
owners:
  - dboyne
address: inventory.{env}.events
protocols: 
  - kafka

parameters:
  env:
    enum:
      - dev
      - sit
      - prod
    description: 'Environment to use'
---

### Overview
The Inventory Events channel is the central stream for all inventory-related events across the system. This includes stock level changes, inventory allocations, adjustments, and stocktake events. Events for a specific SKU are guaranteed to be processed in sequence when using productId as the partition key.

<ChannelInformation />

### Publishing and Subscribing to Events

#### Publishing Example
```python
from kafka import KafkaProducer
import json
from datetime import datetime

# Kafka configuration
bootstrap_servers = ['localhost:9092']
topic = f'inventory.{env}.events'

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Example inventory update event
inventory_event = {
    "eventType": "STOCK_LEVEL_CHANGED",
    "timestamp": datetime.utcnow().isoformat(),
    "version": "1.0",
    "payload": {
        "productId": "PROD-456",
        "locationId": "WH-123",
        "previousQuantity": 100,
        "newQuantity": 95,
        "changeReason": "ORDER_FULFILLED",
        "unitOfMeasure": "EACH",
        "batchInfo": {
            "batchId": "BATCH-789",
            "expiryDate": "2025-12-31"
        }
    },
    "metadata": {
        "source": "warehouse_system",
        "correlationId": "inv-xyz-123",
        "userId": "john.doe"
    }
}

# Send the message - using productId as key for partitioning
producer.send(
    topic, 
    key=inventory_event['payload']['productId'].encode('utf-8'),
    value=inventory_event
)
producer.flush()

print(f"Inventory event sent to topic {topic}")

```

### Subscription example

```python
from kafka import KafkaConsumer
import json
from datetime import datetime

class InventoryEventConsumer:
    def __init__(self):
        # Kafka configuration
        self.topic = f'inventory.{env}.events'
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=['localhost:9092'],
            group_id='inventory-processor-group',
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            key_deserializer=lambda x: x.decode('utf-8') if x else None
        )

    def process_event(self, event):
        """Process individual inventory events based on type"""
        event_type = event.get('eventType')
        
        if event_type == 'STOCK_LEVEL_CHANGED':
            self.handle_stock_level_change(event)
        elif event_type == 'LOW_STOCK_ALERT':
            self.handle_low_stock_alert(event)
        # Add more event type handlers as needed

    def handle_stock_level_change(self, event):
        """Handle stock level change events"""
        payload = event['payload']
        print(f"Stock level change detected for product {payload['productId']}")
        print(f"New quantity: {payload['newQuantity']}")
        # Add your business logic here

    def handle_low_stock_alert(self, event):
        """Handle low stock alert events"""
        payload = event['payload']
        print(f"Low stock alert for product {payload['productId']}")
        print(f"Current quantity: {payload['currentQuantity']}")
        # Add your business logic here

    def start_consuming(self):
        """Start consuming messages from the topic"""
        try:
            print(f"Starting consumption from topic: {self.topic}")
            for message in self.consumer:
                try:
                    # Process the message
                    event = message.value
                    print(f"Received event: {event['eventType']} for product: {event['payload']['productId']}")
                    
                    # Process the event
                    self.process_event(event)
                    
                    # Commit the offset after successful processing
                    self.consumer.commit()
                    
                except Exception as e:
                    print(f"Error processing message: {str(e)}")
                    # Implement your error handling logic here
                    # You might want to send to a DLQ (Dead Letter Queue)
        
        except Exception as e:
            print(f"Consumer error: {str(e)}")
        finally:
            # Clean up
            self.consumer.close()

if __name__ == "__main__":
    # Create and start the consumer
    consumer = InventoryEventConsumer()
    consumer.start_consuming()
  ```
---
id: orders.{env}.events
name: Order Events Channel
version: 1.0.1
summary: |
  Central event stream for all order-related events in the order processing lifecycle
owners:
  - dboyne
address: orders.{env}.events
protocols: 
  - azure-servicebus
sidebar:
  badge: 'ServiceBus'
parameters:
  env:
    enum:
      - dev
      - sit
      - prod
    description: 'Environment to use'
---

### Overview
The Orders Events channel is the central stream for all order-related events across the order processing lifecycle. This includes order creation, updates, payment status, fulfillment status, and customer communications. All events related to a specific order are guaranteed to be processed in sequence when using orderId as the partition key.

<ChannelInformation />

### Publishing a message using Azure Service Bus

Here is an example of how to publish an order event using Azure Service Bus:

```python
import json
from datetime import datetime
from azure.servicebus import ServiceBusClient, ServiceBusMessage

# --- Azure Service Bus Configuration ---
# Replace with your actual connection string and queue/topic name
CONNECTION_STR = "YOUR_AZURE_SERVICE_BUS_CONNECTION_STRING"
QUEUE_NAME = "orders"  # Or your specific queue/topic name e.g., f"orders.{env}.events"

# --- Example Order Event Data ---
# This is the same event structure as before
order_event_data = {
    "eventType": "ORDER_CREATED",
    "timestamp": datetime.utcnow().isoformat() + "Z", # ISO 8601 format with Z for UTC
    "version": "1.0",
    "payload": {
        "orderId": "12345",
        "customerId": "CUST-789",
        "items": [
            {
                "productId": "PROD-456",
                "quantity": 2,
                "price": 29.99
            }
        ],
        "totalAmount": 59.98,
        "shippingAddress": {
            "street": "123 Main St",
            "city": "Springfield",
            "country": "US"
        }
    },
    "metadata": {
        "source": "web_checkout",
        "correlationId": "abc-xyz-123"
        # Potentially add a message ID if not automatically handled or for specific tracking
        # "messageId": str(uuid.uuid4()) # Requires import uuid
    }
}

def send_order_event_to_service_bus(connection_string, queue_name, event_data):
    # Create a ServiceBusClient object
    with ServiceBusClient.from_connection_string(conn_str=connection_string) as servicebus_client:
        # Create a sender for the queue
        # For a topic, use: servicebus_client.get_topic_sender(topic_name=queue_name)
        sender = servicebus_client.get_queue_sender(queue_name=queue_name)
        with sender:
            # Serialize the event data to a JSON string
            event_json = json.dumps(event_data)
            # Create a ServiceBusMessage object
            message = ServiceBusMessage(event_json)
            
            # Set properties if needed, e.g., message_id or correlation_id
            # message.message_id = event_data["metadata"].get("messageId")
            message.correlation_id = event_data["metadata"]["correlationId"]
            
            # Send the message
            sender.send_messages(message)
            print(f"Sent order event (ID: {event_data['payload']['orderId']}) to Azure Service Bus queue: {queue_name}")

if __name__ == "__main__":
    # Example of how to call the function
    # Ensure azure-servicebus package is installed: pip install azure-servicebus
    
    # Basic error handling for placeholders
    if CONNECTION_STR == "YOUR_AZURE_SERVICE_BUS_CONNECTION_STRING" or QUEUE_NAME == "YOUR_QUEUE_NAME":
        print("Please update CONNECTION_STR and QUEUE_NAME with your actual Azure Service Bus details.")
    else:
        try:
            send_order_event_to_service_bus(CONNECTION_STR, QUEUE_NAME, order_event_data)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Ensure your Azure Service Bus connection string and queue name are correct,")
            print("and the 'azure-servicebus' package is installed ('pip install azure-servicebus').")
---
id: payments.{env}.events
name: Payment Events Channel
version: 1.0.0
summary: |
 All events contain payment ID for traceability and ordered processing.
owners:
 - dboyne
address: payments.{env}.events
protocols: 
 - kafka

parameters:
 env:
   enum:
     - dev
     - sit
     - prod
   description: 'Environment to use for payment events'
---

### Overview
The Payments Events channel is the central stream for all payment lifecycle events. This includes payment initiation, authorization, capture, completion and failure scenarios. Events for a specific payment are guaranteed to be processed in sequence when using paymentId as the partition key.

<ChannelInformation />

### Publishing Events Using Kafka

Here's an example of publishing a payment event:

```python
from kafka import KafkaProducer
import json
from datetime import datetime

# Kafka configuration
bootstrap_servers = ['localhost:9092']
topic = f'payments.{env}.events'

# Create Kafka producer
producer = KafkaProducer(
   bootstrap_servers=bootstrap_servers,
   value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Example payment processed event
payment_event = {
   "eventType": "PAYMENT_PROCESSED",
   "timestamp": datetime.utcnow().isoformat(),
   "version": "1.0",
   "payload": {
       "paymentId": "PAY-123-456", 
       "orderId": "ORD-789",
       "amount": {
           "value": 99.99,
           "currency": "USD"
       },
       "status": "SUCCESS",
       "paymentMethod": {
           "type": "CREDIT_CARD",
           "last4": "4242",
           "expiryMonth": "12",
           "expiryYear": "2025",
           "network": "VISA"
       },
       "transactionDetails": {
           "processorId": "stripe_123xyz",
           "authorizationCode": "AUTH123",
           "captureId": "CAP456"
       }
   },
   "metadata": {
       "correlationId": "corr-123-abc",
       "merchantId": "MERCH-456", 
       "source": "payment_service",
       "environment": "prod",
       "idempotencyKey": "PAY-123-456-2024-11-11-99.99"
   }
}

# Send message - using paymentId as key for partitioning
producer.send(
   topic,
   key=payment_event['payload']['paymentId'].encode('utf-8'),
   value=payment_event
)
producer.flush()
```
---
id: PaymentFlow
name: Payment Flow for customers
version: 1.0.0
summary: Business flow for processing payments in an e-commerce platform
owners:
    - dboyne
steps:
    - id: "flow_step"
      title: "Flow Step"
      flow:
        id: SubscriptionRenewed
      next_step: 
        id: "place_order_request"  
        label: "Subscription Renewed, New Order Placed"
    - id: "place_order_request"
      title: Place order
      message:
        id: PlaceOrder
        version: 0.0.1
      next_step:
        id: "payment_initiated"
        label: Initiate payment
    - id: "payment_initiated"
      title: Payment Initiated
      message:
        id: PaymentInitiated
        version: 0.0.1
      next_steps:
        - "payment_processed"
        - "payment_failed"
    - id: "payment_processed"
      title: Payment Processed
      message:
        id: PaymentProcessed
        version: 0.0.1
      next_steps:
        - id: "adjust_inventory"
          label: Adjust inventory
        - id: "send_custom_notification"
          label: Notify customer
    - id: "payment_failed"
      title: Payment Failed
      type: node
      next_steps:
        - id: "failure_notification"
          label: Notify customer of failure
        - id: "retry_payment"
          label: Retry payment
    - id: "adjust_inventory"
      title: Inventory Adjusted
      message:
        id: InventoryAdjusted
        version: 1.0.1
      next_step:
        id: "payment_complete"
        label: Complete order
    - id: "send_custom_notification"
      title: Customer Notified of Payment
      type: node
      next_step:
        id: "payment_complete"
        label: Complete order
    - id: "failure_notification"
      title: Customer Notified of Failure
      type: node
    - id: "retry_payment"
      title: Retry Payment
      type: node
      next_step:
        id: "payment_initiated"
        label: Retry payment process
    - id: "payment_complete"
      title: Payment Complete
      message:
        id: PaymentComplete
      next_step:
        id: "order-complete"
        label: Order completed
    - id: "order-complete"
      title: Order Completed
      type: node
---

### Flow of feature
<NodeGraph />
---
id: "CancelSubscription"
name: "User Cancels Subscription"
version: "1.0.0"
summary: "Flow for when a user has cancelled a subscription"
owners:
  - subscriptions-management
steps:
  - id: "cancel_subscription_initiated"
    title: "Cancels Subscription"
    summary: "User cancels their subscription"
    actor:
      name: "User"
    next_step:
      id: "cancel_subscription_request"
      label: "Initiate subscription cancellation"

  - id: "cancel_subscription_request"
    title: "Cancel Subscription"
    message:
      id: "CancelSubscription"
      version: "0.0.1"
    next_step:
      id: "subscription_service"
      label: "Proceed to subscription service"

  - id: "stripe_integration"
    title: "Stripe"
    externalSystem:
      name: "Stripe"
      summary: "3rd party payment system"
      url: "https://stripe.com/"
    next_step:
      id: "subscription_service"
      label: "Return to subscription service"

  - id: "subscription_service"
    title: "Subscription Service"
    service:
      id: "SubscriptionService"
      version: "0.0.1"
    next_steps:
      - id: "stripe_integration"
        label: "Cancel subscription via Stripe"
      - id: "subscription_cancelled"
        label: "Successful cancellation"
      - id: "subscription_rejected"
        label: "Failed cancellation"

  - id: "subscription_cancelled"
    title: "Subscription has been Cancelled"
    message:
      id: "UserSubscriptionCancelled"
      version: "0.0.1"
    next_step:
      id: "notification_service"
      label: "Email customer"

  - id: "subscription_rejected"
    title: "Subscription cancellation has been rejected"

  - id: "notification_service"
    title: "Notifications Service"
    service:
      id: "NotificationService"
      version: "0.0.2"

---

<NodeGraph />

---
id: "SubscriptionRenewed"
name: "Subscription Renewal Flow"
version: "1.0.0"
summary: "Business flow for automatic subscription renewals and related processes"
owners:
  - subscriptions-management
steps:
  - id: "renewal_timer_triggered"
    title: "Renewal Period Reached"
    custom:
      title: "Renewal Timer"
      color: "orange"
      icon: "ClockIcon"
      type: "Scheduler"
      summary: "Automated timer triggers the subscription renewal process"
      height: 8
      properties:
        subscription_id: "sub_12345678"
        renewal_type: "Automatic"
        billing_cycle: "Monthly"
        next_billing_date: "2024-08-01"
      menu:
        - label: "View scheduler configuration"
          url: "https://docs.example.com/scheduler"
        - label: "Subscription timing documentation"
          url: "https://docs.example.com/subscription-timing"
    next_step:
      id: "check_subscription_status"
      label: "Verify subscription status"

  - id: "check_subscription_status"
    title: "Check Subscription Status"
    service:
      id: "SubscriptionService"
      version: "0.0.1"
    next_steps:
      - id: "payment_approval_check"
        label: "Subscription active, proceed to payment"
      - id: "subscription_expired"
        label: "Subscription has expired"
      - id: "subscription_canceled"
        label: "Subscription was canceled"

  - id: "subscription_expired"
    title: "Subscription Expired"
    type: "node"
    next_step:
      id: "send_renewal_notification"
      label: "Notify customer to renew"

  - id: "subscription_canceled"
    title: "Subscription Canceled"
    type: "node"
    next_step:
      id: "send_reactivation_offer"
      label: "Send special reactivation offer"

  - id: "send_renewal_notification"
    title: "Send Renewal Notification"
    service:
      id: "NotificationService"
      version: "0.0.2"
    next_step:
      id: "await_customer_action"
      label: "Wait for customer response"

  - id: "send_reactivation_offer"
    title: "Send Reactivation Offer"
    service:
      id: "NotificationService"
      version: "0.0.2"
    next_step:
      id: "await_customer_action"
      label: "Wait for customer response"

  - id: "await_customer_action"
    title: "Await Customer Action"
    custom:
      title: "Customer Decision Point"
      color: "purple"
      icon: "UserIcon"
      type: "Decision"
      height: 8
      summary: "Waiting period for customer to take action on notification"
      properties:
        timeout_period: "7 days"
        options: "Renew, Upgrade, Cancel, Ignore"
    next_steps:
      - id: "manual_renewal_flow"
        label: "Customer manually renews"
      - id: "flow_ends"
        label: "No action taken"

  - id: "manual_renewal_flow"
    title: "Manual Renewal Flow"
    type: "node"
    next_step:
      id: "payment_initiated"
      label: "Process payment"

  - id: "payment_approval_check"
    title: "Check Payment Approval"
    message:
      id: "GetPaymentStatus"
      version: "0.0.1"
    next_steps:
      - id: "payment_initiated"
        label: "Payment approved, proceed with billing"
      - id: "payment_method_invalid"
        label: "Invalid payment method"

  - id: "payment_method_invalid"
    title: "Invalid Payment Method"
    type: "node"
    next_step:
      id: "request_payment_update"
      label: "Request updated payment method"

  - id: "request_payment_update"
    title: "Request Payment Update"
    service:
      id: "NotificationService"
      version: "0.0.2"
    next_step:
      id: "await_updated_payment"
      label: "Wait for payment update"

  - id: "await_updated_payment"
    title: "Await Updated Payment Method"
    actor:
      name: "Customer"
      summary: "Customer is waiting for payment update"
    next_steps:
      - id: "payment_initiated"
        label: "Payment method updated"
      - id: "subscription_grace_period"
        label: "No update received"

  - id: "subscription_grace_period"
    title: "Grace Period"
    custom:
      title: "Subscription Grace Period"
      color: "yellow"
      icon: "ShieldExclamationIcon"
      type: "Timer"
      summary: "Limited period where subscription remains active despite payment failure"
      properties:
        duration: "7 days"
        status: "At risk"
    next_steps:
      - id: "payment_initiated"
        label: "Payment updated during grace period"
      - id: "subscription_suspended"
        label: "Grace period expired"

  - id: "subscription_suspended"
    title: "Subscription Suspended"
    message:
      id: "UserSubscriptionCancelled"
      version: "0.0.1"
    next_step:
      id: "send_suspension_notification"
      label: "Notify customer of suspension"

  - id: "send_suspension_notification"
    title: "Send Suspension Notification"
    service:
      id: "NotificationService"
      version: "0.0.2"
    next_step:
      id: "flow_ends"
      label: "Flow ends"

  - id: "payment_initiated"
    title: "Process Payment"
    message:
      id: "PaymentInitiated"
      version: "0.0.1"
    next_step:
      id: "payment_gateway"
      label: "Send to payment gateway"

  - id: "payment_gateway"
    title: "Payment Gateway"
    externalSystem:
      name: "Stripe"
      summary: "3rd party payment processor"
      url: "https://stripe.com/"
    next_steps:
      - id: "payment_processed"
        label: "Payment successful"
      - id: "payment_failed"
        label: "Payment failed"

  - id: "payment_failed"
    title: "Payment Failed"
    type: "node"
    next_step:
      id: "retry_payment"
      label: "Retry payment"

  - id: "retry_payment"
    title: "Retry Payment"
    custom:
      title: "Payment Retry Logic"
      color: "red"
      icon: "ArrowPathIcon"
      type: "Processor"
      summary: "Automated retry logic for failed payments"
      properties:
        max_attempts: 3
        backoff_interval: "24 hours"
        current_attempt: 1
    next_steps:
      - id: "payment_initiated"
        label: "Retry payment"
      - id: "subscription_grace_period"
        label: "Max retries exceeded"

  - id: "payment_processed"
    title: "Payment Processed"
    message:
      id: "PaymentProcessed"
      version: "1.0.0"
    next_step:
      id: "update_subscription_status"
      label: "Update subscription"

  - id: "update_subscription_status"
    title: "Update Subscription"
    service:
      id: "SubscriptionService"
      version: "0.0.1"
    next_step:
      id: "send_renewal_confirmation"
      label: "Confirm renewal to customer"

  - id: "send_renewal_confirmation"
    title: "Send Renewal Confirmation"
    service:
      id: "NotificationService"
      version: "0.0.2"
    next_step:
      id: "analyze_customer_usage"
      label: "Analyze customer usage patterns"

  - id: "analyze_customer_usage"
    title: "Analyze Usage Patterns"
    custom:
      title: "Usage Analytics"
      color: "blue"
      icon: "ChartBarIcon"
      type: "Analytics"
      summary: "Analyze customer usage patterns to identify upsell opportunities"
      properties:
        metrics_analyzed: "Feature usage, Resource consumption, Access patterns"
        lookback_period: "90 days"
      menu:
        - label: "View analytics dashboard"
          url: "https://analytics.example.com/subscriptions"
        - label: "Documentation"
          url: "https://docs.example.com/analytics"
    next_steps:
      - id: "send_upgrade_recommendation"
        label: "Usage suggests upgrade opportunity"
      - id: "flow_ends"
        label: "No upgrade opportunity identified"

  - id: "send_upgrade_recommendation"
    title: "Send Upgrade Recommendation"
    service:
      id: "NotificationService"
      version: "0.0.2"
    next_step:
      id: "flow_ends"
      label: "Flow completed"

  - id: "flow_ends"
    title: "Flow Completed"
    type: "node"

---

## Subscription Renewal Flow

This flow documents the process of automatic subscription renewals, including handling various edge cases such as payment failures, expired subscriptions, and customer interactions.

<NodeGraph />

### Key Components

* **Automatic Renewal Process**: Triggered by a scheduled timer when the subscription renewal period is reached
* **Payment Processing**: Integration with payment gateway and handling of payment failures
* **Customer Notifications**: Various notifications sent throughout the process
* **Grace Period Handling**: Special handling when payments fail with a grace period before subscription suspension
* **Usage Analytics**: Analysis of customer usage patterns to identify upgrade opportunities

### Business Rules

1. Subscriptions are renewed automatically unless explicitly canceled
2. Failed payments trigger a retry process (up to 3 attempts)
3. Customers receive a 7-day grace period before subscription suspension
4. Usage patterns are analyzed to provide personalized upgrade recommendations

---
id: "CancelSubscription"
name: "User Cancels Subscription"
version: "0.0.1"
summary: "Flow for when a user has cancelled a subscription"
owners:
  - subscriptions-management
steps:
  - id: "cancel_subscription_initiated"
    title: "Cancels Subscription"
    summary: "User cancels their subscription"
    actor:
      name: "User"
    next_step:
      id: "cancel_subscription_request"
      label: "Initiate subscription cancellation"

  - id: "cancel_subscription_request"
    title: "Cancel Subscription"
    message:
      id: "CancelSubscription"
      version: "0.0.1"
    next_step:
      id: "subscription_service"
      label: "Proceed to subscription service"

  - id: "stripe_integration"
    title: "Stripe"
    externalSystem:
      name: "Stripe"
      summary: "3rd party payment system"
      url: "https://stripe.com/"
    next_step:
      id: "subscription_service"
      label: "Return to subscription service"

  - id: "subscription_service"
    title: "Subscription Service"
    service:
      id: "SubscriptionService"
      version: "0.0.1"
    next_steps:
      - id: "stripe_integration"
        label: "Cancel subscription via Stripe"
      - id: "subscription_cancelled"
        label: "Successful cancellation"
      - id: "subscription_rejected"
        label: "Failed cancellation"
---

<NodeGraph />

---
title: Creating new microservices
summary: A comprehensive guide to creating new microservices at FlowMart following our best practices and standards
sidebar:
    label: Introduction
    order: 1
owners: 
  - dboyne
badges:
  - content: 'Guide'
    backgroundColor: 'teal'
    textColor: 'teal'
---

Welcome to the FlowMart microservices creation guide. This documentation will help you understand our microservices architecture and guide you through the process of creating, deploying, and maintaining new services that align with our architectural standards and best practices.

## FlowMart's Microservices Architecture

At FlowMart, we've adopted an [Event-**Driven** Architecture (EDA)](/docs/architecture-records/published/02-eda-adoption) for our e-commerce platform. Our architecture consists of domain-oriented microservices that communicate primarily through events, with Apache Kafka serving as our event backbone.

Key architectural principles we follow:

- **Domain-Driven Design**: **Services** are organized around business domains with clear bounded contexts
- **Service Autonomy**: Each service owns its data and can be independently deployed
- **Event-First Communication**: Services publish events when state changes and subscribe to events from other domains
- **Eventual Consistency**: We prioritize availability and partition tolerance over immediate consistency
- **API-First Development**: All services expose well-defined APIs using standardized patterns

## Example service in our architecture (InventoryService)
<NodeGraph id="InventoryService" version="0.0.2" type="service"  />

## Example of event stream in our architecture

If you look at the example service in our architecture, you can see that it has a single event stream. This is a simple example of how we use event streams to communicate between services.

<Design file="event-stream-example" search={false} />


## Getting Started

Before creating a new microservice, please familiarize yourself with our architectural decisions:

1. [Event-Driven Architecture Adoption](/docs/architecture-records/published/02-eda-adoption)
2. [API Gateway Pattern Adoption](/docs/architecture-records/published/01-api-gateway-pattern)
3. [CI/CD and Deployment Strategy](/docs/architecture-records/drafts/02-cicd-deployment-strategy)
4. [API Management and Governance](/docs/architecture-records/drafts/03-api-management-governance)

## Service Creation Process

The following steps outline our microservice creation process:

1. **Domain Analysis**: Identify the business domain and define the bounded context
2. **Service Definition**: Create service specification using our templating tools
3. **Infrastructure Provisioning**: Use our Terraform modules to provision required infrastructure
4. **Service Implementation**: Develop the service following our technological standards
5. **CI/CD Pipeline Setup**: Configure the service pipeline for continuous integration and deployment
6. **Testing**: Implement comprehensive testing (unit, integration, contract, end-to-end)
7. **Documentation**: Document API contracts, event schemas, and service behaviors
8. **Deployment**: Deploy to production using our GitOps workflow

## Available Service Templates

We provide several starter templates for new microservices:

- [Node.js Service Template](/docs/guides/creating-new-microservices/node-service)
- [TypeScript Service Template](/docs/guides/creating-new-microservices/typescript-service)
- [Java Spring Boot Template](/docs/guides/creating-new-microservices/java-spring-boot)
- [Python FastAPI Template](/docs/guides/creating-new-microservices/python-fastapi)

## Infrastructure as Code

All FlowMart infrastructure is managed using [Terraform](/docs/guides/creating-new-microservices/terraform-modules). We maintain a set of reusable modules for common infrastructure components, which you should leverage when creating new services.

## Development Workflow

1. **Engage with the Platform Team**: Discuss your new service requirements with the platform team
2. **Create Service Repository**: Use our GitLab template to create a new service repository
3. **Setup Local Environment**: Configure your local development environment
4. **Implement Core Functionality**: Develop the service capabilities
5. **Review and Testing**: Submit for architecture and code review
6. **Deploy to Production**: Use our deployment pipeline for production rollout

## Support

If you need assistance creating a new microservice, please reach out to:

- **Platform Engineering Team**: For infrastructure and deployment questions
- **Architecture Team**: For design and architecture guidance
- **DevOps Team**: For CI/CD and operational support

## Next Steps

- Continue to [Service Design Principles](/docs/guides/creating-new-microservices/service-design-principles)
- Learn about [Node.js Service Creation](/docs/guides/creating-new-microservices/node-service)
- Explore our [Terraform Modules](/docs/guides/creating-new-microservices/terraform-modules) 
---
title: Microservice Design Principles
summary: Core design principles and best practices for creating well-structured microservices at FlowMart
sidebar:
    label: Design Principles
    order: 2
---

At FlowMart, we follow a set of design principles that guide the creation of new microservices. These principles help ensure our services are maintainable, scalable, and aligned with our overall architectural vision.

## 1. Domain-Driven Design

Each microservice should be aligned with a specific business domain or subdomain. We follow Domain-Driven Design (DDD) principles to identify service boundaries:

### Bounded Contexts

- Define clear bounded contexts for each service
- Maintain a separate ubiquitous language within each context
- Document domain models and context maps

### Example Domains at FlowMart

| Domain | Description | Example Services |
|--------|-------------|------------------|
| Order | Order processing and management | order-service, order-history-service |
| Inventory | Product inventory management | inventory-service, stock-management-service |
| Customer | Customer accounts and profiles | customer-service, authentication-service |
| Payment | Payment processing and refunds | payment-service, refund-service |
| Shipping | Shipping and logistics | shipping-service, tracking-service |
| Catalog | Product information management | product-service, search-service |

## 2. Single Responsibility

Each microservice should have a single responsibility and a clear purpose:

- **Focus on one business capability**: Services should do one thing well
- **Right-sized services**: Not too large (mini-monolith) or too small (nano-service)
- **Cohesive functionality**: Related functions should be grouped together

## 3. Data Ownership

Microservices should own their data and maintain data autonomy:

- Each service has its own database or data store
- No direct data sharing between services
- Data is exposed through well-defined APIs
- Services should be the single source of truth for their domain data

## 4. API Design

All FlowMart microservices must follow our [API Management and Governance Strategy](/docs/architecture-records/drafts/03-api-management-governance):

### RESTful APIs

- Use consistent resource naming conventions
- Follow standard HTTP methods and status codes
- Implement proper error handling and validation
- Design for backward compatibility

### Event-Driven Interfaces

- Define clear event schemas using AsyncAPI
- Document event ownership and responsibilities
- Follow event versioning standards
- Implement idempotent event consumers

## 5. Resilience and Fault Tolerance

Microservices must be designed to handle failures gracefully:

- Implement circuit breakers for downstream dependencies
- Use timeouts and retries with exponential backoff
- Design for graceful degradation of functionality
- Implement health checks and readiness probes

## 6. Observability

All services must expose monitoring and observability data:

- Structured logging (using our ELK stack)
- Metrics exposure (Prometheus format)
- Distributed tracing support (Jaeger)
- Health check endpoints

## 7. Security by Design

Security must be integrated into every service:

- Authentication using OAuth 2.0 / OpenID Connect
- Authorization using role-based access control
- TLS encryption for all communications
- Input validation and output encoding
- No sensitive data in logs or traces

## 8. Testability

Services should be designed with testing in mind:

- High unit test coverage (minimum 80%)
- Integration tests for all critical paths
- Contract tests for API interfaces
- Easy local testing setup
- Simulated dependencies for development

## 9. Configuration Management

Services should follow our configuration management approach:

- Environment-specific configuration via Kubernetes ConfigMaps
- Secrets management via HashiCorp Vault
- Feature flags for conditional functionality
- No hardcoded configuration values

## 10. Independence and Deployability

Services should be independently deployable:

- No deployment coupling with other services
- Infrastructure as Code for all resources
- Self-contained CI/CD pipelines
- Blue/green or canary deployment capabilities

## Microservice Checklist

Use this checklist when designing a new service:

- [ ] Service aligns with a specific business domain
- [ ] Clear bounded context defined
- [ ] Service owns its data
- [ ] APIs follow company standards
- [ ] Event schemas are documented
- [ ] Resilience patterns implemented
- [ ] Observability instrumentation added
- [ ] Security controls integrated
- [ ] Comprehensive test suite created
- [ ] Configuration externalized
- [ ] Independent deployment pipeline configured

## Next Steps

- Learn how to [create a Node.js microservice](/docs/guides/creating-new-microservices/node-service)
- Explore [TypeScript service implementation](/docs/guides/creating-new-microservices/typescript-service)
- Understand our [Terraform infrastructure modules](/docs/guides/creating-new-microservices/terraform-modules) 
---
title: Database Patterns for Microservices
summary: Best practices and patterns for managing data in FlowMart microservices
sidebar:
    label: Database Patterns
    order: 5
---

This guide outlines the database patterns and best practices for managing data in FlowMart's microservices architecture.

## Database Per Service Pattern

At FlowMart, we follow the **Database Per Service** pattern as our primary data management strategy:

- **Definition**: Each microservice owns and manages its database exclusively
- **Access Pattern**: Only the service that owns the database can perform direct read/write operations
- **Purpose**: Ensures loose coupling, independent scaling, and domain isolation

![Database Per Service Diagram](/docs/images/database-per-service.png)

### Why This Pattern?

1. **Service Independence**: Services can be developed, deployed, and scaled independently
2. **Technology Freedom**: Teams can choose the most appropriate database technology for their service needs
3. **Resilience**: Database failures are isolated to individual services
4. **Security**: Clear data ownership boundaries limit the blast radius of security incidents
5. **Performance**: Database schemas and indexes can be optimized for specific service requirements

## Supported Database Technologies

FlowMart supports the following database technologies for microservices:

| Database Type | Technology | Best For | Support Level |
|--------------|------------|----------|---------------|
| Document | MongoDB | Flexible schemas, rapid development | Primary |
| Relational | PostgreSQL | Complex transactions, structured data | Primary |
| Key-Value | Redis | Caching, session management, rate limiting | Primary |
| Search | Elasticsearch | Full-text search, analytics | Secondary |
| Graph | Neptune | Relationship-heavy domains (e.g., recommendations) | Secondary |
| Time-Series | InfluxDB | Metrics, monitoring data | Secondary |

> **Primary**: Fully supported with managed services, infrastructure modules, and dedicated support
> 
> **Secondary**: Available but with limited tooling and support

## Data Modeling Principles

### 1. Model Around Bounded Contexts

- Define clear domain boundaries based on business capabilities
- Avoid modeling your database around UI needs
- Focus on the core domain model within each service

### 2. Design for Access Patterns

- Consider query patterns when designing the schema
- Optimize for the most frequent queries
- Plan for future data growth and access needs

### 3. Denormalization When Appropriate

- Strategic denormalization is often necessary in distributed systems
- Consider composite keys for efficient lookups
- Use materialized views for read-heavy scenarios

### Example: Product Service Data Model (MongoDB)

```javascript
// Product Collection
{
  "_id": ObjectId("5f8d0f3e1c9d440000c9a1f5"),
  "name": "Ultra HD Smart TV",
  "description": "55-inch Ultra HD Smart TV with voice control",
  "sku": "TV-55UHD-2023",
  "price": {
    "amount": 699.99,
    "currency": "USD"
  },
  "category": "electronics",
  "subcategory": "televisions",
  "attributes": {
    "brand": "TechVision",
    "model": "UHD-55X",
    "screenSize": "55",
    "resolution": "3840x2160",
    "smartFeatures": true,
    "voiceControl": true,
    "energyRating": "A+"
  },
  "images": [
    {
      "url": "https://storage.flowmart.com/products/tv-55uhd-2023-main.jpg",
      "isPrimary": true,
      "alt": "TechVision 55-inch Smart TV front view"
    },
    {
      "url": "https://storage.flowmart.com/products/tv-55uhd-2023-side.jpg",
      "isPrimary": false,
      "alt": "TechVision 55-inch Smart TV side view"
    }
  ],
  "inventory": {
    "inStock": 127,
    "reserved": 13,
    "available": 114,
    "lowStockThreshold": 25,
    "lastUpdated": ISODate("2023-09-15T14:23:45.000Z")
  },
  "status": "active",
  "createdAt": ISODate("2023-05-01T09:30:00.000Z"),
  "updatedAt": ISODate("2023-09-15T14:23:45.000Z")
}

// Review Collection
{
  "_id": ObjectId("5f8d0f3e1c9d440000c9a1f9"),
  "productId": ObjectId("5f8d0f3e1c9d440000c9a1f5"),
  "customerId": "cust-12345",
  "rating": 4.5,
  "title": "Great TV for the price",
  "content": "The picture quality is excellent and setup was easy...",
  "verified": true,
  "helpfulVotes": 27,
  "createdAt": ISODate("2023-06-15T18:22:10.000Z")
}
```

### Example: Order Service Data Model (PostgreSQL)

```sql
-- Orders Table
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  customer_id VARCHAR(255) NOT NULL,
  order_number VARCHAR(50) NOT NULL UNIQUE,
  status VARCHAR(50) NOT NULL,
  total_amount DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(3) NOT NULL,
  shipping_address_id UUID NOT NULL,
  billing_address_id UUID NOT NULL,
  payment_method_id UUID,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Order Items Table
CREATE TABLE order_items (
  id UUID PRIMARY KEY,
  order_id UUID NOT NULL REFERENCES orders(id),
  product_id VARCHAR(255) NOT NULL,
  product_sku VARCHAR(100) NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  quantity INTEGER NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  subtotal DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
```

## Data Consistency Patterns

### 1. Eventual Consistency with Event-Driven Updates

At FlowMart, we embrace eventual consistency for most inter-service data coordination:

```mermaid
sequenceDiagram
    participant Order Service
    participant Kafka
    participant Inventory Service
    participant Notification Service
    
    Order Service->>Order Service: Create Order
    Order Service->>Kafka: Publish OrderCreated
    Kafka->>Inventory Service: Consume OrderCreated
    Inventory Service->>Inventory Service: Update Inventory
    Kafka->>Notification Service: Consume OrderCreated
    Notification Service->>Notification Service: Send Notification
```

### 2. Saga Pattern for Distributed Transactions

For operations that span multiple services and require transactional semantics:

```mermaid
sequenceDiagram
    participant Order Service
    participant Payment Service
    participant Inventory Service
    participant Shipping Service
    
    Order Service->>Payment Service: Process Payment
    Payment Service-->>Order Service: Payment Processed
    Order Service->>Inventory Service: Reserve Inventory
    Inventory Service-->>Order Service: Inventory Reserved
    Order Service->>Shipping Service: Create Shipment
    Shipping Service-->>Order Service: Shipment Created
    
    alt Failure at any step
        Note over Order Service,Shipping Service: Begin compensating transactions
        Order Service->>Payment Service: Refund Payment
        Order Service->>Inventory Service: Release Inventory
        Order Service->>Shipping Service: Cancel Shipment
    end
```

### 3. CQRS (Command Query Responsibility Segregation)

For services with complex read patterns or high read-to-write ratios:

```
┌───────────────┐     Commands     ┌───────────────┐
│               │ ──────────────▶  │               │
│   API Layer   │                  │ Command Model │
│               │ ◀──────────────  │               │
└───────────────┘                  └───────────────┘
        │                                  │
        │                                  │
        │                                  ▼
        │                          ┌───────────────┐
        │                          │               │
        │                          │  Event Store  │
        │                          │               │
        │                          └───────────────┘
        │                                  │
        │                                  │
        ▼                                  ▼
┌───────────────┐                  ┌───────────────┐
│               │                  │               │
│  Query Model  │ ◀──────────────  │ Event Handler │
│               │                  │               │
└───────────────┘                  └───────────────┘
```

## Data Migration Patterns

### 1. Schema Evolution

For incremental changes to a service's schema:

- Add new fields with default values
- Make changes backward compatible
- Use database migration tools (e.g., Flyway, Liquibase, MongoDB migrations)

Example migration script (Flyway):

```sql
-- V2023.09.15.1__Add_Order_Tracking.sql
ALTER TABLE orders ADD COLUMN tracking_number VARCHAR(100);
ALTER TABLE orders ADD COLUMN shipping_carrier VARCHAR(50);
```

### 2. Expand-Contract Pattern (Parallel Change)

For significant schema changes:

1. **Expand**: Add new fields/tables while maintaining old ones
2. **Migrate**: Copy/transform data from old to new structure
3. **Contract**: Remove old fields/tables after migration is complete

### 3. Service Decomposition

When splitting a monolithic database:

1. Identify bounded contexts
2. Create new service databases
3. Implement dual-write mechanism temporarily
4. Migrate historical data
5. Switch reads to the new database
6. Remove old tables after migration completes

## Database Access Patterns

### Repository Pattern

Our standard approach for database access:

```typescript
// Product Repository Interface
export interface ProductRepository {
  findById(id: string): Promise<Product | null>;
  findByCategory(category: string, limit?: number, offset?: number): Promise<Product[]>;
  findByQuery(query: ProductQuery): Promise<Product[]>;
  save(product: Product): Promise<Product>;
  update(id: string, updates: Partial<Product>): Promise<Product | null>;
  delete(id: string): Promise<boolean>;
}

// MongoDB Implementation
export class MongoProductRepository implements ProductRepository {
  constructor(private readonly db: Db) {}
  
  async findById(id: string): Promise<Product | null> {
    const result = await this.db.collection('products').findOne({ _id: new ObjectId(id) });
    return result ? this.mapToProduct(result) : null;
  }
  
  // Additional implementation methods...
}

// PostgreSQL Implementation
export class PostgresProductRepository implements ProductRepository {
  constructor(private readonly pool: Pool) {}
  
  async findById(id: string): Promise<Product | null> {
    const result = await this.pool.query(
      'SELECT * FROM products WHERE id = $1',
      [id]
    );
    return result.rows.length ? this.mapToProduct(result.rows[0]) : null;
  }
  
  // Additional implementation methods...
}
```

## Connection Management

### Connection Pooling

```javascript
// MongoDB Connection Pool (Node.js)
const { MongoClient } = require('mongodb');

class MongoDbClient {
  constructor(config) {
    this.client = new MongoClient(config.uri, {
      maxPoolSize: config.maxPoolSize || 10,
      minPoolSize: config.minPoolSize || 5,
      maxIdleTimeMS: config.maxIdleTimeMS || 30000,
      connectTimeoutMS: config.connectTimeoutMS || 5000
    });
  }
  
  async connect() {
    await this.client.connect();
    this.db = this.client.db(config.dbName);
    console.log('Connected to MongoDB');
    return this.db;
  }
  
  async disconnect() {
    await this.client.close();
    console.log('Disconnected from MongoDB');
  }
}
```

### Health Checks

```typescript
// Database Health Check (TypeScript)
export class DatabaseHealthCheck {
  constructor(private readonly dbClient: DbClient) {}
  
  async check(): Promise<HealthStatus> {
    try {
      const startTime = Date.now();
      await this.dbClient.ping();
      const responseTime = Date.now() - startTime;
      
      return {
        status: 'UP',
        responseTime,
        details: {
          database: this.dbClient.getDatabaseName(),
          connections: await this.dbClient.getConnectionStats()
        }
      };
    } catch (error) {
      return {
        status: 'DOWN',
        error: error.message,
        details: {
          database: this.dbClient.getDatabaseName()
        }
      };
    }
  }
}
```

## Database Security Practices

1. **Use IAM Roles/Service Accounts**: Avoid hardcoded credentials
2. **Encryption**: Enable at-rest and in-transit encryption
3. **No Direct Public Access**: Databases should never be directly exposed to the internet
4. **Least Privilege**: Grant minimal required permissions to service accounts
5. **Data Classification**: Tag data according to sensitivity
6. **Audit Logging**: Enable database auditing for sensitive operations
7. **Regular Backups**: Implement automated backup strategies
8. **Secure Connection Strings**: Store connection information in secure vaults

## Technology-Specific Guidelines

### MongoDB Best Practices

- Use document validation for schema enforcement
- Create indexes for frequent query patterns
- Limit document size (< 16MB)
- Use aggregation pipelines for complex queries
- Implement TTL indexes for expiring data

### PostgreSQL Best Practices

- Use connection pooling
- Implement database partitioning for large tables
- Create appropriate indexes based on query patterns
- Use prepared statements to prevent SQL injection
- Implement row-level security for multi-tenant data

### Redis Best Practices

- Set appropriate key expiration times
- Use Redis data structures (not just key-value)
- Implement Redis Cluster for high availability
- Monitor memory usage
- Use Redis for its strengths: caching, rate limiting, session storage

## Infrastructure as Code for Databases

FlowMart provides Terraform modules for common database setups:

```hcl
# MongoDB Atlas Cluster
module "mongodb_cluster" {
  source = "git::https://gitlab.flowmart.com/platform/terraform-modules//mongodb-atlas"
  
  project_id      = var.atlas_project_id
  cluster_name    = "${var.service_name}-${var.environment}"
  environment     = var.environment
  instance_size   = var.environment == "production" ? "M10" : "M0"
  region          = var.region
  
  backup_enabled = var.environment == "production" ? true : false
  
  teams = {
    owner     = "team-product",
    developer = "team-product-dev"
  }
  
  tags = {
    Service     = var.service_name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# PostgreSQL RDS Instance
module "postgres_db" {
  source = "git::https://gitlab.flowmart.com/platform/terraform-modules//aws-rds-postgres"
  
  identifier          = "${var.service_name}-${var.environment}"
  allocated_storage   = var.environment == "production" ? 100 : 20
  storage_type        = "gp2"
  engine_version      = "13.4"
  instance_class      = var.environment == "production" ? "db.m5.large" : "db.t3.small"
  database_name       = replace(var.service_name, "-", "_")
  vpc_id              = var.vpc_id
  subnet_ids          = var.database_subnet_ids
  multi_az            = var.environment == "production" ? true : false
  deletion_protection = var.environment == "production" ? true : false
  
  backup_retention_period = var.environment == "production" ? 7 : 1
  
  tags = {
    Service     = var.service_name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}
```

## Data Governance

### Practices for Maintaining Data Integrity

1. **Schema Registry**: Register and validate event schemas
2. **Data Catalogs**: Document available data and owners
3. **Data Lineage**: Track how data flows between services
4. **Data Quality Checks**: Implement validation and integrity checks
5. **Master Data Management**: Establish source-of-truth services

### GDPR and Compliance

1. **Data Minimization**: Collect only necessary data
2. **Right to Erasure**: Implement mechanisms to delete customer data
3. **Data Portability**: Support data export in common formats
4. **Consent Management**: Track and honor user consent
5. **Purpose Limitation**: Use data only for its intended purpose

## Recommended Resources

- **Books**:
  - "Database Internals" by Alex Petrov
  - "Designing Data-Intensive Applications" by Martin Kleppmann

- **Courses**:
  - MongoDB University
  - PostgreSQL Administration by EnterpriseDB

- **FlowMart Resources**:
  - Internal Database Patterns Playbook
  - Monthly Database Office Hours

## Next Steps

- Learn about [Event schema design](/docs/guides/creating-new-microservices/event-schemas)
- Explore [API design best practices](/docs/guides/creating-new-microservices/api-design)
- Understand [Observability in microservices](/docs/guides/creating-new-microservices/observability) 
---
title: Event Schema Design
summary: Best practices for designing and managing event schemas in FlowMart's event-driven architecture
sidebar:
    label: Event Schema Design
    order: 6
---

This guide outlines best practices for designing, evolving, and managing event schemas in FlowMart's event-driven architecture.

## Introduction to Events in Our Architecture

Events are the backbone of FlowMart's microservices ecosystem. They enable:

- **Loose coupling** between services
- **Asynchronous communication**
- **Eventual consistency** across service boundaries
- **Event sourcing** for critical business processes
- **Audit trails** of system changes

## Event Schema Fundamentals

### What Is an Event Schema?

An event schema defines the structure and validation rules for events flowing through our system. Properly designed schemas ensure events can be:

- **Produced** consistently by services 
- **Consumed** reliably by other services
- **Evolved** over time without breaking consumers
- **Validated** to prevent invalid data from propagating
- **Documented** for developers to understand and use

### Event Schema Registry

FlowMart uses a centralized **Schema Registry** to:

1. Store all event schemas
2. Validate events at publish time
3. Provide a browsable catalog of events
4. Track schema versions and compatibility
5. Generate client libraries and documentation

All services must register their event schemas in the central registry before publishing events.

## Schema Design Principles

### 1. Design for Evolution

Events should be designed to evolve over time:

- **Additive Changes Only**: Add optional fields rather than modifying existing ones
- **Required Minimal Core**: Keep required fields to essential business data
- **Meaningful Defaults**: Provide sensible defaults for optional fields
- **Version Awareness**: Include schema version information

### 2. Event Ownership

Each event type has a single owner:

- The **producing service** owns the event schema
- Only the owner can make changes to the schema
- The owner is responsible for schema compatibility

### 3. Semantic Versioning

Follow semantic versioning for event schemas:

- **Major Version**: Breaking changes (consumers must update)
- **Minor Version**: Backward-compatible feature additions
- **Patch Version**: Backward-compatible bug fixes

### 4. Business-Oriented Event Naming

Events should be named using business terminology:

- Use past tense verbs (e.g., `OrderPlaced`, not `CreateOrder`)
- Follow the pattern: `[Entity][Event]` (e.g., `ProductCreated`, `PaymentProcessed`)
- Use domain-specific terminology consistent with our ubiquitous language

## Event Schema Format (JSON Schema)

FlowMart uses JSON Schema as the standard format for defining event schemas:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.flowmart.com/events/product/ProductCreated/1.0.0",
  "title": "ProductCreated",
  "description": "Represents the creation of a new product in the catalog",
  "type": "object",
  "required": ["eventId", "eventType", "eventVersion", "timestamp", "data"],
  "properties": {
    "eventId": {
      "type": "string",
      "format": "uuid",
      "description": "Unique identifier for this event instance"
    },
    "eventType": {
      "type": "string",
      "enum": ["ProductCreated"],
      "description": "Type of the event"
    },
    "eventVersion": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$",
      "description": "Semantic version of the event schema"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO-8601 timestamp when the event was created"
    },
    "source": {
      "type": "string",
      "description": "Service that produced the event"
    },
    "data": {
      "type": "object",
      "required": ["productId", "name", "sku", "price"],
      "properties": {
        "productId": {
          "type": "string",
          "format": "uuid",
          "description": "Unique identifier for the product"
        },
        "name": {
          "type": "string",
          "minLength": 1,
          "maxLength": 255,
          "description": "Name of the product"
        },
        "description": {
          "type": "string",
          "maxLength": 2000,
          "description": "Description of the product"
        },
        "sku": {
          "type": "string",
          "pattern": "^[A-Z0-9-]{5,20}$",
          "description": "Stock keeping unit - unique product identifier"
        },
        "price": {
          "type": "object",
          "required": ["amount", "currency"],
          "properties": {
            "amount": {
              "type": "number",
              "exclusiveMinimum": 0,
              "description": "Price amount"
            },
            "currency": {
              "type": "string",
              "enum": ["USD", "EUR", "GBP", "CAD"],
              "description": "Price currency code"
            }
          }
        },
        "categories": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Categories the product belongs to"
        },
        "attributes": {
          "type": "object",
          "additionalProperties": {
            "type": ["string", "number", "boolean"]
          },
          "description": "Additional product attributes as key-value pairs"
        }
      }
    },
    "metadata": {
      "type": "object",
      "additionalProperties": true,
      "description": "Additional contextual information about the event"
    },
    "correlationId": {
      "type": "string",
      "format": "uuid",
      "description": "ID for correlating related events"
    },
    "causationId": {
      "type": "string",
      "format": "uuid",
      "description": "ID of the event that caused this event"
    }
  },
  "additionalProperties": false
}
```

## Standard Event Envelope

All FlowMart events follow a standard envelope structure:

```json
{
  "eventId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "eventType": "ProductCreated",
  "eventVersion": "1.0.0",
  "timestamp": "2023-09-15T13:25:47.803Z",
  "source": "product-service",
  "data": {
    // Event-specific payload
  },
  "metadata": {
    // Optional contextual information
  },
  "correlationId": "7f8d0e3c-d5f9-42e1-a11b-78ad6c0c380a",
  "causationId": "3e4f5d6c-7b8a-9c0d-1e2f-3a4b5c6d7e8f"
}
```

### Required Envelope Fields

| Field | Type | Description |
|-------|------|-------------|
| eventId | UUID | Unique identifier for the event instance |
| eventType | String | Name of the event (e.g., `ProductCreated`) |
| eventVersion | String | Semantic version of the event schema |
| timestamp | ISO-8601 | When the event occurred |
| data | Object | Event-specific payload |

### Optional Envelope Fields

| Field | Type | Description |
|-------|------|-------------|
| source | String | Service that produced the event |
| metadata | Object | Additional context about the event |
| correlationId | UUID | ID for correlating related events in a flow |
| causationId | UUID | ID of the event that caused this event |

## Event Data Types

### Primitive Types

- **String**: Use for text data
- **Number**: Use for numeric values (integers or decimals)
- **Boolean**: Use for true/false flags
- **Array**: Use for collections of the same type
- **Object**: Use for nested structures

### Specialized Formats

- **UUID**: Use for unique identifiers (format: `uuid`)
- **ISO Date-Time**: Use for timestamps (format: `date-time`)
- **Email**: Use for email addresses (format: `email`)
- **URI**: Use for web addresses (format: `uri`)
- **Decimal**: Use for currency amounts (type: `number`)

### Complex Types

For complex or reusable types, create separate schema definitions:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.flowmart.com/common/Address/1.0.0",
  "title": "Address",
  "type": "object",
  "required": ["line1", "city", "postalCode", "country"],
  "properties": {
    "line1": {
      "type": "string",
      "maxLength": 100
    },
    "line2": {
      "type": "string",
      "maxLength": 100
    },
    "city": {
      "type": "string",
      "maxLength": 100
    },
    "region": {
      "type": "string",
      "maxLength": 100
    },
    "postalCode": {
      "type": "string",
      "maxLength": 20
    },
    "country": {
      "type": "string",
      "maxLength": 2,
      "pattern": "^[A-Z]{2}$"
    }
  }
}
```

Then reference them in your event schemas:

```json
{
  "properties": {
    "shippingAddress": {
      "$ref": "https://schemas.flowmart.com/common/Address/1.0.0"
    }
  }
}
```

## Common Event Patterns

### State Change Events

Represent changes to an entity's state:

```json
{
  "eventType": "OrderStatusChanged",
  "data": {
    "orderId": "61fea0a1-2ac4-4e8c-a851-d38f7c8c06f9",
    "previousStatus": "PAYMENT_PENDING",
    "newStatus": "PAYMENT_COMPLETED",
    "reason": "Payment successful",
    "changedBy": "payment-service"
  }
}
```

### Resource Creation Events

Represent the creation of a new entity:

```json
{
  "eventType": "CustomerCreated",
  "data": {
    "customerId": "cust-12345",
    "email": "john.doe@example.com",
    "firstName": "John",
    "lastName": "Doe",
    "createdAt": "2023-09-15T10:30:00Z"
  }
}
```

### Resource Update Events

Represent updates to an existing entity:

```json
{
  "eventType": "ProductUpdated",
  "data": {
    "productId": "b3c631a5-f7c8-4d89-a57f-dd2f069b5730",
    "changes": {
      "price": {
        "amount": 24.99,
        "currency": "USD"
      },
      "inventory": {
        "inStock": 250
      }
    },
    "updatedAt": "2023-09-15T14:22:36Z"
  }
}
```

### Action Events

Represent business actions that occurred:

```json
{
  "eventType": "PaymentProcessed",
  "data": {
    "paymentId": "pay-67890",
    "orderId": "ord-12345",
    "amount": 99.99,
    "currency": "USD",
    "status": "SUCCESSFUL",
    "paymentMethod": "CREDIT_CARD",
    "processedAt": "2023-09-15T13:45:22Z"
  }
}
```

## Schema Evolution

### Compatibility Types

We support the following compatibility modes for schema evolution:

- **Backward**: New schema can read data produced with previous schema
- **Forward**: Previous schema can read data produced with new schema
- **Full**: Both backward and forward compatibility
- **None**: No compatibility guarantees (use with caution)

### Backward Compatibility Rules

1. **Adding optional fields** is safe
2. **Removing optional fields** is safe
3. **Making a required field optional** is safe
4. **Adding new enum values** is safe
5. **Widening numeric ranges** is safe (e.g., int to float)

### Breaking Changes to Avoid

1. ❌ **Removing required fields**
2. ❌ **Adding required fields**
3. ❌ **Changing field types**
4. ❌ **Renaming fields**
5. ❌ **Restricting enum values**

### Handling Breaking Changes

If you must make a breaking change:

1. Create a new major version of the schema
2. Maintain both versions for a transition period
3. Implement dual publishing for critical events
4. Help consumers migrate to the new version
5. Deprecate the old version with advance notice

## Consuming Events

### Consumer Best Practices

1. **Be tolerant in what you accept**:
   - Ignore unknown fields
   - Provide defaults for missing optional fields
   - Handle enum values gracefully, including unknown values

2. **Validate incoming events**:
   - Verify events against their schema
   - Check required fields
   - Validate business rules before processing

3. **Handle versioning gracefully**:
   - Check event version before processing
   - Implement version-specific handlers if needed
   - Subscribe to schema registry updates

### Consumer Code Example (TypeScript)

```typescript
import { KafkaConsumer } from '@flowmart/kafka-client';
import { SchemaRegistry } from '@flowmart/schema-registry';
import { OrderProcessingService } from './services';

// Initialize schema registry client
const schemaRegistry = new SchemaRegistry({
  baseUrl: 'https://schema-registry.flowmart.com',
});

// Define event interface
interface OrderPlacedEvent {
  eventId: string;
  eventType: 'OrderPlaced';
  eventVersion: string;
  timestamp: string;
  data: {
    orderId: string;
    customerId: string;
    items: Array<{
      productId: string;
      quantity: number;
      unitPrice: number;
    }>;
    totalAmount: number;
    currency: string;
    shippingAddress: {
      // Address fields...
    };
  };
  // Other envelope fields...
}

// Initialize consumer
const orderConsumer = new KafkaConsumer({
  groupId: 'inventory-service',
  brokers: ['kafka-1:9092', 'kafka-2:9092', 'kafka-3:9092'],
});

// Initialize service
const orderProcessor = new OrderProcessingService();

// Start consuming events
async function startConsumer() {
  await orderConsumer.subscribe('order-events');
  
  orderConsumer.on('message', async (message) => {
    try {
      // Parse the message
      const rawEvent = JSON.parse(message.value.toString());
      
      // Skip if not the event we're interested in
      if (rawEvent.eventType !== 'OrderPlaced') {
        return;
      }
      
      // Validate against schema
      const isValid = await schemaRegistry.validate(
        rawEvent, 
        'OrderPlaced', 
        rawEvent.eventVersion
      );
      
      if (!isValid) {
        console.error('Invalid event schema', rawEvent);
        return;
      }
      
      // Type-safe processing
      const event = rawEvent as OrderPlacedEvent;
      
      // Process the order
      await orderProcessor.processNewOrder(event.data);
      
      // Commit the offset
      await orderConsumer.commitOffset(message);
      
    } catch (error) {
      console.error('Error processing order event', error);
      // Implement retry/dead-letter logic
    }
  });
}

startConsumer().catch(console.error);
```

## Publishing Events

### Producer Best Practices

1. **Validate before publishing**:
   - Ensure events comply with their schema
   - Verify business rules and data integrity
   - Set appropriate event headers

2. **Include essential metadata**:
   - Generate a unique event ID
   - Set the correct event type and version
   - Include accurate timestamp
   - Set correlation and causation IDs

3. **Handle publishing failures**:
   - Implement retry mechanisms with backoff
   - Store events temporarily if Kafka is unavailable
   - Log failed events for troubleshooting

### Producer Code Example (TypeScript)

```typescript
import { v4 as uuid } from 'uuid';
import { KafkaProducer } from '@flowmart/kafka-client';
import { SchemaRegistry } from '@flowmart/schema-registry';
import { Product } from './models';

// Initialize schema registry client
const schemaRegistry = new SchemaRegistry({
  baseUrl: 'https://schema-registry.flowmart.com',
});

// Initialize producer
const producer = new KafkaProducer({
  clientId: 'product-service',
  brokers: ['kafka-1:9092', 'kafka-2:9092', 'kafka-3:9092'],
});

export class ProductEventService {
  async publishProductCreated(product: Product, correlationId?: string): Promise<void> {
    const eventId = uuid();
    
    const event = {
      eventId,
      eventType: 'ProductCreated',
      eventVersion: '1.0.0',
      timestamp: new Date().toISOString(),
      source: 'product-service',
      data: {
        productId: product.id,
        name: product.name,
        summary: product.description || null,
        sku: product.sku,
        price: {
          amount: product.price,
          currency: 'USD'  // Default to USD
        },
        categories: product.categories || [],
        attributes: product.attributes || {}
      },
      metadata: {
        // Add any additional metadata
      },
      correlationId: correlationId || eventId,
      causationId: null  // No previous event caused this
    };
    
    // Validate against schema
    const isValid = await schemaRegistry.validate(
      event, 
      'ProductCreated', 
      '1.0.0'
    );
    
    if (!isValid) {
      const errors = await schemaRegistry.getValidationErrors(
        event, 
        'ProductCreated', 
        '1.0.0'
      );
      throw new Error(`Invalid event schema: ${JSON.stringify(errors)}`);
    }
    
    // Publish event
    await producer.send({
      topic: 'product-events',
      messages: [
        {
          key: product.id,
          value: JSON.stringify(event),
          headers: {
            'eventType': 'ProductCreated',
            'contentType': 'application/json'
          }
        }
      ]
    });
    
    console.log(`Published ProductCreated event: ${eventId}`);
  }
}
```

## Schema Registry Integration

### Registering a New Schema

```bash
# Using CLI tool
flowmart-schema register \
  --file ./schemas/ProductCreated.json \
  --compatibility BACKWARD

# API endpoint
curl -X POST https://schema-registry.flowmart.com/subjects/ProductCreated/versions \
  -H "Content-Type: application/json" \
  -d @./schemas/ProductCreated.json
```

### Retrieving a Schema

```javascript
// Using JavaScript client
const schema = await schemaRegistry.getSchema('ProductCreated', '1.0.0');

// API endpoint
curl https://schema-registry.flowmart.com/subjects/ProductCreated/versions/latest
```

### Checking Compatibility

```javascript
// Using JavaScript client
const isCompatible = await schemaRegistry.checkCompatibility(
  newSchema, 
  'ProductCreated'
);

// API endpoint
curl -X POST https://schema-registry.flowmart.com/compatibility/subjects/ProductCreated/versions/latest \
  -H "Content-Type: application/json" \
  -d @./schemas/ProductCreated.v2.json
```

## Schema Registry UI

Our Schema Registry includes a web interface at [https://schema-registry.flowmart.com/ui](https://schema-registry.flowmart.com/ui) that provides:

- Browsable catalog of all event schemas
- Schema versioning history
- Compatibility information
- Schema validation tools
- Documentation generation

## Testing Event Schemas

### Unit Testing Schemas

```javascript
import { validateAgainstSchema } from '@flowmart/schema-validator';
import productCreatedSchema from './schemas/ProductCreated.json';

describe('ProductCreated schema', () => {
  it('validates valid events', () => {
    const validEvent = {
      eventId: 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
      eventType: 'ProductCreated',
      eventVersion: '1.0.0',
      timestamp: '2023-09-15T13:25:47.803Z',
      data: {
        productId: 'b3c631a5-f7c8-4d89-a57f-dd2f069b5730',
        name: 'Smartphone X Pro',
        sku: 'SP-XPRO-2023',
        price: {
          amount: 999.99,
          currency: 'USD'
        }
      }
    };
    
    const result = validateAgainstSchema(validEvent, productCreatedSchema);
    expect(result.valid).toBe(true);
  });
  
  it('rejects events with missing required fields', () => {
    const invalidEvent = {
      eventId: 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
      eventType: 'ProductCreated',
      eventVersion: '1.0.0',
      timestamp: '2023-09-15T13:25:47.803Z',
      data: {
        // Missing required productId
        name: 'Smartphone X Pro',
        // Missing required sku
        price: {
          amount: 999.99,
          currency: 'USD'
        }
      }
    };
    
    const result = validateAgainstSchema(invalidEvent, productCreatedSchema);
    expect(result.valid).toBe(false);
    expect(result.errors.length).toBeGreaterThan(0);
  });
});
```

### Integration Testing with Schema Registry

```javascript
describe('Schema Registry Integration', () => {
  it('registers and validates schema', async () => {
    // Register test schema
    await schemaRegistry.registerSchema(
      'TestEvent',
      testEventSchema,
      'BACKWARD'
    );
    
    // Create test event
    const testEvent = {
      eventId: uuid(),
      eventType: 'TestEvent',
      eventVersion: '1.0.0',
      timestamp: new Date().toISOString(),
      data: {
        // Test data...
      }
    };
    
    // Validate against registered schema
    const isValid = await schemaRegistry.validate(
      testEvent,
      'TestEvent',
      '1.0.0'
    );
    
    expect(isValid).toBe(true);
  });
});
```

## Event Documentation

### Self-Documenting Schemas

Use descriptive fields in your JSON Schema to auto-generate documentation:

```json
{
  "title": "ProductCreated",
  "description": "Published when a new product is created in the catalog",
  "properties": {
    "data": {
      "properties": {
        "productId": {
          "description": "Unique identifier for the product",
          "examples": ["p-12345"]
        }
      }
    }
  }
}
```

### Documentation in Code

Document event handling with clear comments:

```typescript
/**
 * Handles the ProductCreated event
 * This event is triggered when a new product is added to the catalog.
 * It updates the inventory service with the new product information.
 * 
 * @param event The ProductCreated event
 * @see https://schema-registry.flowmart.com/ui/schemas/ProductCreated/1.0.0
 */
async function handleProductCreated(event: ProductCreatedEvent): Promise<void> {
  // Implementation...
}
```

## Event Tracing and Debugging

### Correlation IDs

Use correlation IDs to trace requests across services:

```typescript
// When handling an API request
const correlationId = req.headers['x-correlation-id'] || uuid();

// Include in all events
const event = {
  // Other event fields...
  correlationId,
  // If this event was caused by another event
  causationId: previousEvent?.eventId
};
```

### Event Logging

Log event publishing and consumption with consistent format:

```typescript
// Producer logging
logger.info('Publishing event', {
  eventId: event.eventId,
  eventType: event.eventType,
  correlationId: event.correlationId
});

// Consumer logging
logger.info('Consuming event', {
  eventId: event.eventId,
  eventType: event.eventType,
  correlationId: event.correlationId,
  consumer: 'inventory-service'
});
```

## Event Monitoring

Monitor your event streams using our standard observability stack:

1. **Kafka Metrics**: Lag, throughput, errors
2. **Schema Registry Metrics**: Validation failures, compatibility checks
3. **Service Metrics**: Event processing times, failure rates
4. **Custom Dashboards**: Domain-specific event flows

Access dashboards at [https://grafana.flowmart.com/d/events](https://grafana.flowmart.com/d/events)

## Event Schema Governance

### Change Management

1. **Proposal**: Document the schema change with rationale
2. **Review**: Domain experts review for business requirements
3. **Compatibility Check**: Verify with schema registry
4. **Approval**: Get sign-off from service team leads
5. **Publication**: Register schema and announce change

### Schema Review Checklist

✅ Schema follows naming conventions  
✅ Required fields are truly necessary  
✅ Field types are appropriate  
✅ Enums have complete value lists  
✅ Constraints (min, max, etc.) are appropriate  
✅ Documentation is complete  
✅ Versioning follows semantic versioning  
✅ Compatibility type is specified  

## Conclusion

Well-designed event schemas are foundational to reliable event-driven systems. Following FlowMart's event schema guidelines ensures our services can communicate reliably today and evolve confidently tomorrow.

## Next Steps

- Explore [API design best practices](/docs/guides/creating-new-microservices/api-design)
- Understand [Observability in microservices](/docs/guides/creating-new-microservices/observability)
- Learn about [CI/CD for microservices](/docs/guides/creating-new-microservices/cicd-pipeline) 
---
title: New TypeScript service
summary: Guide to implementing microservices using TypeScript at FlowMart
sidebar:
    label: TypeScript Service
    order: 4
---

This guide details the recommended patterns, practices, and tools for implementing TypeScript-based microservices at FlowMart.


## Why TypeScript?

At FlowMart, we recommend TypeScript for new microservices because it offers:

- **Type Safety**: Catch errors during development instead of at runtime
- **Better IDE Support**: Enhanced auto-completion, navigation, and refactoring
- **Self-Documenting Code**: Types serve as documentation for your codebase
- **Enterprise-Ready**: Better maintainability for large codebases and teams
- **Ecosystem Compatibility**: Full access to the Node.js ecosystem

## Prerequisites

Before you begin:

- Install Node.js (v18 or later)
- Familiarize yourself with [our Node.js service guide](/docs/guides/creating-new-microservices/node-service)
- Have basic TypeScript knowledge

## Scaffolding a TypeScript Service

Use our service generator to create a TypeScript service:

```bash
# Install the FlowMart service generator
npm install -g @flowmart/service-generator

# Create a new TypeScript service
flowmart-create-service my-service --type typescript
```

## TypeScript Project Structure

The generated service follows our standard TypeScript structure:

```
my-service/
├── src/
│   ├── api/                 # API definition and controllers
│   ├── config/              # Configuration management
│   ├── domain/              # Domain models and business logic
│   │   ├── models/          # Domain entities and value objects
│   │   └── services/        # Domain services
│   ├── events/              # Event producers and consumers
│   ├── infrastructure/      # External dependencies and adapters
│   ├── repositories/        # Data access layer
│   ├── types/               # TypeScript type definitions
│   ├── utils/               # Utility functions
│   └── app.ts               # Application entry point
├── test/
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── contract/            # Contract tests
├── terraform/               # Infrastructure as code
├── .github/                 # GitHub Actions workflows
├── Dockerfile               # Container definition
├── docker-compose.yml       # Local development setup
├── tsconfig.json            # TypeScript configuration
├── package.json             # Dependencies and scripts
└── README.md                # Service documentation
```

## TypeScript Configuration

Our template includes a pre-configured `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2020"],
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "sourceMap": true,
    "declaration": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "test"]
}
```

## Domain Modeling with TypeScript

TypeScript enables us to model our domain with strong types:

### Example Domain Model

```typescript
// src/domain/models/product.ts
export enum ProductCategory {
  ELECTRONICS = 'electronics',
  CLOTHING = 'clothing',
  GROCERY = 'grocery',
  HOME = 'home',
  BEAUTY = 'beauty'
}

export interface ProductAttributes {
  [key: string]: string | number | boolean;
}

export class Product {
  constructor(
    public readonly id: string,
    public name: string,
    public summary: string,
    public price: number,
    public category: ProductCategory,
    public sku: string,
    public inventoryCount: number,
    public attributes: ProductAttributes = {},
    public isActive: boolean = true,
    public createdAt: Date = new Date(),
    public updatedAt: Date = new Date()
  ) {}

  updateInventory(count: number): void {
    if (count < 0) {
      throw new Error('Inventory count cannot be negative');
    }
    this.inventoryCount = count;
    this.updatedAt = new Date();
  }

  updatePrice(price: number): void {
    if (price < 0) {
      throw new Error('Price cannot be negative');
    }
    this.price = price;
    this.updatedAt = new Date();
  }

  deactivate(): void {
    this.isActive = false;
    this.updatedAt = new Date();
  }

  activate(): void {
    this.isActive = true;
    this.updatedAt = new Date();
  }

  isInStock(): boolean {
    return this.inventoryCount > 0;
  }
}
```

## Repository Pattern with TypeScript

Use interfaces to define repositories:

```typescript
// src/repositories/product-repository.ts
import { Product } from '../domain/models/product';

export interface ProductRepository {
  findById(id: string): Promise<Product | null>;
  findAll(limit?: number, offset?: number): Promise<Product[]>;
  findByCategory(category: string, limit?: number, offset?: number): Promise<Product[]>;
  save(product: Product): Promise<Product>;
  update(product: Product): Promise<Product>;
  delete(id: string): Promise<boolean>;
}

// src/repositories/mongodb-product-repository.ts
import { Collection, MongoClient, ObjectId } from 'mongodb';
import { Product, ProductCategory } from '../domain/models/product';
import { ProductRepository } from './product-repository';
import { logger } from '../infrastructure/observability';

export class MongoDBProductRepository implements ProductRepository {
  private collection: Collection;

  constructor(client: MongoClient) {
    this.collection = client.db('ecommerce').collection('products');
  }

  async findById(id: string): Promise<Product | null> {
    try {
      const result = await this.collection.findOne({ _id: new ObjectId(id) });
      if (!result) return null;
      return this.mapToProduct(result);
    } catch (error) {
      logger.error('Error finding product by id', { error, id });
      throw error;
    }
  }

  async findAll(limit = 100, offset = 0): Promise<Product[]> {
    try {
      const results = await this.collection
        .find({})
        .skip(offset)
        .limit(limit)
        .toArray();
      return results.map(this.mapToProduct);
    } catch (error) {
      logger.error('Error finding all products', { error });
      throw error;
    }
  }

  async findByCategory(category: string, limit = 100, offset = 0): Promise<Product[]> {
    try {
      const results = await this.collection
        .find({ category })
        .skip(offset)
        .limit(limit)
        .toArray();
      return results.map(this.mapToProduct);
    } catch (error) {
      logger.error('Error finding products by category', { error, category });
      throw error;
    }
  }

  async save(product: Product): Promise<Product> {
    try {
      const productDoc = {
        name: product.name,
        summary: product.description,
        price: product.price,
        category: product.category,
        sku: product.sku,
        inventoryCount: product.inventoryCount,
        attributes: product.attributes,
        isActive: product.isActive,
        createdAt: product.createdAt,
        updatedAt: product.updatedAt
      };
      
      const result = await this.collection.insertOne(productDoc);
      return {
        ...product,
        id: result.insertedId.toString()
      };
    } catch (error) {
      logger.error('Error saving product', { error, product });
      throw error;
    }
  }

  async update(product: Product): Promise<Product> {
    try {
      const result = await this.collection.updateOne(
        { _id: new ObjectId(product.id) },
        {
          $set: {
            name: product.name,
            summary: product.description,
            price: product.price,
            category: product.category,
            sku: product.sku,
            inventoryCount: product.inventoryCount,
            attributes: product.attributes,
            isActive: product.isActive,
            updatedAt: product.updatedAt
          }
        }
      );
      
      if (result.matchedCount === 0) {
        throw new Error(`Product with id ${product.id} not found`);
      }
      
      return product;
    } catch (error) {
      logger.error('Error updating product', { error, productId: product.id });
      throw error;
    }
  }

  async delete(id: string): Promise<boolean> {
    try {
      const result = await this.collection.deleteOne({ _id: new ObjectId(id) });
      return result.deletedCount === 1;
    } catch (error) {
      logger.error('Error deleting product', { error, id });
      throw error;
    }
  }

  private mapToProduct(doc: any): Product {
    return new Product(
      doc._id.toString(),
      doc.name,
      doc.description,
      doc.price,
      doc.category as ProductCategory,
      doc.sku,
      doc.inventoryCount,
      doc.attributes,
      doc.isActive,
      new Date(doc.createdAt),
      new Date(doc.updatedAt)
    );
  }
}
```

## Type-safe API Controllers

TypeScript enables type-safe API controllers with Express:

```typescript
// src/api/controllers/product-controller.ts
import { Router, Request, Response, NextFunction } from 'express';
import { ProductService } from '../../domain/services/product-service';
import { validateProduct } from '../middleware/product-validator';
import { tracing } from '../../infrastructure/observability';
import { Product, ProductCategory } from '../../domain/models/product';

export interface CreateProductRequest {
  name: string;
  summary: string;
  price: number;
  category: ProductCategory;
  sku: string;
  inventoryCount: number;
  attributes?: { [key: string]: string | number | boolean };
}

export interface UpdateProductRequest {
  name?: string;
  description?: string;
  price?: number;
  category?: ProductCategory;
  sku?: string;
  inventoryCount?: number;
  attributes?: { [key: string]: string | number | boolean };
  isActive?: boolean;
}

export class ProductController {
  private router: Router;
  
  constructor(private productService: ProductService) {
    this.router = Router();
    this.setupRoutes();
  }
  
  private setupRoutes(): void {
    this.router.get('/', tracing.middleware('get-all-products'), this.getAllProducts.bind(this));
    this.router.get('/:id', tracing.middleware('get-product'), this.getProductById.bind(this));
    this.router.post('/', tracing.middleware('create-product'), validateProduct, this.createProduct.bind(this));
    this.router.put('/:id', tracing.middleware('update-product'), this.updateProduct.bind(this));
    this.router.delete('/:id', tracing.middleware('delete-product'), this.deleteProduct.bind(this));
  }
  
  getRouter(): Router {
    return this.router;
  }
  
  private async getAllProducts(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const limit = req.query.limit ? parseInt(req.query.limit as string, 10) : 100;
      const offset = req.query.offset ? parseInt(req.query.offset as string, 10) : 0;
      const products = await this.productService.getAllProducts(limit, offset);
      res.json(products);
    } catch (error) {
      next(error);
    }
  }
  
  private async getProductById(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const product = await this.productService.getProductById(req.params.id);
      if (!product) {
        res.status(404).json({ error: 'Product not found' });
        return;
      }
      res.json(product);
    } catch (error) {
      next(error);
    }
  }
  
  private async createProduct(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const productData = req.body as CreateProductRequest;
      const product = await this.productService.createProduct(productData);
      res.status(201).json(product);
    } catch (error) {
      next(error);
    }
  }
  
  private async updateProduct(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const productData = req.body as UpdateProductRequest;
      const product = await this.productService.updateProduct(req.params.id, productData);
      if (!product) {
        res.status(404).json({ error: 'Product not found' });
        return;
      }
      res.json(product);
    } catch (error) {
      next(error);
    }
  }
  
  private async deleteProduct(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const success = await this.productService.deleteProduct(req.params.id);
      if (!success) {
        res.status(404).json({ error: 'Product not found' });
        return;
      }
      res.status(204).send();
    } catch (error) {
      next(error);
    }
  }
}
```

## Strongly Typed Event Handling

Create strongly typed event producers and consumers:

```typescript
// src/events/types/event-types.ts
export interface EventMetadata {
  eventId: string;
  timestamp: string;
  service: string;
  correlationId?: string;
  causationId?: string;
}

export interface Event<T> {
  type: string;
  data: T;
  metadata: EventMetadata;
}

export interface ProductCreatedEvent extends Event<{
  id: string;
  name: string;
  price: number;
  category: string;
  sku: string;
  inventoryCount: number;
}> {
  type: 'PRODUCT_CREATED';
}

export interface ProductUpdatedEvent extends Event<{
  id: string;
  changes: {
    name?: string;
    price?: number;
    category?: string;
    inventoryCount?: number;
  };
}> {
  type: 'PRODUCT_UPDATED';
}

export interface InventoryUpdatedEvent extends Event<{
  productId: string;
  quantity: number;
  warehouseId: string;
}> {
  type: 'INVENTORY_UPDATED';
}

// src/events/producers/product-event-producer.ts
import { v4 as uuidv4 } from 'uuid';
import { KafkaClient } from '../../infrastructure/kafka';
import { Product } from '../../domain/models/product';
import { ProductCreatedEvent, ProductUpdatedEvent } from '../types/event-types';

export class ProductEventProducer {
  private readonly topic = 'product-events';
  
  constructor(private kafkaClient: KafkaClient) {}

  async productCreated(product: Product): Promise<void> {
    const event: ProductCreatedEvent = {
      type: 'PRODUCT_CREATED',
      data: {
        id: product.id,
        name: product.name,
        price: product.price,
        category: product.category,
        sku: product.sku,
        inventoryCount: product.inventoryCount
      },
      metadata: {
        eventId: uuidv4(),
        timestamp: new Date().toISOString(),
        service: 'product-service'
      }
    };

    await this.kafkaClient.produce({
      topic: this.topic,
      key: product.id,
      value: JSON.stringify(event)
    });
  }

  async productUpdated(product: Product, changes: Partial<Product>): Promise<void> {
    const event: ProductUpdatedEvent = {
      type: 'PRODUCT_UPDATED',
      data: {
        id: product.id,
        changes: {
          name: changes.name,
          price: changes.price,
          category: changes.category,
          inventoryCount: changes.inventoryCount
        }
      },
      metadata: {
        eventId: uuidv4(),
        timestamp: new Date().toISOString(),
        service: 'product-service'
      }
    };

    await this.kafkaClient.produce({
      topic: this.topic,
      key: product.id,
      value: JSON.stringify(event)
    });
  }
}
```

## Dependency Injection with TypeScript

We use the `inversify` library for dependency injection:

```typescript
// src/infrastructure/ioc/container.ts
import { Container } from 'inversify';
import { MongoClient } from 'mongodb';
import { KafkaClient } from '../kafka';
import { ProductRepository } from '../../repositories/product-repository';
import { MongoDBProductRepository } from '../../repositories/mongodb-product-repository';
import { ProductService } from '../../domain/services/product-service';
import { ProductEventProducer } from '../../events/producers/product-event-producer';
import { ProductController } from '../../api/controllers/product-controller';
import { AppConfig } from '../../config/app-config';
import TYPES from './types';

const container = new Container();

// Config
container.bind<AppConfig>(TYPES.AppConfig).to(AppConfig).inSingletonScope();

// Infrastructure
container.bind<MongoClient>(TYPES.MongoClient).toDynamicValue((context) => {
  const config = context.container.get<AppConfig>(TYPES.AppConfig);
  return new MongoClient(config.mongoDbUri);
}).inSingletonScope();

container.bind<KafkaClient>(TYPES.KafkaClient).toDynamicValue((context) => {
  const config = context.container.get<AppConfig>(TYPES.AppConfig);
  return new KafkaClient(config.kafkaBrokers);
}).inSingletonScope();

// Repositories
container.bind<ProductRepository>(TYPES.ProductRepository).toDynamicValue((context) => {
  const mongoClient = context.container.get<MongoClient>(TYPES.MongoClient);
  return new MongoDBProductRepository(mongoClient);
}).inSingletonScope();

// Event Producers
container.bind<ProductEventProducer>(TYPES.ProductEventProducer).toDynamicValue((context) => {
  const kafkaClient = context.container.get<KafkaClient>(TYPES.KafkaClient);
  return new ProductEventProducer(kafkaClient);
}).inSingletonScope();

// Services
container.bind<ProductService>(TYPES.ProductService).toDynamicValue((context) => {
  const repository = context.container.get<ProductRepository>(TYPES.ProductRepository);
  const eventProducer = context.container.get<ProductEventProducer>(TYPES.ProductEventProducer);
  return new ProductService(repository, eventProducer);
}).inSingletonScope();

// Controllers
container.bind<ProductController>(TYPES.ProductController).toDynamicValue((context) => {
  const service = context.container.get<ProductService>(TYPES.ProductService);
  return new ProductController(service);
}).inSingletonScope();

export default container;

// src/infrastructure/ioc/types.ts
const TYPES = {
  AppConfig: Symbol.for('AppConfig'),
  MongoClient: Symbol.for('MongoClient'),
  KafkaClient: Symbol.for('KafkaClient'),
  ProductRepository: Symbol.for('ProductRepository'),
  ProductEventProducer: Symbol.for('ProductEventProducer'),
  ProductService: Symbol.for('ProductService'),
  ProductController: Symbol.for('ProductController')
};

export default TYPES;
```

## Error Handling with TypeScript

Use custom error classes:

```typescript
// src/utils/errors.ts
export class AppError extends Error {
  constructor(
    public readonly message: string,
    public readonly statusCode: number = 500,
    public readonly code: string = 'INTERNAL_ERROR',
    public readonly details?: any
  ) {
    super(message);
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }
}

export class NotFoundError extends AppError {
  constructor(resource: string, id: string) {
    super(`${resource} with id ${id} not found`, 404, 'NOT_FOUND');
    this.name = this.constructor.name;
  }
}

export class ValidationError extends AppError {
  constructor(message: string, details?: any) {
    super(message, 400, 'VALIDATION_ERROR', details);
    this.name = this.constructor.name;
  }
}

export class ConflictError extends AppError {
  constructor(message: string) {
    super(message, 409, 'CONFLICT_ERROR');
    this.name = this.constructor.name;
  }
}

export class AuthorizationError extends AppError {
  constructor(message: string = 'Unauthorized') {
    super(message, 401, 'UNAUTHORIZED');
    this.name = this.constructor.name;
  }
}

// src/api/middleware/error-handler.ts
import { Request, Response, NextFunction } from 'express';
import { AppError } from '../../utils/errors';
import { logger } from '../../infrastructure/observability';

export function errorHandler(
  error: Error, 
  req: Request, 
  res: Response, 
  next: NextFunction
): void {
  logger.error('Request error', {
    error: error.message,
    stack: error.stack,
    path: req.path,
    method: req.method
  });

  if (error instanceof AppError) {
    res.status(error.statusCode).json({
      error: {
        code: error.code,
        message: error.message,
        details: error.details
      }
    });
    return;
  }

  res.status(500).json({
    error: {
      code: 'INTERNAL_SERVER_ERROR',
      message: 'An unexpected error occurred'
    }
  });
}
```

## Testing TypeScript Services

We use Jest for testing TypeScript services:

```typescript
// test/unit/domain/services/product-service.test.ts
import { ProductService } from '../../../../src/domain/services/product-service';
import { Product, ProductCategory } from '../../../../src/domain/models/product';
import { NotFoundError } from '../../../../src/utils/errors';

describe('ProductService', () => {
  const mockProduct = new Product(
    '1',
    'Test Product',
    'Test Description',
    9.99,
    ProductCategory.ELECTRONICS,
    'TEST-123',
    100
  );

  const mockRepository = {
    findById: jest.fn(),
    findAll: jest.fn(),
    findByCategory: jest.fn(),
    save: jest.fn(),
    update: jest.fn(),
    delete: jest.fn()
  };

  const mockEventProducer = {
    productCreated: jest.fn(),
    productUpdated: jest.fn()
  };

  const productService = new ProductService(mockRepository, mockEventProducer);

  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('getProductById', () => {
    it('should return a product when found', async () => {
      mockRepository.findById.mockResolvedValue(mockProduct);
      
      const result = await productService.getProductById('1');
      
      expect(result).toEqual(mockProduct);
      expect(mockRepository.findById).toHaveBeenCalledWith('1');
    });

    it('should return null when product not found', async () => {
      mockRepository.findById.mockResolvedValue(null);
      
      const result = await productService.getProductById('999');
      
      expect(result).toBeNull();
      expect(mockRepository.findById).toHaveBeenCalledWith('999');
    });
  });

  describe('createProduct', () => {
    it('should create and return a new product', async () => {
      const productData = {
        name: 'New Product',
        summary: 'New Description',
        price: 19.99,
        category: ProductCategory.CLOTHING,
        sku: 'NEW-123',
        inventoryCount: 50
      };
      
      mockRepository.save.mockImplementation(product => Promise.resolve(product));
      
      const result = await productService.createProduct(productData);
      
      expect(result).toMatchObject(productData);
      expect(mockRepository.save).toHaveBeenCalledTimes(1);
      expect(mockEventProducer.productCreated).toHaveBeenCalledWith(expect.objectContaining(productData));
    });
  });

  describe('updateProduct', () => {
    it('should update and return the product', async () => {
      const changes = { price: 29.99, inventoryCount: 75 };
      const updatedProduct = { ...mockProduct, ...changes };
      
      mockRepository.findById.mockResolvedValue(mockProduct);
      mockRepository.update.mockResolvedValue(updatedProduct);
      
      const result = await productService.updateProduct('1', changes);
      
      expect(result).toEqual(updatedProduct);
      expect(mockRepository.findById).toHaveBeenCalledWith('1');
      expect(mockRepository.update).toHaveBeenCalledWith(expect.objectContaining(changes));
      expect(mockEventProducer.productUpdated).toHaveBeenCalledWith(
        expect.anything(),
        expect.objectContaining(changes)
      );
    });

    it('should throw NotFoundError when product not found', async () => {
      mockRepository.findById.mockResolvedValue(null);
      
      await expect(productService.updateProduct('999', { price: 29.99 }))
        .rejects
        .toThrow(NotFoundError);
      
      expect(mockRepository.update).not.toHaveBeenCalled();
      expect(mockEventProducer.productUpdated).not.toHaveBeenCalled();
    });
  });
});
```

## Building and Packaging TypeScript Services

Our template includes optimized build scripts:

```json
// package.json (excerpt)
{
  "scripts": {
    "build": "tsc",
    "start": "node dist/app.js",
    "dev": "ts-node-dev --respawn --transpile-only src/app.ts",
    "lint": "eslint src --ext .ts",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

## Dockerizing TypeScript Services

Our Docker setup uses multi-stage builds for optimal container size:

```dockerfile
# Dockerfile
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY tsconfig.json ./
COPY src/ ./src/

RUN npm run build

FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --production

COPY --from=builder /app/dist ./dist

ENV NODE_ENV=production
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget -qO- http://localhost:3000/health || exit 1

CMD ["node", "dist/app.js"]
```

## CI/CD for TypeScript Services

Our CI/CD workflow ensures proper TypeScript builds:

```yaml
# .github/workflows/main.yml (excerpt)
jobs:
  test:
    name: Test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm test
      
  build:
    name: Build and Push
    needs: test
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      - run: npm ci
      - run: npm run build
      # Then Docker build and push steps...
```

## TypeScript Best Practices at FlowMart

1. **Use Interfaces for Public APIs**: Define interfaces for repositories, services, and controllers.

2. **Embrace Type Inference**: Let TypeScript infer types where it makes sense to reduce verbosity.

3. **Use Discriminated Unions**: For handling different event types or command patterns.

4. **Leverage Utility Types**: Use built-in utility types like `Partial<T>`, `Readonly<T>`, `Pick<T>`, etc.

5. **Strict Null Checks**: Always enable `strictNullChecks` to prevent null/undefined errors.

6. **Immutability**: Use `readonly` properties and `const` variables to enforce immutability.

7. **Error Handling**: Use custom error classes with type information.

8. **Asynchronous Code**: Use `async/await` consistently with proper error handling.

9. **Use Enums for Constants**: Define related constants as TypeScript enums.

10. **Module Structure**: Organize code into cohesive modules with clear interfaces.

## Recommended Libraries

- **Express.js**: Web framework
- **inversify**: Dependency injection
- **zod**: Runtime validation
- **winston**: Logging
- **prom-client**: Prometheus metrics
- **jaeger-client**: Distributed tracing
- **mongodb**: Database driver
- **kafkajs**: Kafka client
- **jest**: Testing framework
- **supertest**: API testing
- **ts-node-dev**: Development server

## Next Steps

- Learn about [Database patterns for microservices](/docs/guides/creating-new-microservices/database-patterns)
- Understand [Event schema design](/docs/guides/creating-new-microservices/event-schemas)
- Explore [API design best practices](/docs/guides/creating-new-microservices/api-design) 
---
title: Getting Started with Event Storming
summary: Learn how to use Event Storming to discover and model your business domain effectively
sidebar:
    label: Introduction
    order: 1
owners: 
  - dboyne
badges:
  - content: 'Guide'
    backgroundColor: 'teal'
    textColor: 'teal'
---

# Introduction to Event Storming

Event Storming is a collaborative modeling technique that helps teams explore complex business domains. It was introduced by Alberto Brandolini and has become a valuable tool in Domain-Driven Design (DDD) and Event-Driven Architecture (EDA).

## Why Event Storming?

At FlowMart, we use Event Storming because it:

- Brings together domain experts and technical teams
- Helps identify domain events, commands, and aggregates
- Aligns perfectly with our event-driven architecture
- Facilitates better understanding of business processes
- Helps in defining service boundaries and responsibilities

## Example Event Storming Session

Here is an example of an event storming session for the Orders domain.

<Miro boardId="uXjVIHCImos=/" moveToWidget="3074457347671667709" edit={false} />

## Event Storming Example in Lucid Chart

<Lucid diagramId="e29f42a0-67e2-4f80-b0d7-6922bb7dd9c5" />

## Git workflow 

<DrawIO url="https://viewer.diagrams.net/?border=0&tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20id%3D%22yPxyJZ8AM_hMuL3Unpa9%22%20name%3D%22complex%20gitflow%22%3E7V1dm6I2FP41c6kP4ZvL0dHd7bbbbWf7tNubPhmJSheIhTjj7K9vwoeiiRgREGfZi1kJECDvez5yzoHcaeNg8y6Cq%2BUv2EX%2Bnaq4mzvt4U5VgaIq9D%2FW8pq2mEBLGxaR52YH7Roeve8oPzNrXXsuivcOJBj7xFvtN85wGKIZ2WuDUYRf9g%2BbY3%2F%2Fqiu4QFzD4wz6fOufnkuWWStQlN2O98hbLLNL20a2I4D5wVlDvIQufik0aZM7bRxhTNJfwWaMfDZ4%2Bbik502P7N3eWIRCInPC%2Bs8%2Fwk%2BTB%2FP9xFfhR2Puwg9PAyvt5Rn66%2ByB32My9za0bYyDwCPZvZPXfEAI2tDLjZYk8GkDoD9jEuFvaIx9HNGWEIf0yNHc8%2F2DJuh7i5BuzugNI9o%2BekYR8ehQ32c7As912WVGL0uPoMcVnLFrvlBi0TZMj577yQAu6XGInjDihyAbFdYz2hSasiF5h3CASPRKD8n26qo1VI30rIyilKTp9ssOcDsDcVmAWsvaYEaxxbbzHQr0RwbEGaDYHCgcCsilLM02cUSWeIFD6E92raMIr0MXscso%2B3D9iwh5zQQNrglmY7vt4WeMV9lxKx964eApuYcRCt17Jk07NGnL1GPPlfSfciCXEJ1jxR0dreRfciYdpL%2ByE5ONr2xjaOSbD5vizofX4tZnFHl0lBl%2FksajFIjxOpqhklHONQyB0QJl5zrL0cfPD9%2BxR15WH0bu9%2BnDb9YAZHRgYy5DKdVROUoBcJwrWUefsUcfYUdM%2FXQv6a1nJx6Qbntf1XnoVKDdbB09J6wDZRxEG4%2F8VfhdIADdOsT4JGH4E8rZKisCPKvnOCTZicConX7iAw1J%2BkXIh8R73jdctSun%2FL7LtFOu2H%2BGT8j%2FjGOPeJgp%2BCdMCA4Emp%2BwIedtyp4%2BWcIV6z7YLJinMWS2YLaEERnicMCs8D8RmiOKAxv1feVFT3A9ClCJiaL6aWRMtCkq1Vw12BvV5MQaOLy90Vq1NxKQXiT5QuESCGFRQ5xtcLpiVnIv9aRcK07dgi22JJamD3Vn9%2B%2B6RgUoxvXJVWp%2BdjxhG6%2BFjbMN0zmUO5%2FxzBhNYeD5rN8xJaZHO1OVT%2Bgl27mnwxynXIfVyWy9WyYr19I3b7KOmyaRMZvUY7JMtXsma6s83yCmGkUV3DeLqW2C7mGq1uGGXDzvFXkW5Zr5KB4SmlJSUeag1jK1BHmM6lgXqSlozgXQOKADKicc2F0KNRUnftuJYHar4JQtrkNgtQNhVThhNQTCqqtNCaterxd3QXDgBub6hqw%2BsLrlOBm3Y2RX62jl1%2BE6PRgTO7mLGqRW05yhdaCvbXBlM2t2RnLfYljPkhX12mf%2Fl7GCzwT1on5WIkk3uyfqdi%2FqDYq6IyvqoFuifkNT506KuqF3z6qrfAwfDMFQGVBOIRijBiZXPpqTNzG1snk0%2BVCIqgvgVJuC05IIWZ4bC2klC1NdnZqy6tSSDZq0o06tKvmMGpDJLOp2o9XUw56T0ALmHUuCOzVHP%2FocVks5LGnC2WqnCGf2PtuF0zPATc8088o%2Bm1VLod%2B16y6qC6MlWwJldSssat1QCVQnhdEAeueEMc9%2B3rYwtmxOLdlop9Mt%2F83qo50XSrDTPQkGSs3hzkumZT%2BEN%2B1I5zUV2Rr6luZvfWLzwpowp4PuNG%2FBXfSMfApLH%2Fw8Gvy0eBx1DkcH8Dg2FvvMQ%2Bk%2FUOwzjzacDkt0q7I2v%2B9ej1b1oxTlUP50nS%2FtancmZF3fjeqDm1W0iC6pRTo2G8vvu9ciVb0xADqnRWzeG%2Fvpw%2B%2F3A80YDNAGBmwUVWWOIFlHfXa61EE7RNbgkG03OW3z0ZMvS4Zm5m4HKKk2x2wc4lWU1p4%2FRTCcLW8UaKWKvj4DY4Nzwm3eCW8ZZD458ZWyuyizPaZnYaqbVxdcPouYCu62SKiHtPSlKU5MlWsXCjl8LiqFNH2jZoun6bPRf6Lyay7Idjh6hLlSMO5jMLwfBQqlvu2ALBMR2c1OZj6MY29W5v6e9FzOHuSTc4kTbyrlbRe%2B7E4lktO7hp67UCdecOM%2FwmIIejvoq%2BmPsEiEWHrs0xMECtrSqyGvWaf7ahp5%2FjXJHnkxWipf3aPmCf1zkVf51AbXV%2BPfyOAV%2Fhe4uNPuaVtS1t2A%2BW7uXdkaDLPhKNz76pbAMoM2fS%2Bg8BJagEn58WBS%2BY%2BWiWCy2kVJotijr%2Bw59g2Xm8vtb%2B%2B8DydXlGJBcv%2Fq7zcBUOU1i7645xINYEprgI69y6xI1HL2GqBEA1j8TKoDGoBHteBtqT%2Bet2UD3tsy7Ws7xTJfEmhp2pqXEexKB77eFSoHhGUEUgpz%2Fhj%2BbTyHX7%2FE%2Ftj4BKOPQfTPQDap3s6U2ALcF75MzagaCBP0piuNhUOEw9vHQGWhtxWuHECzKgIv6kttLAIqBF7kzqfpjHgFwz0GmP%2Bt2ef0R0zxDzIdzsxDpsa3%2B%2FMsyBQlyxXMI8RSJtTfow%2FluvRviAmKE3SSRCd8wms2KCRJrawiPEMx243n9E%2BAooUXLthjhEkXRJhTG4qSMGkLHZb0UW4qN6PK5Gbq%2B3KyJYrI8hlVYGpbTVWULdM8LkayBq9M7Qvo6XrPQnbyPNwndCPcPMzao3h4lH7b5uQJelKW1W%2BqQ3P%2F03y6zZNSB7aQlFpTpJR4XbiFEmoRMHWuCFHdV8u8ZImprSZp2i%2FNYAg%2Bsmsf%2BOhH7Cx1eeBr4bAVOyCudKmjOZGTp9Af6X3UavpFL0hXM%2F2MLArj3yBOCJlMGsFqI1THE8hKJig7FgmwqwjFKBlSBaYq1l3PknDB1sof16U3oTVBu1rT0Q9qGoEhmLaqouiCfbbC%2FCNG0a9P%2F7LFoVTFZ9Ge9NTJtgjV9eAigkFCkCgD%2BQVH35IRo%2Bh5dH4Ao9wI7%2BjyziOD9JgdgZSEWuwWfS%2F8ll5pSQhbreqe3aE6DZ89NJxhernpCseMVVM4iNczZrbna3%2BwoL2mJpoa7kGQrqg1TfvMhUW4To1aGPNMuHjiidhxqLEPqltzkpg1RS04VSL4li1blqmmEhu6WaBAKSVyIWYEWEZovqdY6kHxUNXU1Guue%2BC%2B4mmdg1oNHKyBY9tswevBdjF4abTOr0eErqcerG5Aw4u%2FEBy1QfHnfA%2Fxsl8SacQ%2B4JRiavGL6B06r9IBJ0FfupwjXMHrFCN%2FfEr%2FViJOfQyqmvIy%2BPUXBHkxYIq9F7tEsmSn%2B2LXrxuvTB9%2BW%2FcWFvEqXfLxCp%2F2FWtFw%2BTq3xpcuKt0TG4hqX5kxR2qDSb35sg0Oe3FltexDd0Q5NWn9ngyHtejP3Ref7S57I4QV5PXHXtFjIBD%2BY2n1XXVPgxPNFfDSDd3S0CnorpbSFub%2FA8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E" />

## Key Concepts

### Domain Events
- Represent something significant that has happened in the business domain
- Written in past tense (e.g., "Order Placed", "Payment Received")
- Captured on orange sticky notes during the session

### Commands
- Triggers that cause domain events
- Written in imperative form (e.g., "Place Order", "Process Payment")
- Captured on blue sticky notes

### Aggregates
- Business entities that ensure consistency
- Group related events and commands
- Captured on yellow sticky notes

### Policies
- Business rules that react to events
- Automated processes or human workflows
- Captured on purple sticky notes

## Event Storming Levels

1. **Big Picture Event Storming**
   - High-level view of the entire business domain
   - Focuses on major events and workflows
   - Helps identify bounded contexts

2. **Process Level Event Storming**
   - Detailed view of specific processes
   - Includes commands, policies, and external systems
   - Helps design individual services

3. **Software Design Level Event Storming**
   - Technical perspective of the domain
   - Includes aggregates, entities, and value objects
   - Leads to implementation decisions

## Benefits for FlowMart

Event Storming has helped us:
- Design our microservices architecture
- Identify service boundaries
- Define event contracts between services
- Improve collaboration between teams
- Reduce misunderstandings and rework

## Prerequisites for Event Storming

To conduct an effective Event Storming session, you'll need:

- A large modeling space (physical or virtual)
- Sticky notes in different colors
- Domain experts and technical team members
- A skilled facilitator
- 2-4 hours of uninterrupted time

## Next Steps

Continue reading to learn:
- [How to Facilitate an Event Storming Session](/docs/guides/event-storming/02-facilitation)
- [From Event Storming to Implementation](/docs/guides/event-storming/03-implementation) 
---
title: Facilitating an Event Storming Session
summary: A comprehensive guide on how to run effective Event Storming workshops at FlowMart
sidebar:
    label: Facilitation Guide
    order: 2
owners: 
  - dboyne
badges:
  - content: 'Guide'
    backgroundColor: 'teal'
    textColor: 'teal'
---

# Facilitating an Event Storming Session

This guide will help you run effective Event Storming sessions at FlowMart, ensuring you get the most value from this collaborative modeling technique.

## Pre-Session Preparation

### 1. Define the Scope
- Identify the business domain or process to explore
- Set clear objectives for the session
- Determine the appropriate level (Big Picture, Process, or Design)

### 2. Invite the Right People
- Domain experts who understand the business processes
- Technical team members who will implement the solution
- Product owners and stakeholders
- Limit to 8-12 participants for optimal interaction

### 3. Prepare the Space
- Large continuous wall space or virtual whiteboard
- Sticky notes in different colors:
  - Orange: Domain Events
  - Blue: Commands
  - Yellow: Aggregates
  - Purple: Policies
  - Pink: External Systems
  - Red: Problems/Questions

## Running the Session

### 1. Introduction (15 minutes)
- Explain Event Storming concepts and notation
- Set ground rules:
  - No laptops/phones unless necessary
  - Everyone participates
  - No wrong answers
  - Focus on the business process

### 2. Event Discovery (45-60 minutes)
- Start with "What happens in this domain?"
- Let participants write domain events on orange stickies
- Place events on the timeline (left to right)
- Don't worry about order initially

### 3. Timeline Organization (30 minutes)
- Review all events as a group
- Organize events chronologically
- Identify missing events
- Group related events together

### 4. Adding Detail (60-90 minutes)
- Add commands (blue) that trigger events
- Identify external systems (pink)
- Mark problem areas (red)
- Add policies and reactions (purple)

### 5. Identifying Boundaries (45 minutes)
- Group related concepts
- Look for natural service boundaries
- Discuss integration points
- Identify aggregates (yellow)

## Common Challenges and Solutions

### Challenge: Dominant Participants
- Actively engage quieter participants
- Use round-robin techniques
- Split into smaller groups temporarily

### Challenge: Too Much Detail
- Keep focus on relevant abstraction level
- Park detailed discussions for later
- Use "parking lot" for important but off-topic items

### Challenge: Losing Focus
- Take regular breaks (10 minutes every hour)
- Use timeboxing for each activity
- Keep referring back to session goals

## Remote Facilitation Tips

When running remote Event Storming sessions:

- Use tools like Miro or Mural
- Pre-create templates and sticky note colors
- Use breakout rooms for small group discussions
- Schedule more frequent but shorter sessions
- Use video to maintain engagement

## Post-Session Activities

1. **Documentation**
   - Photograph or export the board
   - Capture key insights and decisions
   - Document identified bounded contexts

2. **Follow-up**
   - Schedule deep-dive sessions for specific areas
   - Create action items and assign owners
   - Plan next steps for implementation

3. **Review and Refine**
   - Review findings with stakeholders
   - Validate assumptions
   - Plan additional sessions if needed

## Measuring Success

A successful Event Storming session should:
- Create shared understanding
- Identify key domain events and processes
- Highlight potential problems and solutions
- Generate actionable next steps
- Engage all participants effectively

## Next Steps

Continue to [From Event Storming to Implementation](/docs/guides/event-storming/03-implementation) to learn how to turn your Event Storming insights into working software. 
---
title: From Event Storming to Implementation
summary: Learn how to transform Event Storming outcomes into concrete microservice implementations at FlowMart
sidebar:
    label: Implementation
    order: 3
owners: 
  - dboyne
badges:
  - content: 'Guide'
    backgroundColor: 'teal'
    textColor: 'teal'
---

# From Event Storming to Implementation

This guide will help you transform the insights gained from Event Storming sessions into concrete microservice implementations at FlowMart.

## Translating Event Storming Artifacts

### Domain Events to Event Schema
Convert orange sticky notes (domain events) into event schemas:

```typescript
// Example Event Schema for "OrderPlaced"
interface OrderPlacedEvent {
  eventType: 'OrderPlaced';
  orderId: string;
  customerId: string;
  orderItems: OrderItem[];
  totalAmount: number;
  timestamp: string;
}
```

### Commands to API Endpoints
Transform blue sticky notes (commands) into API endpoints:

```typescript
// Example API endpoint for "PlaceOrder"
@POST
@Path("/orders")
async placeOrder(orderRequest: OrderRequest): Promise<OrderResponse> {
  // Implementation
}
```

### Aggregates to Service Boundaries
Convert yellow sticky notes (aggregates) into service definitions:

```typescript
// Example Order Service
@Service
class OrderService {
  private readonly orderRepository: OrderRepository;
  private readonly eventPublisher: EventPublisher;
  
  async createOrder(order: Order): Promise<Order> {
    // Implementation
  }
}
```

## Implementation Steps

### 1. Define Service Boundaries
- Use bounded contexts identified during Event Storming
- Create new service repositories using our [templates](/docs/guides/creating-new-microservices)
- Define service interfaces and contracts

### 2. Design Event Schemas
- Create event schemas for all domain events
- Use our [schema registry](/docs/technical-architecture-design/schema-registry)
- Version schemas appropriately
- Document event ownership and consumers

### 3. Implement Commands
- Create API endpoints for commands
- Implement command handlers
- Add validation and error handling
- Document API contracts using OpenAPI

### 4. Set Up Event Publishing
- Implement event publishers
- Configure Kafka topics
- Set up dead letter queues
- Implement retry mechanisms

### 5. Create Event Subscribers
- Implement event handlers
- Set up consumer groups
- Handle failure scenarios
- Implement idempotency

## Example Implementation Flow

Here's a typical flow from Event Storming to implementation:

1. **Event Storming Identifies**:
   - Domain Event: "OrderPlaced"
   - Command: "PlaceOrder"
   - Aggregate: "Order"

2. **Create Service Structure**:
```typescript
// Service structure based on Event Storming
src/
  ├── domain/
  │   ├── Order.ts
  │   └── OrderItem.ts
  ├── commands/
  │   └── PlaceOrderCommand.ts
  ├── events/
  │   └── OrderPlacedEvent.ts
  └── api/
      └── OrderController.ts
```

3. **Implement Domain Model**:
```typescript
class Order {
  private readonly items: OrderItem[];
  private status: OrderStatus;

  placeOrder(): OrderPlacedEvent {
    // Implementation
    return new OrderPlacedEvent(this);
  }
}
```

## Best Practices

### Event Design
- Use past tense for event names
- Include all necessary context
- Follow our [event naming conventions](/docs/technical-architecture-design/event-naming)
- Version events appropriately

### Service Design
- Keep services focused on single bounded context
- Implement proper error handling
- Add comprehensive logging
- Include monitoring and metrics

### Testing Strategy
- Unit test domain logic
- Integration test event flows
- Contract test event schemas
- End-to-end test critical paths

## Common Pitfalls

1. **Too Many Events**
   - Solution: Focus on meaningful state changes
   - Combine related events when appropriate

2. **Tight Coupling**
   - Solution: Use event-driven communication
   - Avoid direct service-to-service calls

3. **Missing Context**
   - Solution: Include necessary data in events
   - Document event purpose and usage

## Monitoring and Observability

Implement proper monitoring for:
- Event processing metrics
- Command execution times
- Error rates and types
- Service health indicators

## Example: Order Processing Flow

Here's a complete example of implementing an order processing flow:

1. **Event Storming Identified**:
   - Command: "PlaceOrder"
   - Event: "OrderPlaced"
   - Event: "PaymentProcessed"
   - Policy: "Send Order Confirmation"

2. **Implementation**:
```typescript
// Command Handler
async function handlePlaceOrder(command: PlaceOrderCommand) {
  const order = new Order(command.orderDetails);
  const event = order.placeOrder();
  await eventPublisher.publish('order-events', event);
  return order;
}

// Event Handler
async function handleOrderPlaced(event: OrderPlacedEvent) {
  await paymentService.processPayment(event.orderId);
  await notificationService.sendConfirmation(event.orderId);
}
```

## Next Steps

1. Review our [service templates](/docs/guides/creating-new-microservices)
2. Study our [event schema guidelines](/docs/technical-architecture-design/event-schemas)
3. Explore our [monitoring setup](/docs/operations-and-support/monitoring)

Remember: Event Storming is an iterative process. As you implement and learn more about the domain, you may need to revisit and refine your model. Keep the dialogue open between domain experts and developers throughout the implementation phase. 
---
title: Inventory Service - Runbook
summary: Operational runbook for troubleshooting and maintaining the InventoryService
sidebar:
    label: InventoryService
    order: 2
owners:
    - order-management
badges:
   - content: 🚀 Operational Procedures
     textColor: white
     backgroundColor: blue
   - content: 🚨 Troubleshooting Guide
     textColor: white
     backgroundColor: red
   - content: 🔄 Maintenance Schedule
     textColor: white
     backgroundColor: yellow
---

This runbook provides operational procedures for the InventoryService, which is responsible for managing product inventory and stock levels across the FlowMart e-commerce platform.

## Architecture

The InventoryService is responsible for:
- Managing product inventory and stock levels
- Reserving inventory for pending orders
- Tracking inventory across warehouses and locations
- Providing real-time availability information
- Triggering restock notifications

### Service Dependencies

```mermaid
flowchart TD
    InventoryService --> PostgresDB[(PostgreSQL Database)]
    InventoryService --> Redis[(Redis Cache)]
    InventoryService --> EventBus[Event Bus]
    InventoryService --> WarehouseSystem[Warehouse Management System]
```

## Monitoring and Alerting

### Key Metrics

| Metric | Description | Warning Threshold | Critical Threshold |
|--------|-------------|-------------------|-------------------|
| `inventory_check_rate` | Inventory availability checks per minute | > 1000 | > 5000 |
| `inventory_check_latency` | Time to check inventory availability | > 100ms | > 500ms |
| `inventory_update_latency` | Time to update inventory levels | > 200ms | > 1s |
| `low_stock_items` | Number of items with low stock | > 50 | > 100 |
| `connection_pool_usage` | Database connection pool utilization | > 70% | > 90% |
| `redis_hit_rate` | Cache hit rate | < 80% | < 60% |

### Dashboards

- [InventoryService Overview](https://grafana.flowmart.com/d/inventory-overview)
- [Stock Level Alerts](https://grafana.flowmart.com/d/inventory-stock-alerts)
- [Database Performance](https://grafana.flowmart.com/d/inventory-database)

### Common Alerts

| Alert | Description | Troubleshooting Steps |
|-------|-------------|----------------------|
| `InventoryServiceHighLatency` | API latency exceeds thresholds | See [High Latency](#high-latency) |
| `InventoryServiceDatabaseIssues` | Database connection or performance issues | See [Database Issues](#database-issues) |
| `InventoryServiceCacheFailure` | Redis cache unavailable or performance degraded | See [Cache Issues](#cache-issues) |
| `InventoryServiceOutOfStock` | Critical products out of stock | See [Stock Management](#stock-management) |

## Troubleshooting Guides

### High Latency

If the service is experiencing high latency:

1. **Check system resource usage**:
   ```bash
   kubectl top pods -n inventory
   ```

2. **Check database connection pool**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl localhost:8080/actuator/metrics/hikaricp.connections.usage
   ```

3. **Check cache hit rate**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl localhost:8080/actuator/metrics/cache.gets | grep "hit_ratio"
   ```

4. **Check for slow queries** in the database:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- psql -U postgres -c "SELECT query, calls, mean_exec_time FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10;"
   ```

5. **Scale the service** if needed:
   ```bash
   kubectl scale deployment inventory-service -n inventory --replicas=5
   ```

### Database Issues

If there are database connection or performance issues:

1. **Check PostgreSQL status**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- pg_isready -U postgres
   ```

2. **Check for long-running transactions**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- psql -U postgres -c "SELECT pid, now() - xact_start AS duration, state, query FROM pg_stat_activity WHERE state != 'idle' ORDER BY duration DESC;"
   ```

3. **Check for table bloat**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- psql -U postgres -c "SELECT schemaname, relname, n_live_tup, n_dead_tup, (n_dead_tup::float / n_live_tup::float) AS dead_ratio FROM pg_stat_user_tables WHERE n_live_tup > 1000 ORDER BY dead_ratio DESC;"
   ```

4. **Restart database connections** in the application if needed:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl -X POST localhost:8080/actuator/restart-db-connections
   ```

### Cache Issues

If there are Redis cache issues:

1. **Check Redis status**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=redis -n data -o jsonpath='{.items[0].metadata.name}') -n data -- redis-cli ping
   ```

2. **Check Redis memory usage**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=redis -n data -o jsonpath='{.items[0].metadata.name}') -n data -- redis-cli info memory
   ```

3. **Check cache hit rate**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=redis -n data -o jsonpath='{.items[0].metadata.name}') -n data -- redis-cli info stats | grep hit_rate
   ```

4. **Clear cache** if necessary:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl -X POST localhost:8080/actuator/caches/clearAll
   ```

### Stock Management

For critical stock issues:

1. **Identify products with low or no stock**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl localhost:8080/internal/api/inventory/low-stock
   ```

2. **Check for stuck inventory reservations**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl localhost:8080/internal/api/inventory/stuck-reservations
   ```

3. **Release expired reservations** if necessary:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl -X POST localhost:8080/internal/api/inventory/release-expired-reservations
   ```

4. **Manually update inventory levels** for emergency corrections:
   ```bash
   curl -X PUT https://api.internal.flowmart.com/inventory/products/{productId}/stock \
     -H "Authorization: Bearer $ADMIN_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"warehouseId": "WAREHOUSE_ID", "quantity": 100, "reason": "Manual correction"}'
   ```

## Common Operational Tasks

### Scaling the Service

To scale the service horizontally:

```bash
kubectl scale deployment inventory-service -n inventory --replicas=<number>
```

### Restarting the Service

To restart all pods:

```bash
kubectl rollout restart deployment inventory-service -n inventory
```

### Database Maintenance

For routine database maintenance:

1. **Run VACUUM ANALYZE to optimize tables**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- psql -U postgres -c "VACUUM ANALYZE inventory_items;"
   ```

2. **Update database statistics**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- psql -U postgres -c "ANALYZE;"
   ```

### Reconcile Inventory

To reconcile inventory with the warehouse management system:

```bash
kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl -X POST localhost:8080/internal/api/inventory/reconcile
```

### Manually Trigger Restock Notifications

To trigger restock notifications for low stock items:

```bash
kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl -X POST localhost:8080/internal/api/inventory/trigger-restock-notifications
```

## Recovery Procedures

### Database Failure Recovery

If the PostgreSQL database becomes unavailable:

1. Verify the status of the PostgreSQL cluster:
   ```bash
   kubectl get pods -l app=postgresql -n data
   ```

2. If the primary instance is down, check if automatic failover has occurred:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql-patroni -n data -o jsonpath='{.items[0].metadata.name}') -n data -- patronictl list
   ```

3. If automatic failover has not occurred, initiate manual failover:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql-patroni -n data -o jsonpath='{.items[0].metadata.name}') -n data -- patronictl failover
   ```

4. Once database availability is restored, validate the InventoryService functionality:
   ```bash
   curl -X GET https://api.internal.flowmart.com/inventory/health
   ```

### Cache Failure Recovery

If the Redis cache becomes unavailable:

1. Verify Redis cluster status:
   ```bash
   kubectl get pods -l app=redis -n data
   ```

2. If needed, restart the Redis cluster:
   ```bash
   kubectl rollout restart statefulset redis -n data
   ```

3. The InventoryService will fall back to database queries when the cache is unavailable.

4. When the cache is restored, you can warm it up:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=inventory-service -n inventory -o jsonpath='{.items[0].metadata.name}') -n inventory -- curl -X POST localhost:8080/internal/api/inventory/warm-cache
   ```

## Disaster Recovery

### Complete Service Failure

In case of a complete service failure:

1. Initiate incident response by notifying the on-call team through PagerDuty.

2. Verify the deployment status:
   ```bash
   kubectl describe deployment inventory-service -n inventory
   ```

3. If necessary, restore from a previous version:
   ```bash
   kubectl rollout undo deployment inventory-service -n inventory
   ```

4. If the primary region is experiencing issues, fail over to the secondary region:
   ```bash
   ./scripts/dr-failover.sh inventory-service
   ```

5. Verify the service is functioning in the secondary region:
   ```bash
   curl -X GET https://api-dr.internal.flowmart.com/inventory/health
   ```

## Maintenance Tasks

### Deploying New Versions

```bash
kubectl set image deployment/inventory-service -n inventory inventory-service=ecr.aws/flowmart/inventory-service:$VERSION
```

### Database Schema Updates

For database schema updates:

1. Notify stakeholders through the #maintenance Slack channel.

2. Set InventoryService to maintenance mode:
   ```bash
   curl -X POST https://api.internal.flowmart.com/inventory/admin/maintenance -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" -d '{"maintenanceMode": true, "message": "Database schema update"}'
   ```

3. Apply the database migrations:
   ```bash
   kubectl apply -f inventory-flyway-job.yaml
   ```

4. Verify migration completion:
   ```bash
   kubectl logs -l job-name=inventory-flyway-migration -n inventory
   ```

5. Turn off maintenance mode:
   ```bash
   curl -X POST https://api.internal.flowmart.com/inventory/admin/maintenance -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" -d '{"maintenanceMode": false}'
   ```

## Contact Information

**Primary On-Call:** Inventory Team (rotating schedule)  
**Secondary On-Call:** Platform Team  
**Escalation Path:** Inventory Team Lead > Engineering Manager > CTO

**Slack Channels:**
- #inventory-support (primary support channel)
- #inventory-alerts (automated alerts)
- #incident-response (for major incidents)

## Reference Information

- [InventoryService API Documentation](https://docs.internal.flowmart.com/inventory/api)
- [Architecture Diagram](https://docs.internal.flowmart.com/architecture/inventory)
- [Service Level Objectives (SLOs)](https://docs.internal.flowmart.com/slo/inventory)
- [Database Schema](https://docs.internal.flowmart.com/inventory/database-schema) 
---
title: OrdersService Runbook
summary: Operational runbook for troubleshooting and maintaining the OrdersService
sidebar:
    label: OrdersService
    order: 1
---

This runbook provides operational procedures for the OrdersService, which is responsible for managing the entire lifecycle of customer orders in the FlowMart e-commerce platform.


## Architecture

The OrdersService is responsible for:
- Creating and processing customer orders
- Tracking order status throughout fulfillment
- Coordinating with other services (Inventory, Payment, Shipping)
- Managing order history and amendments

### Service Dependencies

```mermaid
flowchart TD
    OrdersService --> InventoryService[Inventory Service]
    OrdersService --> PaymentService[Payment Service]
    OrdersService --> ShippingService[Shipping Service]
    OrdersService --> NotificationService[Notification Service]
    OrdersService --> OrdersDB[(Orders Database)]
    OrdersService --> EventBus[Event Bus]
```

## Monitoring and Alerting

### Key Metrics

| Metric | Description | Warning Threshold | Critical Threshold |
|--------|-------------|-------------------|-------------------|
| `order_creation_rate` | Orders created per minute | < 5 | < 1 |
| `order_creation_latency` | Time to create an order | > 2s | > 5s |
| `order_error_rate` | Percentage of failed orders | > 1% | > 5% |
| `database_connection_pool` | Database connection pool utilization | > 70% | > 90% |
| `memory_usage` | Container memory usage | > 80% | > 90% |
| `cpu_usage` | Container CPU usage | > 70% | > 85% |

### Dashboards

- [OrdersService Overview](https://grafana.flowmart.com/d/orders-overview)
- [OrdersService API Metrics](https://grafana.flowmart.com/d/orders-api)
- [OrdersService Error Tracking](https://grafana.flowmart.com/d/orders-errors)

### Common Alerts

| Alert | Description | Troubleshooting Steps |
|-------|-------------|----------------------|
| `OrdersServiceHighLatency` | API latency exceeds thresholds | See [High Latency](#high-latency) |
| `OrdersServiceHighErrorRate` | Error rate exceeds thresholds | See [High Error Rate](#high-error-rate) |
| `OrdersServiceDatabaseConnectionIssues` | Database connection issues | See [Database Issues](#database-issues) |

## Troubleshooting Guides

### High Latency

If the service is experiencing high latency:

1. **Check system metrics**:
   ```bash
   kubectl top pods -n orders
   ```

2. **Check database metrics** in the MongoDB dashboard to identify slow queries.

3. **Check dependent services** to see if delays are caused by downstream systems:
   ```bash
   curl -X GET https://api.internal.flowmart.com/inventory/health
   curl -X GET https://api.internal.flowmart.com/payment/health
   ```

4. **Analyze recent changes** that might have impacted performance.

5. **Scale the service** if needed:
   ```bash
   kubectl scale deployment orders-service -n orders --replicas=5
   ```

### High Error Rate

If the service is experiencing a high error rate:

1. **Check application logs**:
   ```bash
   kubectl logs -l app=orders-service -n orders --tail=100
   ```

2. **Check for recent deployments** that might have introduced issues:
   ```bash
   kubectl rollout history deployment/orders-service -n orders
   ```

3. **Verify database connectivity**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=orders-service -n orders -o jsonpath='{.items[0].metadata.name}') -n orders -- node -e "const mongoose = require('mongoose'); mongoose.connect(process.env.MONGODB_URI).then(() => console.log('Connected!')).catch(err => console.error('Connection error', err));"
   ```

4. **Check dependent services** for failures:
   ```bash
   curl -X GET https://api.internal.flowmart.com/inventory/health
   curl -X GET https://api.internal.flowmart.com/payment/health
   ```

5. **Consider rolling back** if issues persist:
   ```bash
   kubectl rollout undo deployment/orders-service -n orders
   ```

### Database Issues

If there are database connection issues:

1. **Check MongoDB status**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=mongodb -n data -o jsonpath='{.items[0].metadata.name}') -n data -- mongo admin -u admin -p $MONGODB_PASSWORD --eval "db.serverStatus()"
   ```

2. **Verify network connectivity**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=orders-service -n orders -o jsonpath='{.items[0].metadata.name}') -n orders -- ping mongodb.data.svc.cluster.local
   ```

3. **Check MongoDB resource usage**:
   ```bash
   kubectl top pods -l app=mongodb -n data
   ```

4. **Review MongoDB logs**:
   ```bash
   kubectl logs -l app=mongodb -n data --tail=100
   ```

## Common Operational Tasks

### Scaling the Service

To scale the service horizontally:

```bash
kubectl scale deployment orders-service -n orders --replicas=<number>
```

### Restarting the Service

To restart all pods:

```bash
kubectl rollout restart deployment orders-service -n orders
```

### Viewing Recent Orders

To view recent orders in the database:

```bash
kubectl exec -it $(kubectl get pods -l app=orders-service -n orders -o jsonpath='{.items[0].metadata.name}') -n orders -- node -e "const mongoose = require('mongoose'); const Order = require('./models/order'); mongoose.connect(process.env.MONGODB_URI).then(async () => { const orders = await Order.find().sort({createdAt: -1}).limit(10); console.log(JSON.stringify(orders, null, 2)); process.exit(0); });"
```

### Manually Processing Stuck Orders

If orders are stuck in a particular state:

1. Identify stuck orders:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=orders-service -n orders -o jsonpath='{.items[0].metadata.name}') -n orders -- node -e "const mongoose = require('mongoose'); const Order = require('./models/order'); mongoose.connect(process.env.MONGODB_URI).then(async () => { const stuckOrders = await Order.find({status: 'PROCESSING', updatedAt: {$lt: new Date(Date.now() - 30*60*1000)}}); console.log(JSON.stringify(stuckOrders, null, 2)); process.exit(0); });"
   ```

2. Manually trigger processing for a specific order:
   ```bash
   curl -X POST https://api.internal.flowmart.com/orders/process -H "Content-Type: application/json" -d '{"orderId": "ORDER_ID", "force": true}'
   ```

## Recovery Procedures

### Database Failure Recovery

If the MongoDB database becomes unavailable:

1. Verify the status of the MongoDB cluster:
   ```bash
   kubectl get pods -l app=mongodb -n data
   ```

2. If the primary node is down, initiate a manual failover if necessary:
   ```bash
   kubectl exec -it mongodb-0 -n data -- mongo admin -u admin -p $MONGODB_PASSWORD --eval "rs.stepDown()"
   ```

3. If the entire cluster is unavailable, create an incident and notify the Database Team.

4. Once database availability is restored, validate the OrdersService functionality:
   ```bash
   curl -X GET https://api.internal.flowmart.com/orders/health
   ```

### Event Bus Failure Recovery

If the Event Bus is unavailable:

1. The OrdersService implements the Circuit Breaker pattern and will queue messages locally.

2. When the Event Bus is restored, check the backlog of events:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=orders-service -n orders -o jsonpath='{.items[0].metadata.name}') -n orders -- curl localhost:9090/metrics | grep event_queue
   ```

3. Manually trigger event processing if necessary:
   ```bash
   curl -X POST https://api.internal.flowmart.com/orders/admin/process-event-queue -H "Authorization: Bearer $ADMIN_TOKEN"
   ```

## Disaster Recovery

### Complete Service Failure

In case of a complete service failure:

1. Initiate incident response by notifying the on-call team through PagerDuty.

2. Check for region-wide AWS issues on the AWS Status page.

3. If necessary, trigger the DR plan to fail over to the secondary region:
   ```bash
   ./scripts/dr-failover.sh orders-service
   ```

4. Update Route53 DNS to point to the secondary region if global failover is needed:
   ```bash
   aws route53 change-resource-record-sets --hosted-zone-id $HOSTED_ZONE_ID --change-batch file://dr-dns-change.json
   ```

## Maintenance Tasks

### Deploying New Versions

```bash
kubectl set image deployment/orders-service -n orders orders-service=ecr.aws/flowmart/orders-service:$VERSION
```

### Database Maintenance

Scheduled database maintenance should be performed during off-peak hours:

1. Notify stakeholders through the #maintenance Slack channel.

2. Set OrdersService to maintenance mode:
   ```bash
   curl -X POST https://api.internal.flowmart.com/orders/admin/maintenance -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" -d '{"maintenanceMode": true, "message": "Scheduled maintenance"}'
   ```

3. Perform database maintenance operations.

4. Turn off maintenance mode:
   ```bash
   curl -X POST https://api.internal.flowmart.com/orders/admin/maintenance -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" -d '{"maintenanceMode": false}'
   ```

## Contact Information

**Primary On-Call:** Orders Team (rotating schedule)  
**Secondary On-Call:** Platform Team  
**Escalation Path:** Orders Team Lead > Engineering Manager > CTO

**Slack Channels:**
- #orders-support (primary support channel)
- #orders-alerts (automated alerts)
- #incident-response (for major incidents)

## Reference Information

- [OrdersService API Documentation](https://docs.internal.flowmart.com/orders/api)
- [Architecture Diagram](https://docs.internal.flowmart.com/architecture/orders)
- [Service Level Objectives (SLOs)](https://docs.internal.flowmart.com/slo/orders) 
---
title: PaymentService Runbook
summary: Operational runbook for troubleshooting and maintaining the PaymentService
sidebar:
    label: PaymentService
    order: 3
---

This runbook provides operational procedures for the PaymentService, which is responsible for processing payments, refunds, and managing financial transactions in the FlowMart e-commerce platform.

## Architecture

The PaymentService is responsible for:
- Processing customer payments
- Managing refunds and chargebacks
- Integrating with external payment gateways
- Storing payment transactions
- Handling subscription billing

### Service Dependencies

```mermaid
flowchart TD
    PaymentService --> PostgresDB[(PostgreSQL Database)]
    PaymentService --> EventBus[Event Bus]
    PaymentService --> StripeGateway[Stripe Payment Gateway]
    PaymentService --> PayPalGateway[PayPal Gateway]
    PaymentService --> VaultService[Vault - Secret Management]
```

## Monitoring and Alerting

### Key Metrics

| Metric | Description | Warning Threshold | Critical Threshold |
|--------|-------------|-------------------|-------------------|
| `payment_processing_rate` | Payments processed per minute | < 5 | < 1 |
| `payment_success_rate` | Percentage of successful payments | < 95% | < 90% |
| `payment_processing_latency` | Time to process a payment | > 3s | > 8s |
| `refund_processing_latency` | Time to process a refund | > 5s | > 15s |
| `gateway_error_rate` | Payment gateway errors | > 2% | > 5% |
| `fraud_detection_latency` | Time for fraud checks | > 1s | > 3s |

### Dashboards

- [PaymentService Overview](https://grafana.flowmart.com/d/payment-overview)
- [Payment Gateway Status](https://grafana.flowmart.com/d/payment-gateways)
- [Transaction Success Rates](https://grafana.flowmart.com/d/payment-success-rates)

### Common Alerts

| Alert | Description | Troubleshooting Steps |
|-------|-------------|----------------------|
| `PaymentServiceHighErrorRate` | Payment failure rate above threshold | See [High Error Rate](#high-error-rate) |
| `PaymentServiceGatewayFailure` | Payment gateway connection issues | See [Gateway Issues](#payment-gateway-issues) |
| `PaymentServiceHighLatency` | Payment processing latency issues | See [High Latency](#high-latency) |
| `PaymentServiceDatabaseIssues` | Database connection issues | See [Database Issues](#database-issues) |

## Troubleshooting Guides

### High Error Rate

If the service is experiencing a high payment error rate:

1. **Check application logs** for error patterns:
   ```bash
   kubectl logs -l app=payment-service -n payment --tail=100
   ```

2. **Check payment gateway status** on their status pages:
   - [Stripe Status](https://status.stripe.com/)
   - [PayPal Status](https://status.paypal.com/)

3. **Check for patterns in failed transactions**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/query-failed-transactions.js --last-hour
   ```

4. **Check for recent deployments** that might have introduced issues:
   ```bash
   kubectl rollout history deployment/payment-service -n payment
   ```

5. **Verify if the issue is specific to a payment method** (credit card, PayPal, etc.):
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/payment-method-success-rates.js
   ```

### Payment Gateway Issues

If there are issues with payment gateways:

1. **Check gateway connectivity**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- curl -o /dev/null -s -w "%{http_code}\n" https://api.stripe.com/v1/charges -H "Authorization: Bearer $STRIPE_TEST_KEY"
   ```

2. **Check payment gateway API keys** rotation status:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/check-api-key-rotation.js
   ```

3. **Check gateway timeouts** in application logs:
   ```bash
   kubectl logs -l app=payment-service -n payment | grep "gateway timeout"
   ```

4. **Verify if the issue is isolated to a specific gateway**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/gateway-health-check.js
   ```

5. **Switch to backup payment gateway** if primary is down:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- curl -X POST localhost:3000/internal/api/payment/switch-gateway -H "Content-Type: application/json" -d '{"primaryGateway": "paypal", "reason": "Stripe outage"}'
   ```

### High Latency

If the service is experiencing high latency:

1. **Check system metrics**:
   ```bash
   kubectl top pods -n payment
   ```

2. **Check database connection pool**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/db-pool-stats.js
   ```

3. **Check slow queries** in the payment database:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- psql -U postgres -d payments -c "SELECT query, calls, mean_exec_time, max_exec_time FROM pg_stat_statements WHERE mean_exec_time > 100 ORDER BY mean_exec_time DESC LIMIT 10;"
   ```

4. **Check payment gateway response times**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/gateway-latency-check.js
   ```

5. **Scale the service** if needed:
   ```bash
   kubectl scale deployment payment-service -n payment --replicas=5
   ```

### Database Issues

If there are database issues:

1. **Check PostgreSQL status**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- pg_isready -U postgres -d payments
   ```

2. **Check for long-running transactions**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- psql -U postgres -d payments -c "SELECT pid, now() - xact_start AS duration, state, query FROM pg_stat_activity WHERE state != 'idle' ORDER BY duration DESC LIMIT 10;"
   ```

3. **Check for database locks**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- psql -U postgres -d payments -c "SELECT relation::regclass, mode, pid, granted FROM pg_locks l JOIN pg_stat_activity a ON l.pid = a.pid WHERE relation = 'payments.transactions'::regclass;"
   ```

4. **Restart database connections** if needed:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- curl -X POST localhost:3000/internal/api/system/refresh-db-connections
   ```

## Common Operational Tasks

### Managing API Keys

#### Rotating Payment Gateway API Keys

1. **Generate new API keys** in the payment gateway admin portal.

2. **Store the new keys** in AWS Secrets Manager:
   ```bash
   aws secretsmanager update-secret --secret-id flowmart/payment/stripe-api-key --secret-string '{"api_key": "sk_live_NEW_KEY", "webhook_secret": "whsec_NEW_SECRET"}'
   ```

3. **Trigger key rotation** in the service:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- curl -X POST localhost:3000/internal/api/system/reload-api-keys
   ```

4. **Verify the new keys are active**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/verify-api-keys.js
   ```

### Managing Refunds

#### Processing Manual Refunds

For special cases requiring manual intervention:

```bash
curl -X POST https://api.internal.flowmart.com/payment/transactions/{transactionId}/refund \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"amount": 1999, "reason": "Customer service request", "refundToOriginalMethod": true}'
```

#### Finding Failed Refunds

To identify and retry failed refunds:

```bash
kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/list-failed-refunds.js --last-24h
```

### Handling Chargebacks

To record and process a new chargeback:

```bash
curl -X POST https://api.internal.flowmart.com/payment/transactions/{transactionId}/chargeback \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"chargebackReference": "CB12345", "amount": 1999, "reason": "Unauthorized transaction"}'
```

### Payment Reconciliation

To trigger payment reconciliation with payment gateway:

```bash
kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/reconcile-payments.js --gateway=stripe --date=2023-05-15
```

## Recovery Procedures

### Failed Transactions Recovery

If transactions are stuck or failed:

1. **Identify stuck transactions**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/find-stuck-transactions.js
   ```

2. **Check transaction status** with the payment gateway:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/check-gateway-transaction.js --transaction-id=TXN123456
   ```

3. **Resolve transactions** that completed at gateway but failed in our system:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/resolve-stuck-transaction.js --transaction-id=TXN123456 --status=completed
   ```

### Payment Gateway Failure Recovery

If a payment gateway is unavailable:

1. **Enable fallback gateway** mode:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- curl -X POST localhost:3000/internal/api/system/enable-fallback-gateway
   ```

2. **Monitor gateway status** for recovery:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/monitor-gateway-health.js --gateway=stripe
   ```

3. **Disable fallback mode** once the primary gateway is restored:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- curl -X POST localhost:3000/internal/api/system/disable-fallback-gateway
   ```

### Database Failure Recovery

If the PostgreSQL database becomes unavailable:

1. Verify the status of the PostgreSQL cluster:
   ```bash
   kubectl get pods -l app=postgresql -n data
   ```

2. Check if automatic failover has occurred:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql-patroni -n data -o jsonpath='{.items[0].metadata.name}') -n data -- patronictl list
   ```

3. Once database availability is restored, validate the PaymentService functionality:
   ```bash
   curl -X GET https://api.internal.flowmart.com/payment/health
   ```

## Disaster Recovery

### Complete Service Failure

In case of a complete service failure:

1. Initiate incident response by notifying the on-call team through PagerDuty.

2. If necessary, deploy to the disaster recovery environment:
   ```bash
   ./scripts/dr-failover.sh payment-service
   ```

3. Update DNS records to point to the DR environment:
   ```bash
   aws route53 change-resource-record-sets --hosted-zone-id $HOSTED_ZONE_ID --change-batch file://dr-dns-change.json
   ```

4. Enable simplified payment flow (if necessary):
   ```bash
   kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- curl -X POST localhost:3000/internal/api/system/enable-simplified-flow
   ```

5. Regularly check primary environment recovery status.

## Maintenance Tasks

### Deploying New Versions

```bash
kubectl set image deployment/payment-service -n payment payment-service=ecr.aws/flowmart/payment-service:$VERSION
```

### Database Migrations

For database schema updates:

1. Notify stakeholders through the #maintenance Slack channel.

2. Create a migration plan and backup the database:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=postgresql -n data -o jsonpath='{.items[0].metadata.name}') -n data -- pg_dump -U postgres -d payments > payments_backup_$(date +%Y%m%d).sql
   ```

3. Apply database migrations:
   ```bash
   kubectl apply -f payment-migration-job.yaml
   ```

4. Verify migration completion:
   ```bash
   kubectl logs -l job-name=payment-db-migration -n payment
   ```

### Compliance and Auditing

To generate PCI compliance reports:

```bash
kubectl exec -it $(kubectl get pods -l app=payment-service -n payment -o jsonpath='{.items[0].metadata.name}') -n payment -- node scripts/generate-pci-audit-report.js --month=2023-05
```

## Contact Information

**Primary On-Call:** Payments Team (rotating schedule)  
**Secondary On-Call:** Platform Team  
**Escalation Path:** Payments Team Lead > Engineering Manager > CTO

**Slack Channels:**
- #payments-support (primary support channel)
- #payments-alerts (automated alerts)
- #incident-response (for major incidents)

**External Contacts:**
- Stripe Support: support@stripe.com, 1-888-555-1234
- PayPal Support: merchant-support@paypal.com, 1-888-555-5678

## Reference Information

- [PaymentService API Documentation](https://docs.internal.flowmart.com/payment/api)
- [Architecture Diagram](https://docs.internal.flowmart.com/architecture/payment)
- [Service Level Objectives (SLOs)](https://docs.internal.flowmart.com/slo/payment)
- [PCI Compliance Documentation](https://docs.internal.flowmart.com/security/payment-pci)
- [Payment Gateway Integration Guides](https://docs.internal.flowmart.com/payment/gateway-integration) 
---
title: ShippingService Runbook
summary: Operational runbook for troubleshooting and maintaining the ShippingService
sidebar:
    label: ShippingService
    order: 4
---

This runbook provides operational procedures for the ShippingService, which is responsible for managing shipping options, carrier integration, and delivery tracking in the FlowMart e-commerce platform.


## Architecture

The ShippingService is responsible for:
- Calculating shipping costs and delivery estimates
- Managing shipping carriers and integration
- Generating shipping labels
- Tracking shipments
- Handling delivery exceptions and returns

### Service Dependencies

```mermaid
flowchart TD
    ShippingService --> MongoDB[(MongoDB Database)]
    ShippingService --> EventBus[Event Bus]
    ShippingService --> Redis[(Redis Cache)]
    ShippingService --> FedExAPI[FedEx API]
    ShippingService --> UPSApi[UPS API]
    ShippingService --> USPSApi[USPS API]
    ShippingService --> DHLApi[DHL API]
    ShippingService --> VaultService[Vault - Secret Management]
```

## Monitoring and Alerting

### Key Metrics

| Metric | Description | Warning Threshold | Critical Threshold |
|--------|-------------|-------------------|-------------------|
| `shipping_rate_calculation_rate` | Rate calculations per minute | < 10 | < 2 |
| `shipping_label_generation_success` | Label generation success % | < 98% | < 95% |
| `carrier_api_response_time` | Carrier API response time | > 2s | > 5s |
| `carrier_api_error_rate` | Carrier API errors % | > 2% | > 5% |
| `tracking_update_processing_rate` | Tracking updates processed per minute | < 50 | < 10 |
| `shipment_tracking_lag` | Delay in tracking information | > 15m | > 1h |

### Dashboards

- [Shipping Service Overview](https://grafana.flowmart.com/d/shipping-overview)
- [Carrier API Status](https://grafana.flowmart.com/d/shipping-carriers)
- [Delivery Performance](https://grafana.flowmart.com/d/shipping-delivery-performance)

### Common Alerts

| Alert | Description | Troubleshooting Steps |
|-------|-------------|----------------------|
| `ShippingServiceHighErrorRate` | Shipping API error rate above threshold | See [High Error Rate](#high-error-rate) |
| `ShippingCarrierAPIDown` | Carrier API connection issues | See [Carrier API Issues](#carrier-api-issues) |
| `ShippingServiceHighLatency` | Shipping service latency issues | See [High Latency](#high-latency) |
| `ShippingServiceDatabaseIssues` | Database connection issues | See [Database Issues](#database-issues) |

## Troubleshooting Guides

### High Error Rate

If the service is experiencing a high error rate:

1. **Check application logs** for error patterns:
   ```bash
   kubectl logs -l app=shipping-service -n shipping --tail=100
   ```

2. **Check specific error types**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/error-analyzer.jar --last-hour
   ```

3. **Check for patterns in failed shipments**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/failed-shipments-analyzer.jar
   ```

4. **Check for recent deployments** that might have introduced issues:
   ```bash
   kubectl rollout history deployment/shipping-service -n shipping
   ```

5. **Verify if the issue is specific to a carrier** (FedEx, UPS, etc.):
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/carrier-success-rates.jar
   ```

### Carrier API Issues

If there are issues with carrier APIs:

1. **Check carrier API connectivity**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/carrier-health-check.jar
   ```

2. **Check carrier API credentials** and rotation status:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/check-carrier-credentials.jar
   ```

3. **Check carrier status pages** for announced outages:
   - [FedEx Status](https://www.fedex.com/en-us/service-alerts.html)
   - [UPS Status](https://www.ups.com/service-alerts)
   - [USPS Status](https://about.usps.com/newsroom/service-alerts/)

4. **Check carrier timeouts** in application logs:
   ```bash
   kubectl logs -l app=shipping-service -n shipping | grep "carrier timeout"
   ```

5. **Enable fallback shipping carrier**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- curl -X POST localhost:8080/internal/api/shipping/enable-fallback-carrier -H "Content-Type: application/json" -d '{"primaryCarrier": "fedex", "fallbackCarrier": "ups", "reason": "FedEx API outage"}'
   ```

### High Latency

If the service is experiencing high latency:

1. **Check system metrics**:
   ```bash
   kubectl top pods -n shipping
   ```

2. **Check JVM memory and GC metrics**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/jvm-metrics.jar
   ```

3. **Check MongoDB performance**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=mongodb -n data -o jsonpath='{.items[0].metadata.name}') -n data -- mongo --eval "db.currentOp()"
   ```

4. **Check carrier API response times**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/carrier-response-times.jar
   ```

5. **Scale the service** if needed:
   ```bash
   kubectl scale deployment shipping-service -n shipping --replicas=5
   ```

### Database Issues

If there are MongoDB issues:

1. **Check MongoDB status**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=mongodb -n data -o jsonpath='{.items[0].metadata.name}') -n data -- mongo --eval "rs.status()"
   ```

2. **Check for slow queries**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=mongodb -n data -o jsonpath='{.items[0].metadata.name}') -n data -- mongo --eval "db.currentOp({ 'active': true, 'secs_running': { '$gt': 5 } })"
   ```

3. **Check database connection pool**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/db-pool-stats.jar
   ```

4. **Restart database connections** if needed:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- curl -X POST localhost:8080/internal/api/system/refresh-db-connections
   ```

## Common Operational Tasks

### Managing Carrier API Credentials

#### Rotating Carrier API Keys

1. **Generate new API keys** in the carrier portal:
   - FedEx Developer Portal: [https://developer.fedex.com](https://developer.fedex.com)
   - UPS Developer Portal: [https://developer.ups.com](https://developer.ups.com)
   - USPS Web Tools: [https://www.usps.com/business/web-tools-apis](https://www.usps.com/business/web-tools-apis)

2. **Store the new keys** in AWS Secrets Manager:
   ```bash
   aws secretsmanager update-secret --secret-id flowmart/shipping/fedex-api-key --secret-string '{"api_key": "NEW_KEY", "password": "NEW_PASSWORD", "account_number": "ACCOUNT_NUMBER"}'
   ```

3. **Trigger key rotation** in the service:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- curl -X POST localhost:8080/internal/api/system/reload-carrier-credentials
   ```

4. **Verify the new keys are working** by testing label generation:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/test-label-generation.jar --carrier=fedex
   ```

### Managing Shipping Rates

#### Updating Shipping Rate Tables

When carrier rates change:

1. **Prepare the new rate table** in the required JSON format.

2. **Upload the rate table** to S3:
   ```bash
   aws s3 cp new-fedex-rates.json s3://flowmart-configs/shipping/rates/
   ```

3. **Trigger rate table reload**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- curl -X POST localhost:8080/internal/api/shipping/reload-rate-tables -H "Content-Type: application/json" -d '{"carrier": "fedex"}'
   ```

4. **Verify rate calculations** with test scenarios:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/test-rate-calculation.jar
   ```

### Shipping Label Generation Troubleshooting

#### Debugging Failed Label Generation

If labels are failing to generate:

```bash
# Find recent failed label generation attempts
kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/find-failed-labels.jar --hours=2

# Get detailed error for a specific shipment
kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/label-error-details.jar --shipment-id=SHIP123456
```

#### Manual Label Generation

For special cases requiring manual intervention:

```bash
curl -X POST https://api.internal.flowmart.com/shipping/shipments/{shipmentId}/generate-label \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"carrier": "fedex", "service": "PRIORITY_OVERNIGHT", "forceGeneration": true}'
```

### Tracking Updates

#### Triggering Manual Tracking Updates

To manually trigger tracking updates:

```bash
kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/sync-tracking.jar --shipment-id=SHIP123456

# For bulk tracking updates
kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/sync-tracking.jar --status=in_transit --hours=24
```

#### Tracking Webhook Troubleshooting

If tracking webhooks from carriers are failing:

```bash
# Check recent webhook failures
kubectl logs -l app=shipping-webhook-service -n shipping | grep "Webhook failure"

# Replay failed webhooks
kubectl exec -it $(kubectl get pods -l app=shipping-webhook-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/replay-webhooks.jar --hours=2
```

## Recovery Procedures

### Failed Shipment Recovery

If shipments are stuck or failed:

1. **Identify stuck shipments**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/find-stuck-shipments.jar
   ```

2. **Check shipment status** with the carrier:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/check-carrier-shipment.jar --shipment-id=SHIP123456
   ```

3. **Resolve shipments** that completed at carrier but failed in our system:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/resolve-shipment.jar --shipment-id=SHIP123456 --tracking-number=1Z999AA10123456784 --status=label_created
   ```

### Carrier API Failure Recovery

If a carrier API is unavailable:

1. **Enable automatic carrier fallback**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- curl -X POST localhost:8080/internal/api/system/enable-carrier-fallback
   ```

2. **Monitor carrier API status** for recovery:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/monitor-carrier-health.jar --carrier=fedex
   ```

3. **Switch back to primary carrier** once it's restored:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- curl -X POST localhost:8080/internal/api/system/disable-carrier-fallback
   ```

### Database Failure Recovery

If the MongoDB database becomes unavailable:

1. **Verify the status of the MongoDB cluster**:
   ```bash
   kubectl get pods -l app=mongodb -n data
   ```

2. **Check if automatic failover has occurred**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=mongodb -n data -o jsonpath='{.items[0].metadata.name}') -n data -- mongo --eval "rs.status()"
   ```

3. **Once database availability is restored, validate ShippingService functionality**:
   ```bash
   curl -X GET https://api.internal.flowmart.com/shipping/health
   ```

## Disaster Recovery

### Complete Service Failure

In case of a complete service failure:

1. **Initiate incident response** by notifying the on-call team through PagerDuty.

2. **Deploy to the disaster recovery environment** if necessary:
   ```bash
   ./scripts/dr-failover.sh shipping-service
   ```

3. **Update DNS records** to point to the DR environment:
   ```bash
   aws route53 change-resource-record-sets --hosted-zone-id $HOSTED_ZONE_ID --change-batch file://dr-dns-change.json
   ```

4. **Enable simplified shipping flow** (if necessary):
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- curl -X POST localhost:8080/internal/api/system/enable-simplified-flow
   ```

5. **Regularly check primary environment recovery status**.

## Maintenance Tasks

### Deploying New Versions

```bash
kubectl set image deployment/shipping-service -n shipping shipping-service=ecr.aws/flowmart/shipping-service:$VERSION
```

### Database Maintenance

#### MongoDB Index Maintenance

Periodically verify and optimize MongoDB indexes:

```bash
# Check current indexes
kubectl exec -it $(kubectl get pods -l app=mongodb -n data -o jsonpath='{.items[0].metadata.name}') -n data -- mongo --eval "db.shipments.getIndexes()"

# Add new index (example)
kubectl exec -it $(kubectl get pods -l app=mongodb -n data -o jsonpath='{.items[0].metadata.name}') -n data -- mongo --eval "db.shipments.createIndex({carrier: 1, status: 1, createdAt: -1})"
```

#### Database Backups

Verify scheduled MongoDB backups:

```bash
# Check recent backups
aws s3 ls s3://flowmart-mongodb-backups/shipping/ --human-readable

# Trigger manual backup if needed
kubectl apply -f shipping-db-backup-job.yaml
```

### Carrier Integration Updates

When a carrier updates their API:

1. **Test the API changes** in the staging environment:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service-staging -n shipping-staging -o jsonpath='{.items[0].metadata.name}') -n shipping-staging -- java -jar /app/tools/test-carrier-integration.jar --carrier=fedex --mode=new
   ```

2. **Update integration configuration** if needed:
   ```bash
   kubectl apply -f updated-fedex-integration-config.yaml
   ```

3. **Validate the updated integration**:
   ```bash
   kubectl exec -it $(kubectl get pods -l app=shipping-service -n shipping -o jsonpath='{.items[0].metadata.name}') -n shipping -- java -jar /app/tools/validate-carrier-integration.jar --carrier=fedex
   ```

## Contact Information

**Primary On-Call:** Logistics Team (rotating schedule)  
**Secondary On-Call:** Platform Team  
**Escalation Path:** Logistics Team Lead > Engineering Manager > CTO

**Slack Channels:**
- #shipping-support (primary support channel)
- #shipping-alerts (automated alerts)
- #incident-response (for major incidents)

**External Contacts:**
- FedEx API Support: apisupport@fedex.com, 1-800-555-1234
- UPS Developer Support: developer@ups.com, 1-800-555-5678
- USPS Web Tools Support: uspstechsupport@usps.gov, 1-800-555-9012

## Reference Information

- [ShippingService API Documentation](https://docs.internal.flowmart.com/shipping/api)
- [Architecture Diagram](https://docs.internal.flowmart.com/architecture/shipping)
- [Service Level Objectives (SLOs)](https://docs.internal.flowmart.com/slo/shipping)
- [Carrier Integration Guides](https://docs.internal.flowmart.com/shipping/carrier-integration)
- [Rate Calculation Documentation](https://docs.internal.flowmart.com/shipping/rate-calculation) 
---
title: Architecture Decision Records (ADR)
summary: A document that captures important architectural decisions and their context
sidebar:
    label: ADR Template
    order: 1
---



## What is an Architecture Decision Record (ADR)?

<Tiles columns={2}>
    <Tile icon="CommandLineIcon" iconColor="black" href="/docs" title="Explore examples on GitHub" description="Delve into our documentation for more insights." />
    <Tile icon="UsersIcon" iconColor="black" href="/docs" title="Request a review" description="Request a review from the team. Reviews for ADRs are from the design authority, and can take a week." />
</Tiles>

Architecture Decision Records (ADRs) are documents that capture important architectural decisions made during the development of a software system. Each ADR describes a choice the team has made, the context in which it was made, and the consequences of that choice.

## Why ADRs are Important

:::tip
Use this template to create your own ADRs. Once you read this page you can submit new ADRs to the [Architecture Decision Records](https://github.com/eventcatalog/eventcatalog/issues/new?assignees=&labels=architecture&template=architecture-decision-record.mdx&title=ADR%3A+) repository.
:::

ADRs help teams:
- Document decisions for future reference
- Communicate architectural choices across the organization
- Onboard new team members by providing insight into past decisions
- Track the evolution of the system architecture over time
- Establish a process for making and documenting significant technical decisions

## ADR Format

Our ADRs follow this structure:
- **Title**: A descriptive name for the decision
- **Status**: Current status (Proposed, Accepted, Superseded, etc.)
- **Context**: The factors that influenced the decision
- **Decision**: The choice that was made
- **Consequences**: The resulting outcomes, both positive and negative
- **Compliance Requirements**: Any regulatory or policy requirements that must be met
- **Implementation Details**: How and when the decision will be implemented
- **Alternatives**: Other options that were considered
- **References**: Resources that support or provide more information
- **Decision History**: The record of changes to the ADR

```mermaid
flowchart TD
    A[Identify Architectural Decision Point] --> B[Discuss Options]
    B --> C[Draft ADR]
    C --> D[Review with Stakeholders]
    D --> E{Approved?}
    E -->|Yes| F[Update Status to Approved]
    E -->|No| G[Revise ADR]
    G --> D
    F --> H[Implement Decision]
    H --> I[Monitor & Evaluate]
    I --> J{Changes Needed?}
    J -->|Yes| K[Create New or Update ADR]
    K --> B
    J -->|No| L[Document Learnings]
```

---
title: Infrastructure as Code (IaC) Overview
summary: An overview of the infrastructure-as-code approach used in the FlowMart e-commerce platform
sidebar:
    label: 01 - IaC Overview
    order: 1
---

# Infrastructure as Code (IaC) Overview

This document provides an overview of the Infrastructure as Code (IaC) approach used to manage and provision the infrastructure for the FlowMart e-commerce platform.

## What is Infrastructure as Code?

Infrastructure as Code (IaC) is an approach to infrastructure management where infrastructure resources are defined and provisioned through machine-readable definition files, rather than through manual processes or interactive configuration tools. This approach allows us to:

- **Version control** our infrastructure definitions alongside our application code
- **Automate** the provisioning and management of infrastructure
- **Standardize** configurations across different environments
- **Document** our infrastructure setup as living code rather than static documentation
- **Test** infrastructure changes before deploying to production

## Our IaC Tech Stack

For the FlowMart e-commerce platform, we use the following technologies for our infrastructure management:

### Primary Tools

| Tool | Purpose |
|------|---------|
| **Terraform** | Infrastructure provisioning across cloud providers (primary tool) |
| **Kubernetes (K8s)** | Container orchestration |
| **Helm Charts** | Kubernetes application deployment packaging |
| **GitHub Actions** | CI/CD pipeline automation |
| **AWS CloudFormation** | Specific AWS infrastructure components |

### Additional Supporting Tools

| Tool | Purpose |
|------|---------|
| **Terragrunt** | Terraform code organization and management |
| **Packer** | Virtual machine image building |
| **Ansible** | Configuration management |
| **Prometheus & Grafana** | Monitoring and alerting |
| **ELK Stack** | Logging |

## Infrastructure Architecture

Our infrastructure is organized into the following logical components:

```mermaid
flowchart TD
    classDef networkInfra fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    classDef computeInfra fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    classDef datastoreInfra fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px
    classDef securityInfra fill:#f8cecc,stroke:#b85450,stroke-width:2px
    classDef monitoringInfra fill:#fff2cc,stroke:#d6b656,stroke-width:2px

    subgraph "Networking Infrastructure"
        VPC[VPC & Subnets]
        IGW[Internet Gateway]
        NLB[Network Load Balancer]
        Route53[DNS - Route53]
    end
    
    subgraph "Compute Infrastructure"
        EKS[EKS Cluster]
        EC2[EC2 Instances]
        Lambda[Lambda Functions]
    end
    
    subgraph "Data Storage"
        RDS[RDS Databases]
        DynamoDB[DynamoDB Tables]
        S3[S3 Buckets]
        ElastiCache[ElastiCache Redis]
    end
    
    subgraph "Security"
        IAM[IAM Roles & Policies]
        SG[Security Groups]
        WAF[WAF & Shield]
        Secrets[Secrets Manager]
    end
    
    subgraph "Monitoring & Logging"
        CloudWatch[CloudWatch]
        Prometheus[Prometheus]
        Grafana[Grafana Dashboards]
        ELK[ELK Stack]
    end
    
    %% Connections
    VPC --> IGW
    IGW --> NLB
    NLB --> EKS
    Route53 --> NLB
    
    EKS --> SG
    EC2 --> SG
    Lambda --> SG
    
    EKS --> RDS
    EKS --> DynamoDB
    EKS --> S3
    EKS --> ElastiCache
    
    IAM --> EKS
    IAM --> Lambda
    IAM --> RDS
    
    CloudWatch --> EKS
    CloudWatch --> RDS
    CloudWatch --> Lambda
    Prometheus --> EKS
    Grafana --> Prometheus
    ELK --> EKS
    
    %% Apply styles
    class VPC,IGW,NLB,Route53 networkInfra
    class EKS,EC2,Lambda computeInfra
    class RDS,DynamoDB,S3,ElastiCache datastoreInfra
    class IAM,SG,WAF,Secrets securityInfra
    class CloudWatch,Prometheus,Grafana,ELK monitoringInfra
```

## Repository Structure

Our infrastructure code is organized as follows:

```
infrastructure/
│
├── terraform/                  # Terraform configuration
│   ├── environments/           # Environment-specific configurations
│   │   ├── dev/
│   │   ├── staging/
│   │   └── production/
│   ├── modules/                # Reusable Terraform modules
│   │   ├── networking/
│   │   ├── compute/
│   │   ├── database/
│   │   └── monitoring/
│   └── global/                 # Global resources (e.g., Route53)
│
├── kubernetes/                 # Kubernetes manifests
│   ├── base/                   # Base configurations
│   └── overlays/               # Environment-specific overlays (Kustomize)
│
├── helm-charts/                # Helm charts for application deployment
│
├── scripts/                    # Utility scripts
│
└── packer/                     # Packer templates for image building
```

## Deployment Principles

1. **Infrastructure Changes via Pull Requests**: All infrastructure changes must go through a pull request process, with automated testing and reviews.

2. **Environment Promotion**: Changes are first deployed to development, then staging, and finally production, with appropriate testing at each stage.

3. **Immutable Infrastructure**: We prefer to replace rather than modify infrastructure components.

4. **Least Privilege**: We follow the principle of least privilege for all IAM roles and security groups.

5. **Automated Rollbacks**: Our CI/CD pipelines include automated rollback capabilities if deployments fail.

## Next Steps

For more detailed information about our infrastructure as code setup, please refer to the following documents:

- [Terraform Implementation](./02-terraform-implementation.mdx)
- [Environment Setups](./03-environment-setups.mdx)
- [CI/CD Pipelines](./04-cicd-pipelines.mdx) 
---
title: Terraform Implementation
summary: Details of how Terraform is used to provision and manage the FlowMart infrastructure
sidebar:
    label: 02 - Terraform Implementation
    order: 2
---

# Terraform Implementation

This document describes how we use Terraform to manage and provision the infrastructure for the FlowMart e-commerce platform.

## Why Terraform?

We chose Terraform as our primary IaC tool for the following reasons:

- **Cloud-agnostic**: While we primarily use AWS, Terraform gives us the flexibility to work with multiple cloud providers if needed
- **Declarative syntax**: Define what you want, not how to get there
- **State management**: Tracks the current state of infrastructure to plan changes
- **Modular approach**: Supports reusable components through modules
- **Strong community support**: Wide adoption means better documentation and resources
- **Extensible**: Can be extended through providers and modules

## Terraform Structure

Our Terraform code follows a structured approach:

### Directory Structure

```
terraform/
│
├── environments/                 # Environment-specific configurations
│   ├── dev/
│   │   ├── main.tf              # Main configuration file
│   │   ├── variables.tf         # Input variables
│   │   ├── outputs.tf           # Output variables
│   │   └── terraform.tfvars     # Variable values
│   ├── staging/
│   │   └── ...
│   └── production/
│       └── ...
│
├── modules/                      # Reusable Terraform modules
│   ├── networking/               # VPC, subnets, routing
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── eks/                      # EKS cluster configuration
│   │   └── ...
│   ├── rds/                      # Database configurations
│   │   └── ...
│   ├── lambda/                   # Serverless functions
│   │   └── ...
│   └── monitoring/               # Monitoring resources
│       └── ...
│
└── global/                       # Global resources
    ├── iam/                      # IAM roles and policies
    │   └── ...
    └── route53/                  # DNS configurations
        └── ...
```

### Module Design

Each module follows a consistent pattern:

- **Inputs**: Defined in `variables.tf`
- **Resources**: Defined in `main.tf`
- **Outputs**: Defined in `outputs.tf`

## Core Infrastructure Components

Here's an overview of our main Terraform modules and what they provision:

### Networking Module

The networking module provisions our VPC infrastructure:

```hcl
module "vpc" {
  source = "../../modules/networking"

  name                 = "flowmart-${var.environment}"
  cidr                 = "10.0.0.0/16"
  azs                  = ["us-west-2a", "us-west-2b", "us-west-2c"]
  private_subnets      = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets       = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  database_subnets     = ["10.0.201.0/24", "10.0.202.0/24", "10.0.203.0/24"]
  
  enable_nat_gateway   = true
  single_nat_gateway   = var.environment != "production"
  
  tags = {
    Environment = var.environment
    Project     = "FlowMart"
    ManagedBy   = "Terraform"
  }
}
```

### EKS Module

The EKS module provisions our Kubernetes cluster:

```hcl
module "eks" {
  source = "../../modules/eks"

  cluster_name    = "flowmart-${var.environment}"
  cluster_version = "1.23"
  
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnets
  
  node_groups = {
    application = {
      desired_capacity = 3
      max_capacity     = 10
      min_capacity     = 2
      instance_types   = ["t3.large"]
      disk_size        = 50
    }
    
    system = {
      desired_capacity = 2
      max_capacity     = 4
      min_capacity     = 2
      instance_types   = ["t3.medium"]
      disk_size        = 20
    }
  }
  
  tags = {
    Environment = var.environment
    Project     = "FlowMart"
    ManagedBy   = "Terraform"
  }
}
```

### Database Module

The database module provisions our RDS instances:

```hcl
module "database" {
  source = "../../modules/rds"

  identifier           = "flowmart-${var.environment}"
  engine               = "postgres"
  engine_version       = "13.4"
  instance_class       = var.environment == "production" ? "db.r5.large" : "db.t3.medium"
  allocated_storage    = 100
  
  name                 = "flowmart"
  username             = "flowmart_admin"
  password             = var.db_password
  
  vpc_security_group_ids = [module.security_groups.database_sg_id]
  subnet_ids             = module.vpc.database_subnets
  
  backup_retention_period = var.environment == "production" ? 30 : 7
  
  tags = {
    Environment = var.environment
    Project     = "FlowMart"
    ManagedBy   = "Terraform"
  }
}
```

### DynamoDB Module

For NoSQL database needs, we use DynamoDB:

```hcl
module "dynamodb" {
  source = "../../modules/dynamodb"

  tables = {
    inventory = {
      name           = "inventory-${var.environment}"
      billing_mode   = "PROVISIONED"
      read_capacity  = var.environment == "production" ? 20 : 5
      write_capacity = var.environment == "production" ? 20 : 5
      hash_key       = "productId"
      attributes = [
        {
          name = "productId"
          type = "S"
        }
      ]
    },
    
    shopping_cart = {
      name           = "shopping-cart-${var.environment}"
      billing_mode   = "PROVISIONED"
      read_capacity  = var.environment == "production" ? 20 : 5
      write_capacity = var.environment == "production" ? 20 : 5
      hash_key       = "sessionId"
      attributes = [
        {
          name = "sessionId"
          type = "S"
        }
      ]
    }
  }
  
  tags = {
    Environment = var.environment
    Project     = "FlowMart"
    ManagedBy   = "Terraform"
  }
}
```

## Terraform Workflows

We follow these workflows when making infrastructure changes:

### Development Workflow

```mermaid
flowchart LR
    classDef highlightStep fill:#d5e8d4,stroke:#82b366,stroke-width:2px

    Init[terraform init] --> Plan[terraform plan]
    Plan --> Review[Review plan]
    Review --> Apply[terraform apply]
    Apply --> Validate[Validate changes]
    
    class Plan,Review highlightStep
```

### Terraform in CI/CD Pipeline

```mermaid
flowchart TD
    Code[Code changes pushed] --> PR[Pull request created]
    PR --> Init[terraform init]
    Init --> Plan[terraform plan]
    Plan --> AutoReview[Automated plan review]
    AutoReview --> HumanReview[Human review]
    HumanReview --> Approved{Approved?}
    Approved -->|Yes| Merge[Merge PR]
    Approved -->|No| Revise[Revise changes]
    Revise --> PR
    Merge --> CI[CI/CD pipeline]
    CI --> Apply[terraform apply]
    Apply --> PostCheck[Post-apply validation]
```

## Terraform State Management

We manage Terraform state using a remote backend with the following characteristics:

- **S3 Bucket**: For state storage
- **DynamoDB Table**: For state locking
- **IAM Roles**: For secure access to state files
- **State Encryption**: For security of sensitive data

Example remote backend configuration:

```hcl
terraform {
  backend "s3" {
    bucket         = "flowmart-terraform-state"
    key            = "environments/${var.environment}/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "terraform-lock"
    encrypt        = true
    role_arn       = "arn:aws:iam::ACCOUNT_ID:role/TerraformStateManager"
  }
}
```

## Terraform Best Practices

We follow these best practices for our Terraform codebase:

1. **Version Pinning**: Lock provider and module versions to ensure reproducibility

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16.0"
    }
  }
  required_version = ">= 1.2.0"
}
```

2. **Resource Tagging**: All resources are tagged for billing and management purposes

```hcl
tags = {
  Environment = var.environment
  Project     = "FlowMart"
  ManagedBy   = "Terraform"
  Service     = "Orders"
}
```

3. **Variable Validation**: Validate inputs to prevent errors

```hcl
variable "environment" {
  description = "The deployment environment (e.g., dev, staging, production)"
  type        = string
  
  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be one of: dev, staging, production."
  }
}
```

4. **Modular Design**: Use modules for reusable components

5. **Minimal Permissions**: Follow the principle of least privilege for IAM roles

## Next Steps

For more information about our IaC implementation, please refer to:

- [Environment Setups](./03-environment-setups.mdx)
- [CI/CD Pipelines](./04-cicd-pipelines.mdx) 
---
title: Environment Setups
summary: Detailed information about the different environments for the FlowMart e-commerce platform
sidebar:
    label: 03 - Environment Setups
    order: 3
---

# Environment Setups

This document describes the different environments used in the FlowMart e-commerce platform, their purposes, configurations, and the promotion process between them.

## Environment Strategy

We follow a multi-environment strategy with clear separation and purposes:

```mermaid
flowchart TD
    classDef devEnv fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px
    classDef stagingEnv fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    classDef prodEnv fill:#f8cecc,stroke:#b85450,stroke-width:2px
    classDef dataEnv fill:#fff2cc,stroke:#d6b656,stroke-width:2px

    Dev[Development Environment] --> Staging[Staging Environment]
    Staging --> Production[Production Environment]
    
    Dev --- Sandbox[Sandbox Environments]
    Production --- DR[Disaster Recovery]
    
    class Dev,Sandbox devEnv
    class Staging stagingEnv
    class Production,DR prodEnv
    class Data dataEnv
```

## Environment Descriptions

### Development Environment

The development environment is used by developers to test changes and new features.

- **Purpose**: Development, testing, and integration
- **Access**: Development team
- **Data**: Subset of anonymized production data or synthetic data
- **Infrastructure Scale**: Minimal, cost-optimized
- **Deployment Frequency**: Multiple times per day
- **Automated Testing**: Unit tests, API tests

**Key Characteristics**:
- Shared development environment
- Reduced redundancy (e.g., single NAT gateway, smaller instances)
- Feature flags enabled for work-in-progress features
- Debug and verbose logging enabled
- Daily database refresh from anonymized production data

### Staging Environment

The staging environment is a pre-production environment that closely mirrors production.

- **Purpose**: System testing, performance testing, UAT
- **Access**: Development team, QA, selected stakeholders
- **Data**: Full anonymized copy of production data
- **Infrastructure Scale**: Nearly identical to production, but smaller scale
- **Deployment Frequency**: Once per release (multiple times per week)
- **Automated Testing**: Integration tests, performance tests, security scans

**Key Characteristics**:
- Configuration as close to production as possible
- Full feature set enabled
- Production-level logging
- Staged rollout of new features
- Regular (weekly) database refresh from anonymized production data

### Production Environment

The production environment serves real customers and processes real transactions.

- **Purpose**: Serving end-users
- **Access**: Limited access via break-glass procedures
- **Data**: Real customer data
- **Infrastructure Scale**: Full scale, highly available
- **Deployment Frequency**: Multiple times per week, during designated windows
- **Automated Testing**: Smoke tests, canary tests

**Key Characteristics**:
- High availability across multiple availability zones
- Auto-scaling based on demand
- Enhanced security controls
- Full monitoring and alerting
- Regular backups
- Blue/green deployment strategy

### Sandbox Environments

Ephemeral environments for developers to test specific features or changes.

- **Purpose**: Feature development, experimentation
- **Access**: Individual developers or teams
- **Data**: Synthetic data
- **Infrastructure Scale**: Minimal
- **Deployment Frequency**: On-demand
- **Lifetime**: Temporary (hours to days)

### Disaster Recovery Environment

A standby environment that can be activated in case of a major outage in the production environment.

- **Purpose**: Business continuity
- **State**: Warm standby
- **Data**: Regular replication from production
- **Region**: Different from primary production region
- **Activation**: Automated with manual approval

## Environment Configuration

We manage environment-specific configurations through:

1. **Terraform Variables**: Each environment has its own `terraform.tfvars` file
2. **Kubernetes ConfigMaps**: Environment-specific Kubernetes configurations
3. **Environment Variables**: Set at the pod or container level
4. **Feature Flags**: Application-level feature toggles

Example Terraform Variable Differences:

| Variable | Dev | Staging | Production |
|----------|-----|---------|------------|
| `vpc_cidr` | 10.0.0.0/16 | 10.1.0.0/16 | 10.2.0.0/16 |
| `eks_node_count` | 2 | 3 | 5-10 (auto-scaling) |
| `rds_instance_type` | db.t3.medium | db.r5.large | db.r5.2xlarge |
| `rds_multi_az` | false | true | true |
| `enable_waf` | false | true | true |

## Environment Promotion Process

We follow a structured promotion process for changes moving through environments:

```mermaid
sequenceDiagram
    participant Dev as Development
    participant Staging as Staging
    participant Prod as Production
    
    Note over Dev: Feature development complete
    Dev->>Staging: Promote code
    Note over Staging: Run integration tests
    Note over Staging: Performance testing
    Note over Staging: Security scanning
    Note over Staging: UAT approval
    Staging->>Prod: Promote code
    Note over Prod: Canary deployment
    Note over Prod: Monitoring
    Note over Prod: Full rollout
```

### Promotion Guidelines

1. **Development to Staging**:
   - All unit tests pass
   - Code review completed
   - Feature implementation verified in development
   - Feature documentation completed

2. **Staging to Production**:
   - All integration tests pass
   - Performance tests meet SLAs
   - Security scans show no critical or high vulnerabilities
   - UAT completed and signed off
   - Release notes prepared

## Environment Variables Management

We manage environment variables securely using:

1. **AWS Parameter Store**: For non-secret configuration
2. **AWS Secrets Manager**: For sensitive values
3. **Kubernetes Secrets**: Mounted into containers at runtime

Example parameter naming convention:
```
/flowmart/{environment}/{service}/{parameter-name}
```

Example secret access in application code:
```javascript
const AWS = require('aws-sdk');
const ssm = new AWS.SSM();

async function getDatabaseConfig() {
  const params = {
    Name: `/flowmart/${process.env.ENVIRONMENT}/orders-service/db-connection-string`,
    WithDecryption: true
  };
  
  const result = await ssm.getParameter(params).promise();
  return result.Parameter.Value;
}
```

## Network Isolation

Our environments are isolated from each other:

```mermaid
flowchart TB
    subgraph "AWS Account: Production"
        ProdVPC[Production VPC]
    end
    
    subgraph "AWS Account: Non-Production"
        StagingVPC[Staging VPC]
        DevVPC[Development VPC]
    end
    
    Internet[Internet] --> PVPN[Production VPN]
    Internet --> NPVPN[Non-Production VPN]
    
    PVPN --> ProdVPC
    NPVPN --> StagingVPC
    NPVPN --> DevVPC
```

Key security controls:
- Separate AWS accounts for production and non-production
- VPC isolation for each environment
- Separate VPN access for production and non-production
- Restricted traffic between environments
- Different IAM roles for each environment

## Data Management Across Environments

We handle data carefully across environments:

1. **Production**: Real customer data with full security controls
2. **Staging**: Anonymized production data, refreshed weekly
3. **Development**: Subset of anonymized data or synthetic data
4. **Sandbox**: Synthetic data only

Data anonymization process:
```mermaid
flowchart LR
    ProdDB[(Production Database)] --> Extract[Extract Data]
    Extract --> Anonymize[Anonymize Sensitive Data]
    Anonymize --> Load[Load to Non-Prod Environments]
    Load --> StageDB[(Staging Database)]
    Load --> DevDB[(Development Database)]
```

## Monitoring and Observability

Each environment has appropriate monitoring:

| Monitoring Aspect | Development | Staging | Production |
|-------------------|-------------|---------|------------|
| Metrics Collection | Basic | Full | Full |
| Logs Retention | 7 days | 14 days | 90 days |
| Alerting | Critical only | High and Critical | All severities |
| Dashboards | Basic | Full | Full with extended |
| Tracing | Sampled (50%) | Sampled (75%) | Sampled (10%) |

## Next Steps

For more information about our environment management and deployment processes, please refer to:

- [CI/CD Pipelines](./04-cicd-pipelines.mdx) 
---
title: CI/CD Pipelines
summary: Detailed overview of the CI/CD pipelines used to deploy and maintain the FlowMart e-commerce platform
sidebar:
    label: 04 - CI/CD Pipelines
    order: 4
---

# CI/CD Pipelines

This document provides an overview of the Continuous Integration (CI) and Continuous Deployment (CD) pipelines used to build, test, and deploy the FlowMart e-commerce platform.

## CI/CD Philosophy

Our CI/CD approach follows these key principles:

1. **Automation First**: Automate everything that can be automated
2. **Fast Feedback**: Provide developers with quick feedback on their changes
3. **Consistency**: Ensure consistent builds and deployments across all environments
4. **Security**: Integrate security testing throughout the pipeline
5. **Observability**: Monitor and track all deployments and their impacts
6. **Self-service**: Enable teams to deploy independently, but safely

## CI/CD Technology Stack

Our CI/CD pipeline utilizes the following key technologies:

| Technology | Purpose |
|------------|---------|
| GitHub Actions | Main CI/CD orchestration platform |
| ArgoCD | Kubernetes GitOps deployment tool |
| Helm | Kubernetes package management |
| Docker | Container building and registry |
| Terraform | Infrastructure as Code deployment |
| SonarQube | Code quality and security analysis |
| Jest, JUnit, pytest | Unit testing frameworks |
| Playwright | End-to-end testing |
| K6 | Performance testing |
| OWASP ZAP | Security scanning |
| Snyk | Dependency vulnerability scanning |
| AWS ECR | Container registry |

## CI/CD Pipeline Overview

Our CI/CD pipeline consists of multiple stages with specific responsibilities:

```mermaid
flowchart TD
    classDef build fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px
    classDef test fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    classDef deploy fill:#ffe6cc,stroke:#d79b00,stroke-width:2px
    classDef release fill:#f8cecc,stroke:#b85450,stroke-width:2px

    CodePush[Code Push] --> Build[Build & Package]
    Build --> UnitTest[Unit Tests]
    UnitTest --> CodeQuality[Code Quality Analysis]
    CodeQuality --> SecurityScan[Security Scanning]
    SecurityScan --> DockerBuild[Docker Build]
    DockerBuild --> PushRegistry[Push to Registry]
    PushRegistry --> DeployDev[Deploy to Dev]
    DeployDev --> IntegrationTest[Integration Tests]
    IntegrationTest --> DeployStaging[Deploy to Staging]
    DeployStaging --> PerformanceTest[Performance Tests]
    DeployStaging --> E2ETest[End-to-End Tests]
    PerformanceTest --> Approval{Approval}
    E2ETest --> Approval
    Approval -->|Approved| DeployProd[Deploy to Production]
    Approval -->|Rejected| Feedback[Feedback Loop]
    DeployProd --> SmokeTest[Smoke Tests]
    SmokeTest --> Monitoring[Monitoring & Observability]
    
    class Build,DockerBuild build
    class UnitTest,CodeQuality,SecurityScan,IntegrationTest,PerformanceTest,E2ETest,SmokeTest test
    class DeployDev,DeployStaging,DeployProd deploy
    class Approval,Monitoring release
```

## Pipeline Stages in Detail

### 1. Build & Package

- Triggered by code push or pull request
- Compiles application code
- Installs dependencies using package managers (npm, Maven, pip)
- Generates build artifacts
- Built in isolated environments with cached dependencies

```yaml
# Example GitHub Actions code snippet
build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '16'
        cache: 'npm'
    - name: Install dependencies
      run: npm ci
    - name: Build
      run: npm run build
    - name: Upload build artifacts
      uses: actions/upload-artifact@v3
      with:
        name: build-artifacts
        path: build/
```

### 2. Test

Multiple types of tests run in parallel to provide rapid feedback:

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete user flows
- **Performance Tests**: Test application performance under load
- **Security Tests**: Scan for vulnerabilities in code and dependencies

```mermaid
flowchart LR
    subgraph "Test Phase"
        direction TB
        Unit[Unit Tests]
        Integration[Integration Tests]
        E2E[End-to-End Tests]
        Performance[Performance Tests]
        Security[Security Tests]
    end
    
    CodeBase[Code Base] --> Unit
    CodeBase --> Integration
    CodeBase --> E2E
    CodeBase --> Performance
    CodeBase --> Security
    
    Unit --> Results[Test Results]
    Integration --> Results
    E2E --> Results
    Performance --> Results
    Security --> Results
```

### 3. Docker Build & Registry Push

- Builds Docker images for all services
- Tags images with git commit SHA and environment
- Pushes images to AWS ECR
- Scans images for vulnerabilities before pushing

```yaml
# Example GitHub Actions code snippet
docker-build:
  runs-on: ubuntu-latest
  needs: [build, test]
  steps:
    - uses: actions/checkout@v3
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-west-2
    - name: Login to Amazon ECR
      id: login-ecr
      uses: aws-actions/amazon-ecr-login@v1
    - name: Build and push Docker image
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: ${{ steps.login-ecr.outputs.registry }}/flowmart-orders-service:${{ github.sha }}
```

### 4. Deployment

We use GitOps with ArgoCD for managing deployments:

- **Development**: Automatic deployment on successful build
- **Staging**: Automatic deployment after integration tests pass
- **Production**: Manual approval required, then automated deployment

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant GH as GitHub Actions
    participant Reg as Container Registry
    participant Git as Git Repo (Manifests)
    participant Argo as ArgoCD
    participant K8s as Kubernetes Cluster
    
    Dev->>GH: Push Code
    GH->>GH: Build & Test
    GH->>Reg: Push Container Image
    GH->>Git: Update Image Tag in Manifests
    Git->>Argo: Sync (Automatic or Manual)
    Argo->>K8s: Apply Manifests
    K8s->>K8s: Deploy Application
    K8s->>Argo: Report Status
    Argo->>Git: Update Deployment Status
```

### 5. Post-Deployment Verification

- **Smoke Tests**: Quick tests to verify basic functionality
- **Canary Deployment**: Rolling deployment with traffic shifting
- **Monitoring**: Performance and error tracking during and after deployment

## Infrastructure Pipeline

For infrastructure changes, we have a separate pipeline:

```mermaid
flowchart TD
    InfraChange[Infrastructure Change] --> TerraformPlan[Terraform Plan]
    TerraformPlan --> AutoReview[Automated Review]
    AutoReview --> HumanReview[Human Review]
    HumanReview --> Approval{Approved?}
    Approval -->|Yes| TerraformApply[Terraform Apply]
    Approval -->|No| Feedback[Feedback Loop]
    TerraformApply --> Verification[Infrastructure Verification]
    Verification --> Documentation[Update Documentation]
```

## Feature Branch Workflow

We follow a feature branch workflow for development:

```mermaid
gitGraph
    commit
    commit
    branch feature/order-tracking
    checkout feature/order-tracking
    commit
    commit
    commit
    checkout main
    merge feature/order-tracking
    branch feature/payment-gateway
    checkout feature/payment-gateway
    commit
    commit
    checkout main
    merge feature/payment-gateway
    commit
```

## Deployment to Multiple Environments

Our pipeline handles deployments to multiple environments:

```mermaid
flowchart TD
    Build[Build & Test] --> DevDeploy[Deploy to Dev]
    
    DevDeploy --> IntegrationTest[Run Integration Tests]
    IntegrationTest -->|Pass| StagingDeploy[Deploy to Staging]
    IntegrationTest -->|Fail| FixIssues[Fix Issues]
    FixIssues --> Build
    
    StagingDeploy --> StagingTests[Run E2E & Performance Tests]
    StagingTests -->|Pass| ApprovalGate{Approval Gate}
    StagingTests -->|Fail| FixIssues
    
    ApprovalGate -->|Approved| ProdDeploy[Deploy to Production]
    ApprovalGate -->|Rejected| FixIssues
    
    ProdDeploy --> CanaryDeploy[Canary Deployment]
    CanaryDeploy --> Monitor[Monitor]
    Monitor -->|Healthy| FullRollout[Full Rollout]
    Monitor -->|Issues| Rollback[Rollback]
```

## Rollback Strategy

In case of deployment issues, we have an automated rollback strategy:

1. **Immediate Automated Rollback**: Triggered by health checks or error rate spikes
2. **One-Click Manual Rollback**: Available through the deployment dashboard
3. **Previous Version Restoration**: Reverts to the last known good state

```mermaid
sequenceDiagram
    participant Metrics as Metrics System
    participant CD as CD Pipeline
    participant Git as Git Repository
    participant K8s as Kubernetes
    
    Note over Metrics,K8s: New deployment shows issues
    Metrics->>CD: Alert on error threshold exceeded
    CD->>CD: Trigger rollback process
    CD->>Git: Revert to previous manifest version
    Git->>K8s: Apply previous manifests
    K8s->>K8s: Restore previous deployment
    K8s->>CD: Report successful rollback
    CD->>Metrics: Verify metrics returning to normal
```

## Pipeline Security

Security is integrated throughout our pipeline:

- **Secrets Management**: Secrets stored in AWS Secrets Manager and injected at runtime
- **SAST**: Static Application Security Testing integrated in build phase
- **DAST**: Dynamic Application Security Testing during staging deployment
- **Dependency Scanning**: Checks for vulnerable dependencies
- **Container Scanning**: Scans container images for vulnerabilities
- **Infrastructure Scanning**: Checks IaC for security misconfigurations

## Observability

Our pipeline provides comprehensive observability:

- **Deployment Tracking**: Each deployment is traced from commit to production
- **Metrics Collection**: Performance metrics before and after deployment
- **Log Aggregation**: Centralized logging for all pipeline stages
- **Alerting**: Automated alerts for pipeline failures or anomalies
- **Dashboards**: Visual representation of pipeline health and history

Example deployment dashboard:

```mermaid
gantt
    title Recent Deployments Timeline
    dateFormat  YYYY-MM-DD HH:mm
    axisFormat %H:%M
    
    section Orders Service
    Build #452           :a1, 2023-05-10 09:00, 5m
    Deploy to Dev        :a2, after a1, 10m
    Integration Tests    :a3, after a2, 15m
    Deploy to Staging    :a4, after a3, 10m
    E2E Tests            :a5, after a4, 30m
    Deploy to Prod       :a6, after a5, 15m
    
    section Inventory Service
    Build #389           :b1, 2023-05-10 10:00, 5m
    Deploy to Dev        :b2, after b1, 10m
    Integration Tests    :b3, after b2, 15m
    Deploy to Staging    :b4, after b3, 10m
    E2E Tests            :b5, after b4, 30m
    
    section Payment Service
    Build #421           :c1, 2023-05-10 08:30, 5m
    Deploy to Dev        :c2, after c1, 10m
    Integration Tests    :c3, after c2, 15m
    Deploy to Staging    :c4, after c3, 10m
    E2E Tests            :c5, after c4, 30m
    Deploy to Prod       :c6, after c5, 15m
```

## Continuous Improvement

We continuously improve our pipeline through:

1. **Pipeline Metrics**: Track build times, success rates, and deployment frequency
2. **Postmortems**: Document and learn from deployment failures
3. **Automation Improvements**: Regularly identify manual steps for automation
4. **Cross-team Learning**: Share best practices across development teams

## Conclusion

Our CI/CD pipeline provides a robust, secure, and efficient process for deploying changes to the FlowMart platform. By automating the build, test, and deployment processes, we can deliver new features and bug fixes to users quickly and reliably while maintaining high quality standards. 
---
title: High-Level FlowMart System Architecture Overview
summary: A high-level overview of the FlowMart e-commerce system architecture
sidebar:
    label: 01 - High-Level Overview
    order: 1
---

# FlowMart System Architecture: High-Level Overview

This diagram provides a high-level overview of the FlowMart e-commerce platform architecture. It illustrates the main components and how they interact to deliver our online shopping experience.

## Business Context

FlowMart is an e-commerce platform that enables customers to browse products, place orders, make payments, and track shipments. The architecture is designed to be scalable, resilient, and maintainable, following domain-driven design and event-driven architecture principles.

## High-Level Architecture Diagram

```mermaid
flowchart TB
    subgraph "Customer Channels"
        Web["Web Application"]
        Mobile["Mobile Apps"]
        ThirdParty["Third-Party Integrations"]
    end

    subgraph "API Gateway Layer"
        APIGateway["API Gateway / BFF"]
    end

    subgraph "Core Business Domains"
        Orders["Orders Domain"]
        Inventory["Inventory Domain"]
        Payment["Payment Domain"]
        Shipping["Shipping Domain"]
        Subscription["Subscription Domain"]
        Notification["Notification Domain"]
    end

    subgraph "Data Stores"
        OrdersDB[(Orders Database)]
        InventoryDB[(Inventory Database)]
        PaymentDB[(Payment Database)]
        ShippingDB[(Shipping Database)]
        SubscriptionDB[(Subscription Database)]
    end

    subgraph "External Systems"
        PaymentGateways["Payment Gateways"]
        LogisticsProviders["Logistics Providers"]
        EmailSMS["Email/SMS Providers"]
    end

    Web --> APIGateway
    Mobile --> APIGateway
    ThirdParty --> APIGateway
    
    APIGateway --> Orders
    APIGateway --> Inventory
    APIGateway --> Payment
    APIGateway --> Shipping
    APIGateway --> Subscription
    
    Orders <--> OrdersDB
    Inventory <--> InventoryDB
    Payment <--> PaymentDB
    Shipping <--> ShippingDB
    Subscription <--> SubscriptionDB
    
    Orders <--> Inventory
    Orders <--> Payment
    Orders <--> Shipping
    Orders <--> Notification
    Payment <--> Subscription
    
    Payment <--> PaymentGateways
    Shipping <--> LogisticsProviders
    Notification <--> EmailSMS
```

## Component Descriptions

### Customer Channels
- **Web Application**: A responsive web interface for customers to browse products and place orders
- **Mobile Apps**: Native iOS and Android applications for mobile shopping
- **Third-Party Integrations**: External platforms that integrate with our services

### API Gateway Layer
- **API Gateway / BFF**: Backend for Frontend that routes requests, handles authentication, and optimizes responses for different clients

### Core Business Domains
- **Orders Domain**: Manages the order lifecycle from creation to fulfillment
- **Inventory Domain**: Tracks product availability and stock levels
- **Payment Domain**: Processes payments and manages financial transactions
- **Shipping Domain**: Handles order delivery and shipment tracking
- **Subscription Domain**: Manages recurring subscriptions and memberships
- **Notification Domain**: Delivers notifications to customers across different channels

### Data Stores
- Each domain has its dedicated database to ensure domain isolation and independent scalability

### External Systems
- **Payment Gateways**: Third-party services for processing credit card payments
- **Logistics Providers**: External shipping and delivery services
- **Email/SMS Providers**: Services for sending notifications to customers

## Key Architectural Principles

1. **Domain-Driven Design**: Our system is organized around business domains and their bounded contexts
2. **Event-Driven Architecture**: Services communicate primarily through events, enhancing decoupling and scalability
3. **Microservices**: Each domain is implemented as one or more microservices with clear boundaries
4. **API-First Approach**: All functionality is exposed through well-defined APIs
5. **Polyglot Persistence**: Each domain can choose the most appropriate database technology

## Next Steps

For a more detailed view of our architecture, refer to the following documents:
- [Domain-Level Architecture](./02-domain-level-architecture.mdx)
- [Service-Level Architecture](./03-service-level-architecture.mdx)
- [Data Flow Architecture](./04-data-flow-architecture.mdx) 
---
title: FlowMart Domain-Level Architecture
summary: A detailed view of FlowMart's domain architecture showing bounded contexts and domain interactions
sidebar:
    label: 02 - Domain Architecture
    order: 2
---

# FlowMart Domain-Level Architecture

This document describes the domain-level architecture of the FlowMart e-commerce platform, showing how different domains interact with each other through well-defined interfaces and events.

## Domain Architecture Diagram

The following diagram illustrates the bounded contexts of each domain and how they communicate with each other:

```mermaid
flowchart TD
    classDef domainStyle fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef eventStyle fill:#e1f5fe,stroke:#0288d1,stroke-width:1px,color:#01579b
    classDef commandStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px,color:#4a148c
    classDef queryStyle fill:#e8f5e9,stroke:#388e3c,stroke-width:1px,color:#1b5e20

    subgraph Orders["Orders Domain"]
        class Orders domainStyle
        OrdersService["Orders Service"]
        
        subgraph OrderEvents[" "]
            OrderConfirmed["OrderConfirmed Event"]
            OrderCancelled["OrderCancelled Event"]
            OrderAmended["OrderAmended Event"]
        end
        
        subgraph OrderCommands[" "]
            PlaceOrder["PlaceOrder Command"]
        end
        
        subgraph OrderQueries[" "]
            GetOrder["GetOrder Query"]
        end
    end
    
    subgraph Inventory["Inventory Domain"]
        class Inventory domainStyle
        InventoryService["Inventory Service"]
        
        subgraph InventoryEvents[" "]
            InventoryAdjusted["InventoryAdjusted Event"]
            OutOfStock["OutOfStock Event"]
        end
        
        subgraph InventoryCommands[" "]
            AddInventory["AddInventory Command"]
            UpdateInventory["UpdateInventory Command"]
            DeleteInventory["DeleteInventory Command"]
        end
        
        subgraph InventoryQueries[" "]
            GetInventoryStatus["GetInventoryStatus Query"]
            GetInventoryList["GetInventoryList Query"]
        end
    end
    
    subgraph Payment["Payment Domain"]
        class Payment domainStyle
        PaymentService["Payment Service"]
        
        subgraph PaymentEvents[" "]
            PaymentProcessed["PaymentProcessed Event"]
        end
        
        subgraph PaymentCommands[" "]
            PaymentInitiated["PaymentInitiated Command"]
        end
        
        subgraph PaymentQueries[" "]
            GetPaymentStatus["GetPaymentStatus Query"]
        end
    end
    
    subgraph Shipping["Shipping Domain"]
        class Shipping domainStyle
        ShippingService["Shipping Service"]
        
        subgraph ShippingEvents[" "]
            ShipmentCreated["ShipmentCreated Event"]
            ShipmentDispatched["ShipmentDispatched Event"]
            ShipmentInTransit["ShipmentInTransit Event"]
            ShipmentDelivered["ShipmentDelivered Event"]
            DeliveryFailed["DeliveryFailed Event"]
            ReturnInitiated["ReturnInitiated Event"]
        end
        
        subgraph ShippingCommands[" "]
            CreateShipment["CreateShipment Command"]
            UpdateShipmentStatus["UpdateShipmentStatus Command"]
            CancelShipment["CancelShipment Command"]
            CreateReturnLabel["CreateReturnLabel Command"]
        end
    end
    
    subgraph Subscription["Subscription Domain"]
        class Subscription domainStyle
        SubscriptionService["Subscription Service"]
        
        subgraph SubscriptionEvents[" "]
            UserSubscriptionStarted["UserSubscriptionStarted Event"]
            UserSubscriptionCancelled["UserSubscriptionCancelled Event"]
        end
        
        subgraph SubscriptionCommands[" "]
            SubscribeUser["SubscribeUser Command"]
            CancelSubscription["CancelSubscription Command"]
        end
        
        subgraph SubscriptionQueries[" "]
            GetSubscriptionStatus["GetSubscriptionStatus Query"]
        end
    end
    
    subgraph Notification["Notification Domain"]
        class Notification domainStyle
        NotificationService["Notification Service"]
        
        subgraph NotificationQueries[" "]
            GetUserNotifications["GetUserNotifications Query"]
            GetNotificationDetails["GetNotificationDetails Query"]
        end
    end

    %% Domain Interactions through Events
    OrderConfirmed -->|Consumed by| InventoryService
    OrderConfirmed -->|Consumed by| ShippingService
    OrderCancelled -->|Consumed by| InventoryService
    OrderAmended -->|Consumed by| InventoryService
    
    InventoryAdjusted -->|Consumed by| OrdersService
    InventoryAdjusted -->|Consumed by| NotificationService
    OutOfStock -->|Consumed by| NotificationService
    
    PaymentProcessed -->|Consumed by| OrdersService
    PaymentProcessed -->|Consumed by| ShippingService
    PaymentProcessed -->|Consumed by| SubscriptionService
    
    UserSubscriptionCancelled -->|Consumed by| OrdersService

    %% Apply styles to events, commands and queries
    class OrderConfirmed,OrderCancelled,OrderAmended,InventoryAdjusted,OutOfStock,PaymentProcessed,ShipmentCreated,ShipmentDispatched,ShipmentInTransit,ShipmentDelivered,DeliveryFailed,ReturnInitiated,UserSubscriptionStarted,UserSubscriptionCancelled eventStyle
    
    class PlaceOrder,AddInventory,UpdateInventory,DeleteInventory,PaymentInitiated,CreateShipment,UpdateShipmentStatus,CancelShipment,CreateReturnLabel,SubscribeUser,CancelSubscription commandStyle
    
    class GetOrder,GetInventoryStatus,GetInventoryList,GetPaymentStatus,GetSubscriptionStatus,GetUserNotifications,GetNotificationDetails queryStyle
```

## Domain Descriptions

### Orders Domain
The Orders Domain is the central domain of our e-commerce platform. It manages the entire lifecycle of customer orders, from creation to fulfillment. It communicates with other domains to check inventory availability, process payments, and arrange shipping.

**Key Events Published:**
- OrderConfirmed
- OrderCancelled 
- OrderAmended

**Commands:**
- PlaceOrder

**Queries:**
- GetOrder

### Inventory Domain
The Inventory Domain manages product stock levels across all warehouses. It ensures accurate inventory tracking and provides real-time stock information to other domains.

**Key Events Published:**
- InventoryAdjusted
- OutOfStock

**Commands:**
- AddInventory
- UpdateInventory
- DeleteInventory

**Queries:**
- GetInventoryStatus
- GetInventoryList

### Payment Domain
The Payment Domain handles all financial transactions within the platform. It processes customer payments, manages refunds, and communicates with external payment gateways.

**Key Events Published:**
- PaymentProcessed

**Commands:**
- PaymentInitiated

**Queries:**
- GetPaymentStatus

### Shipping Domain
The Shipping Domain manages order delivery to customers. It tracks shipment status, handles returns, and integrates with external logistics providers.

**Key Events Published:**
- ShipmentCreated
- ShipmentDispatched
- ShipmentInTransit
- ShipmentDelivered
- DeliveryFailed
- ReturnInitiated

**Commands:**
- CreateShipment
- UpdateShipmentStatus
- CancelShipment
- CreateReturnLabel

### Subscription Domain
The Subscription Domain manages recurring customer subscriptions. It handles subscription lifecycle, billing cycles, and renewal processes.

**Key Events Published:**
- UserSubscriptionStarted
- UserSubscriptionCancelled

**Commands:**
- SubscribeUser
- CancelSubscription

**Queries:**
- GetSubscriptionStatus

### Notification Domain
The Notification Domain is responsible for sending notifications to customers through various channels like email, SMS, and push notifications.

**Queries:**
- GetUserNotifications
- GetNotificationDetails

## Domain Integration Patterns

The domains in FlowMart's architecture interact using several integration patterns:

1. **Event-Driven Communication**: Most domain interactions occur through asynchronous events published to a message broker, promoting loose coupling.

2. **Synchronous API Calls**: For operations requiring immediate responses, domains expose REST APIs that can be called synchronously.

3. **Saga Pattern**: For complex workflows spanning multiple domains, we use choreography-based sagas where services respond to events to maintain data consistency.

4. **CQRS**: We separate command (write) and query (read) operations, allowing for optimization of each path.

## Next Steps

For more detailed architectural information, see:
- [Service-Level Architecture](./03-service-level-architecture.mdx)
- [Data Flow Architecture](./04-data-flow-architecture.mdx) 
---
title: FlowMart Service-Level Architecture
summary: A detailed view of the services within each domain and their interactions
sidebar:
    label: 03 - Service Architecture
    order: 3
---

# FlowMart Service-Level Architecture

This document provides a detailed view of the individual services within FlowMart's e-commerce platform, their responsibilities, and how they interact.

## Service Architecture Overview

The following diagram illustrates the services that make up our platform and how they communicate:

```mermaid
flowchart TD
    classDef apiGateway fill:#f8cecc,stroke:#b85450,stroke-width:2px
    classDef orderService fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px
    classDef inventoryService fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    classDef paymentService fill:#ffe6cc,stroke:#d79b00,stroke-width:2px
    classDef shippingService fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    classDef notificationService fill:#fff2cc,stroke:#d6b656,stroke-width:2px
    classDef subscriptionService fill:#f8cecc,stroke:#b85450,stroke-width:2px
    classDef datastore fill:#f5f5f5,stroke:#666666,stroke-width:1px
    classDef messagebroker fill:#e6ffcc,stroke:#36b37e,stroke-width:2px
    classDef externalSystem fill:#f5f5f5,stroke:#666666,stroke-width:1px,stroke-dasharray: 5 5

    APIGateway[API Gateway]
    EventBus[Event Bus / Message Broker]
    
    subgraph OrdersDomain["Orders Domain"]
        OrdersService[Orders Service]
        OrdersDB[(Orders Database)]
    end
    
    subgraph InventoryDomain["Inventory Domain"]
        InventoryService[Inventory Service]
        InventoryDB[(Inventory Database)]
    end
    
    subgraph PaymentDomain["Payment Domain"]
        PaymentService[Payment Service]
        PaymentDB[(Payment Database)]
    end
    
    subgraph ShippingDomain["Shipping Domain"]
        ShippingService[Shipping Service]
        ShippingDB[(Shipping Database)]
    end
    
    subgraph NotificationDomain["Notification Domain"]
        NotificationService[Notification Service]
    end
    
    subgraph SubscriptionDomain["Subscription Domain"]
        SubscriptionService[Subscription Service]
        SubscriptionDB[(Subscription Database)]
    end
    
    subgraph ExternalSystems["External Systems"]
        PaymentGateway[Payment Gateway]
        EmailProvider[Email Provider]
        SMSProvider[SMS Provider]
        LogisticsPartner[Logistics Partner]
    end
    
    %% API Gateway connections
    APIGateway --> OrdersService
    APIGateway --> InventoryService
    APIGateway --> PaymentService
    APIGateway --> ShippingService
    APIGateway --> SubscriptionService
    
    %% Database connections
    OrdersService <--> OrdersDB
    InventoryService <--> InventoryDB
    PaymentService <--> PaymentDB
    ShippingService <--> ShippingDB
    SubscriptionService <--> SubscriptionDB
    
    %% Event bus connections
    OrdersService <--> EventBus
    InventoryService <--> EventBus
    PaymentService <--> EventBus
    ShippingService <--> EventBus
    NotificationService <--> EventBus
    SubscriptionService <--> EventBus
    
    %% External system connections
    PaymentService --> PaymentGateway
    NotificationService --> EmailProvider
    NotificationService --> SMSProvider
    ShippingService --> LogisticsPartner
    
    %% Apply styles
    class APIGateway apiGateway
    class OrdersService orderService
    class InventoryService inventoryService
    class PaymentService paymentService
    class ShippingService shippingService
    class NotificationService notificationService
    class SubscriptionService subscriptionService
    class OrdersDB,InventoryDB,PaymentDB,ShippingDB,SubscriptionDB datastore
    class EventBus messagebroker
    class PaymentGateway,EmailProvider,SMSProvider,LogisticsPartner externalSystem
```

## Service Component Details

### API Gateway
- **Description**: Entry point for all client requests, handles routing, authentication, and load balancing
- **Technologies**: AWS API Gateway, Kong, or Nginx
- **Key Responsibilities**:
  - Route requests to appropriate services
  - Handle authentication and authorization
  - API rate limiting and throttling
  - Request validation
  - Response caching

### Orders Service
- **Description**: Manages the entire lifecycle of customer orders
- **Technologies**: Node.js, Express, MongoDB
- **Key Responsibilities**:
  - Create and manage orders
  - Process order amendments and cancellations
  - Coordinate with other services for order fulfillment
  - Maintain order history and status
- **Key Events**:
  - Publishes: OrderConfirmed, OrderCancelled, OrderAmended
  - Consumes: InventoryAdjusted, PaymentProcessed, UserSubscriptionCancelled

### Inventory Service
- **Description**: Tracks and manages product inventory across warehouses
- **Technologies**: Java, Spring Boot, PostgreSQL
- **Key Responsibilities**:
  - Maintain accurate inventory levels
  - Process inventory adjustments
  - Monitor stock levels and trigger alerts
  - Support inventory queries
- **Key Events**:
  - Publishes: InventoryAdjusted, OutOfStock
  - Consumes: OrderConfirmed, OrderCancelled, OrderAmended

### Payment Service
- **Description**: Handles all payment processing and financial transactions
- **Technologies**: Node.js, Express, PostgreSQL
- **Key Responsibilities**:
  - Process customer payments
  - Manage refunds and chargebacks
  - Integrate with payment gateways
  - Track payment status
- **Key Events**:
  - Publishes: PaymentProcessed
  - Consumes: PaymentInitiated, UserSubscriptionStarted, InventoryAdjusted

### Shipping Service
- **Description**: Manages logistics and shipment of orders
- **Technologies**: Python, Flask, MongoDB
- **Key Responsibilities**:
  - Create and track shipments
  - Integrate with logistics providers
  - Process returns and exchanges
  - Calculate shipping costs
- **Key Events**:
  - Publishes: ShipmentCreated, ShipmentDispatched, ShipmentInTransit, ShipmentDelivered, DeliveryFailed, ReturnInitiated
  - Consumes: OrderConfirmed, PaymentProcessed

### Notification Service
- **Description**: Delivers notifications to customers through various channels
- **Technologies**: Node.js, Express, Redis
- **Key Responsibilities**:
  - Send transactional emails
  - Deliver SMS notifications
  - Push mobile app notifications
  - Store notification history
- **Key Events**:
  - Consumes: InventoryAdjusted, OutOfStock, PaymentProcessed

### Subscription Service
- **Description**: Manages recurring subscriptions and memberships
- **Technologies**: Java, Spring Boot, MySQL
- **Key Responsibilities**:
  - Handle subscription lifecycle
  - Process recurring billing
  - Manage subscription plans and tiers
  - Track subscription status
- **Key Events**:
  - Publishes: UserSubscriptionStarted, UserSubscriptionCancelled
  - Consumes: PaymentProcessed

### Event Bus / Message Broker
- **Description**: Central messaging system that enables asynchronous communication between services
- **Technologies**: Apache Kafka, RabbitMQ, or AWS SNS/SQS
- **Key Responsibilities**:
  - Reliable event delivery
  - Support for event persistence
  - Message routing
  - Scalable message throughput

## Service Interaction Patterns

### Synchronous Communication
Services communicate directly with each other through REST APIs for operations that require immediate responses.

```mermaid
sequenceDiagram
    participant Client
    participant OrdersService
    participant InventoryService
    participant PaymentService
    
    Client->>OrdersService: Place Order
    OrdersService->>InventoryService: Check Inventory Availability
    InventoryService-->>OrdersService: Inventory Available
    OrdersService->>PaymentService: Process Payment
    PaymentService-->>OrdersService: Payment Successful
    OrdersService-->>Client: Order Confirmation
```

### Asynchronous Communication
Services communicate through events published to the event bus, allowing for loose coupling.

```mermaid
sequenceDiagram
    participant OrdersService
    participant EventBus
    participant InventoryService
    participant ShippingService
    participant NotificationService
    
    OrdersService->>EventBus: Publish OrderConfirmed Event
    EventBus->>InventoryService: OrderConfirmed Event
    InventoryService->>EventBus: Publish InventoryAdjusted Event
    EventBus->>ShippingService: OrderConfirmed Event
    ShippingService->>EventBus: Publish ShipmentCreated Event
    EventBus->>NotificationService: ShipmentCreated Event
    NotificationService->>Customer: Send Shipment Notification
```

## Infrastructure Considerations

- All services are containerized using Docker and orchestrated with Kubernetes
- Services are deployed across multiple availability zones for high availability
- Auto-scaling is configured based on CPU and memory metrics
- Database replication and backups are implemented for data durability
- Centralized logging and monitoring using Prometheus and Grafana

## Next Steps

For more information about data flows within the system, refer to:
- [Data Flow Architecture](./04-data-flow-architecture.mdx) 
---
title: Cloud Infrastructure Strategy
summary: Architectural decision record for cloud infrastructure approach for the FlowMart e-commerce platform
sidebar:
    label: Cloud Infrastructure Strategy
    order: 1
---

# DRAFT - NOT YET APPROVED

:::warning
This is a draft ADR. It is not yet approved and should not be used as a reference.
:::

## ADR-007: Cloud Infrastructure Strategy for FlowMart E-commerce Platform

### Status

Draft (Last Updated: 2024-09-25)

<Flow id="PaymentFlow" version="latest" includeKey={false} />
<Flow id="PaymentFlow" version="latest" includeKey={false} />
<Flow id="PaymentFlow" version="latest" includeKey={false} />

### Context

As part of our transition to a microservices architecture, we need to define our cloud infrastructure strategy to support the new FlowMart e-commerce platform. Our current infrastructure consists primarily of on-premises data centers with some workloads in AWS, creating operational and scaling challenges:

1. **Infrastructure Provisioning**: Manual processes for provisioning infrastructure lead to long lead times for new environments and services.

2. **Scaling Limitations**: Physical hardware constraints prevent rapid scaling during peak shopping periods.

3. **High Operational Overhead**: Significant effort required for hardware maintenance, patching, and capacity management.

4. **Disaster Recovery Challenges**: Limited geographic redundancy and complex DR procedures.

5. **Cloud Fragmentation**: Ad-hoc adoption of cloud services has created inconsistent practices and tooling.

6. **Developer Experience**: Complex local development setup and environment inconsistencies slow down development cycles.

7. **Cost Management**: Difficult to attribute infrastructure costs to specific business capabilities or teams.

8. **Security Compliance**: Maintaining compliance across hybrid infrastructure requires duplicate controls and auditing.

We need a cohesive infrastructure strategy that enables rapid delivery, scalability, and operational efficiency for our new e-commerce platform.

### Decision

We will adopt a **cloud-native infrastructure strategy** with a **multi-cloud capability** but **AWS-primary approach**. Key aspects of this strategy include:

1. **Primary Cloud Platform**:
   - AWS will be our primary cloud provider for all new workloads
   - Azure will be maintained as a secondary provider for specific use cases (e.g., Microsoft-ecosystem services)
   - GCP may be selectively used for specialized AI/ML workloads

2. **Infrastructure as Code (IaC)**:
   - Terraform as primary IaC tool for provisioning cloud resources
   - AWS CDK for complex, AWS-specific resource configurations
   - GitOps-based deployment workflows with infrastructure CI/CD pipelines

3. **Containerization Strategy**:
   - Containerize all new microservices using Docker
   - Amazon EKS (Kubernetes) as primary container orchestration platform
   - Amazon ECR for container registry with cross-region replication

4. **Platform Services Over Custom Infrastructure**:
   - Prefer managed services over self-managed infrastructure where possible
   - AWS RDS, DocumentDB, ElastiCache for database needs
   - AWS MSK (Managed Kafka) for event streaming
   - CloudFront for CDN and edge caching

5. **Multi-Region Architecture**:
   - Primary operations in AWS US-East-1 and US-West-2
   - Active-active configuration for critical services
   - Region-specific deployments for EU and APAC markets to address data residency

6. **Landing Zone and Account Structure**:
   - Hub-and-spoke model with centralized security and governance
   - Separate AWS accounts for production, staging, development, and sandbox environments
   - Service-oriented account structure within each environment category
   - Centralized logging, monitoring, and security controls

7. **Network Architecture**:
   - Transit Gateway for interconnecting VPCs and on-premises
   - VPC design aligned with microservice domains
   - AWS PrivateLink for service-to-service connectivity
   - AWS Shield and WAF for DDoS protection and application security

8. **Cost Optimization**:
   - Tagging strategy for cost allocation and tracking
   - Automated cost monitoring and anomaly detection
   - Leverage Savings Plans and Reserved Instances strategically
   - Implemented auto-scaling for elastic workloads

### Infrastructure Architecture by Domain

| Domain | Primary Services | Scaling Strategy | Special Requirements |
|--------|------------------|------------------|----------------------|
| Product Catalog | EKS, ElastiCache, DocumentDB | Horizontal pod scaling, Read replicas | High read throughput, Global availability |
| Order Processing | EKS, RDS (PostgreSQL), MSK | Horizontal pod scaling, DB connection pooling | Strong consistency, Transaction support |
| Payment | EKS, RDS (PostgreSQL), KMS | Fixed scaling with headroom | PCI-DSS compliance, Encryption requirements |
| Inventory | EKS, DocumentDB, Lambda | Horizontal auto-scaling | Event-sourcing patterns, Eventual consistency |
| User Authentication | Cognito, Lambda, DynamoDB | Regional deployments | Multi-factor auth, Token management |
| Content Delivery | S3, CloudFront, Lambda@Edge | Edge caching, Regional replication | Image optimization, Low latency delivery |
| Search | OpenSearch, Lambda, EKS | Search domain scaling, Query throttling | High cardinality, Complex query support |
| Analytics | Redshift, Kinesis, EMR | Workload-based scaling | Batch processing, Data lake integration |

### Consequences

#### Positive

1. **Improved Scalability**: Elastic infrastructure that scales with demand without manual intervention.

2. **Faster Time-to-Market**: Automated provisioning and deployment enable rapid delivery of new features.

3. **Enhanced Resilience**: Multi-region architecture improves availability and disaster recovery capabilities.

4. **Cost Efficiency**: Pay-for-use model and automated scaling optimize infrastructure costs.

5. **Developer Productivity**: Consistent environments and self-service capabilities improve developer experience.

6. **Security Improvements**: Standardized security controls and automated compliance checks.

7. **Operational Efficiency**: Reduced operational overhead through managed services and automation.

8. **Global Reach**: Ability to deploy services closer to customers in different geographic regions.

#### Negative

1. **Cloud Vendor Dependency**: While designed for multi-cloud, primary workloads will have AWS dependencies.

2. **Cost Management Complexity**: Cloud costs can escalate without proper governance and monitoring.

3. **Skill Set Transition**: Team needs to develop new skills in cloud-native technologies and practices.

4. **Increased Architectural Complexity**: Distributed cloud architecture is more complex to design and troubleshoot.

5. **Security Model Changes**: Cloud security requires different approaches and tools than on-premises.

6. **Data Transfer Costs**: Cross-region and internet data transfer can become a significant cost factor.

7. **Service Maturity Variations**: Some AWS services are more mature and reliable than others.

### Mitigation Strategies

1. **Cloud Platform Team**:
   - Create a dedicated platform engineering team for cloud infrastructure
   - Develop reusable infrastructure modules and patterns
   - Provide internal consultation and support to service teams

2. **Cloud Center of Excellence (CCoE)**:
   - Establish cloud best practices and governance
   - Regular architecture reviews and guidance
   - Develop certification and training program for engineering teams

3. **Cloud Financial Management**:
   - Implement FinOps practices and tooling
   - Regular cost reviews and optimization cycles
   - Showback/chargeback mechanisms to drive accountability

4. **Abstraction Layers**:
   - Create service abstractions to minimize direct cloud provider coupling
   - Develop infrastructure interfaces that could support multiple providers
   - Use cloud-agnostic tools and practices where practical

5. **Hybrid Transition Strategy**:
   - Phased migration from on-premises to cloud
   - Maintain hybrid capabilities during transition period
   - Clear exit criteria for legacy infrastructure decommissioning

### Implementation Details

#### Phase 1: Foundation (Q4 2024)

1. Establish AWS Landing Zone and account structure
2. Implement core networking and security controls
3. Set up CI/CD pipelines for infrastructure
4. Deploy EKS clusters for development and staging
5. Migrate first non-critical workloads

#### Phase 2: Production Migration (Q1-Q2 2025)

1. Deploy production EKS clusters and platform services
2. Migrate core services to cloud infrastructure
3. Implement multi-region capabilities for critical services
4. Establish cloud cost management and optimization
5. Complete developer tooling and self-service capabilities

#### Phase 3: Advanced Capabilities (Q3-Q4 2025)

1. Implement advanced security and compliance controls
2. Deploy cross-region data synchronization
3. Optimize for global performance and availability
4. Enhance disaster recovery capabilities
5. Begin decommissioning legacy infrastructure

### Considered Alternatives

#### 1. Maintain and Expand On-Premises Infrastructure

**Pros**: Full control, potentially lower ongoing costs for stable workloads, no data sovereignty concerns  
**Cons**: Limited agility, high capital expenditure, scaling limitations, operational overhead

This approach would not provide the agility and scalability needed for our strategic growth and would perpetuate our current limitations.

#### 2. Single Cloud Provider (AWS Only)

**Pros**: Simplified operations, deeper integration between services, volume discounts, focused expertise  
**Cons**: Vendor lock-in, limited negotiating leverage, regional provider limitations

While simpler operationally, this approach would increase our dependency on a single provider and limit flexibility.

#### 3. Multi-Cloud with Equal Workload Distribution

**Pros**: Maximize negotiating leverage, no single provider dependency, best-of-breed services  
**Cons**: Significantly increased complexity, higher operations costs, fragmented expertise, integration challenges

The operational complexity and cost of maintaining equal capabilities across multiple cloud providers outweighs the benefits for our current needs.

#### 4. Cloud Service Provider (CSP) Abstraction Layer

**Pros**: Provider independence, standardized interfaces, easier migration between providers  
**Cons**: Significant development overhead, lowest common denominator functionality, performance impacts

Building comprehensive abstractions across cloud providers would create substantial engineering overhead and limit access to valuable provider-specific capabilities.

### References

1. AWS Well-Architected Framework ([AWS Documentation](https://aws.amazon.com/architecture/well-architected/))
2. "Cloud Strategy Leadership" (Gartner)
3. "Architecting for the Cloud: AWS Best Practices" ([AWS Whitepaper](https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf))
4. "Multi-cloud: The good, the bad and the ugly" (ThoughtWorks Technology Radar)
5. Terraform Documentation ([Terraform.io](https://www.terraform.io/docs/))
6. "Cloud Native Infrastructure" by Justin Garrison and Kris Nova

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-09-10 | 0.1 | Initial draft | Marcus Johnson |
| 2024-09-18 | 0.2 | Added implementation phases and domain details | Patricia Lopez |
| 2024-09-25 | 0.3 | Incorporated feedback from architecture review | David Boyne |
| TBD | 1.0 | Pending approval | Architecture Board |

## Appendix A: Cloud Infrastructure Architecture

```mermaid
flowchart TB
    subgraph "AWS Global"
        subgraph "AWS Organizations"
            org[Management Account]
            security[Security Account]
            shared[Shared Services Account]
            log[Logging Account]
            net[Network Account]
            
            subgraph "Production"
                prod1[Product Domain]
                prod2[Order Domain]
                prod3[Customer Domain]
                prod4[Payment Domain]
            end
            
            subgraph "Non-Production"
                dev[Development]
                stage[Staging]
                test[Testing]
                sandbox[Sandbox]
            end
        end
    end
    
    subgraph "On-Premises"
        dc[Data Center]
        legacy[Legacy Systems]
    end
    
    subgraph "Network Fabric"
        dx[Direct Connect]
        tgw[Transit Gateway]
        vpn[VPN]
        cf[CloudFront]
    end
    
    org --> security
    org --> shared
    org --> log
    org --> net
    org --> prod1
    org --> prod2
    org --> prod3
    org --> prod4
    org --> dev
    org --> stage
    org --> test
    org --> sandbox
    
    dc --> dx
    dc --> vpn
    legacy --> dx
    
    dx --> tgw
    vpn --> tgw
    
    tgw --> net
    net --> prod1
    net --> prod2
    net --> prod3
    net --> prod4
    net --> dev
    net --> stage
    
    cf --> prod1
    cf --> prod2
    cf --> prod3
    cf --> prod4
```

## Appendix B: Deployment Architecture

```mermaid
flowchart LR
    subgraph "Developer Experience"
        ide[IDE Plugins]
        cli[CLI Tools]
        local[Local Dev Environment]
    end
    
    subgraph "CI/CD Pipeline"
        git[Git Repository]
        build[Build System]
        test[Automated Tests]
        scan[Security Scans]
        artifact[Artifact Repository]
    end
    
    subgraph "GitOps Deployment"
        config[Config Repository]
        argocd[ArgoCD]
        flux[Flux]
    end
    
    subgraph "AWS EKS Clusters"
        subgraph "Development"
            devNS1[Team 1 Namespace]
            devNS2[Team 2 Namespace]
        end
        
        subgraph "Staging"
            stageNS1[Team 1 Namespace]
            stageNS2[Team 2 Namespace]
        end
        
        subgraph "Production"
            prodNS1[Team 1 Namespace]
            prodNS2[Team 2 Namespace]
        end
    end
    
    ide --> git
    cli --> git
    local --> git
    
    git --> build
    build --> test
    test --> scan
    scan --> artifact
    
    artifact --> config
    config --> argocd
    config --> flux
    
    argocd --> devNS1
    argocd --> devNS2
    argocd --> stageNS1
    argocd --> stageNS2
    argocd --> prodNS1
    argocd --> prodNS2
    
    flux --> devNS1
    flux --> devNS2
    flux --> stageNS1
    flux --> stageNS2
    flux --> prodNS1
    flux --> prodNS2
```

## Appendix C: AWS Account Structure

```mermaid
flowchart TB
    subgraph "Management & Governance"
        mgmt[Management Account]
        style mgmt fill:#f9f,stroke:#333,stroke-width:2px
        
        security[Security Account]
        audit[Audit Account]
        shared[Shared Services]
        network[Network Account]
        
        mgmt --> security
        mgmt --> audit
        mgmt --> shared
        mgmt --> network
    end
    
    subgraph "Production OU"
        prodOU[Production]
        
        payment[Payment Services]
        order[Order Services]
        product[Product Catalog]
        identity[Identity Services]
        content[Content Services]
        analytics[Analytics]
        
        prodOU --> payment
        prodOU --> order
        prodOU --> product
        prodOU --> identity
        prodOU --> content
        prodOU --> analytics
    end
    
    subgraph "Non-Production OU"
        nonProdOU[Non-Production]
        
        dev[Development]
        stage[Staging]
        test[Testing]
        sandbox[Sandbox]
        
        nonProdOU --> dev
        nonProdOU --> stage
        nonProdOU --> test
        nonProdOU --> sandbox
    end
    
    mgmt --> prodOU
    mgmt --> nonProdOU
``` 
---
title: FlowMart Data Flow Architecture
summary: A detailed view of key data flows and business processes within the FlowMart e-commerce platform
sidebar:
    label: 04 - Data Flow Architecture
    order: 4
---

# FlowMart Data Flow Architecture

This document illustrates the key data flows within the FlowMart e-commerce platform, focusing on the most important business processes and how data moves through the system.

## Key Business Process Flows

### Order Placement and Fulfillment Flow

This diagram shows the complete flow from order placement to order fulfillment:

```mermaid
flowchart TD
    classDef customerAction fill:#ffcccc,stroke:#ff0000
    classDef systemProcess fill:#ccffcc,stroke:#00aa00
    classDef decisionPoint fill:#ffffcc,stroke:#ffcc00
    classDef externalSystem fill:#ccccff,stroke:#0000ff
    classDef dataStore fill:#f5f5f5,stroke:#333333

    Start([Customer starts checkout]) --> ValidateCart[Validate Shopping Cart]
    class Start customerAction
    
    ValidateCart --> CartValid{Is cart valid?}
    class ValidateCart systemProcess
    class CartValid decisionPoint
    
    CartValid -->|No| UpdateCart[Customer updates cart]
    class UpdateCart customerAction
    
    UpdateCart --> ValidateCart
    
    CartValid -->|Yes| CheckInventory[Check Inventory Availability]
    class CheckInventory systemProcess
    
    CheckInventory --> InventoryAvailable{Inventory available?}
    class InventoryAvailable decisionPoint
    
    InventoryAvailable -->|No| NotifyCustomer[Notify Customer of Unavailability]
    class NotifyCustomer systemProcess
    
    NotifyCustomer --> UpdateCart
    
    InventoryAvailable -->|Yes| ProcessPayment[Process Payment]
    class ProcessPayment systemProcess
    
    ProcessPayment --> PaymentGateway[Payment Gateway]
    class PaymentGateway externalSystem
    
    PaymentGateway --> PaymentSuccessful{Payment successful?}
    class PaymentSuccessful decisionPoint
    
    PaymentSuccessful -->|No| NotifyPaymentFailure[Notify Payment Failure]
    class NotifyPaymentFailure systemProcess
    
    NotifyPaymentFailure --> UpdatePayment[Customer updates payment]
    class UpdatePayment customerAction
    
    UpdatePayment --> ProcessPayment
    
    PaymentSuccessful -->|Yes| CreateOrder[Create Order]
    class CreateOrder systemProcess
    
    CreateOrder --> OrderDB[(Orders Database)]
    class OrderDB dataStore
    
    CreateOrder --> ReserveInventory[Reserve Inventory]
    class ReserveInventory systemProcess
    
    ReserveInventory --> InventoryDB[(Inventory Database)]
    class InventoryDB dataStore
    
    ReserveInventory --> CreateShipment[Create Shipment]
    class CreateShipment systemProcess
    
    CreateShipment --> ShipmentDB[(Shipment Database)]
    class ShipmentDB dataStore
    
    CreateShipment --> NotifyCustomerOrder[Send Order Confirmation]
    class NotifyCustomerOrder systemProcess
    
    NotifyCustomerOrder --> End([Order Placement Complete])
    class End customerAction
```

### Payment Processing Flow

This diagram details the payment processing flow:

```mermaid
sequenceDiagram
    participant Customer
    participant OrdersService
    participant PaymentService
    participant PaymentGateway
    participant PaymentDB
    participant EventBus
    participant NotificationService

    Customer->>OrdersService: Place Order
    OrdersService->>PaymentService: Request Payment
    PaymentService->>PaymentGateway: Process Payment
    
    alt Payment Successful
        PaymentGateway->>PaymentService: Confirm Payment
        PaymentService->>PaymentDB: Store Payment Information
        PaymentService->>EventBus: Publish PaymentProcessed Event
        EventBus->>OrdersService: PaymentProcessed Event
        EventBus->>NotificationService: PaymentProcessed Event
        NotificationService->>Customer: Send Payment Confirmation
        OrdersService->>Customer: Complete Order
    else Payment Failed
        PaymentGateway->>PaymentService: Payment Failure
        PaymentService->>PaymentDB: Log Failed Transaction
        PaymentService->>OrdersService: Payment Failed Response
        OrdersService->>Customer: Request Different Payment Method
    end
```

### Inventory Management Flow

This diagram shows how inventory is managed across the system:

```mermaid
stateDiagram-v2
    [*] --> Available: Initial Stock
    
    Available --> Reserved: Customer Places Order
    Reserved --> Allocated: Order Confirmed
    Reserved --> Available: Order Cancelled
    
    Allocated --> Shipped: Order Shipped
    Shipped --> Delivered: Order Delivered
    Delivered --> [*]
    
    Available --> Replenished: Inventory Low
    Replenished --> Available: Stock Received
    
    Available --> OutOfStock: All Units Reserved
    OutOfStock --> Available: Replenishment
```

### Subscription Processing Flow

This diagram illustrates the subscription management flow:

```mermaid
flowchart TD
    classDef process fill:#d5e8d4,stroke:#82b366
    classDef event fill:#dae8fc,stroke:#6c8ebf
    classDef externalSystem fill:#f5f5f5,stroke:#666666,stroke-width:1px
    classDef decision fill:#fff2cc,stroke:#d6b656

    Start([Start Subscription Process]) --> NewSubscription[Create Subscription]
    class NewSubscription process

    NewSubscription --> InitialPayment[Process Initial Payment]
    class InitialPayment process
    
    InitialPayment --> PaymentSystem[Payment Gateway]
    class PaymentSystem externalSystem
    
    PaymentSystem --> PaymentSuccessful{Payment Successful?}
    class PaymentSuccessful decision
    
    PaymentSuccessful -->|Yes| ActivateSubscription[Activate Subscription]
    class ActivateSubscription process
    
    PaymentSuccessful -->|No| FailedSubscription[Failed Subscription]
    class FailedSubscription process
    
    FailedSubscription --> NotifyFailure[Notify Customer of Failure]
    class NotifyFailure process
    
    ActivateSubscription --> UserSubscriptionStarted[Publish UserSubscriptionStarted Event]
    class UserSubscriptionStarted event
    
    UserSubscriptionStarted --> ScheduleRenewal[Schedule Next Renewal]
    class ScheduleRenewal process
    
    ScheduleRenewal --> TimeForRenewal{Time for Renewal?}
    class TimeForRenewal decision
    
    TimeForRenewal -->|Yes| ProcessRenewalPayment[Process Renewal Payment]
    class ProcessRenewalPayment process
    
    TimeForRenewal -->|No| Wait[Wait for Renewal Date]
    class Wait process
    
    Wait --> TimeForRenewal
    
    ProcessRenewalPayment --> PaymentSystem
    
    PaymentSystem --> RenewalSuccessful{Renewal Successful?}
    class RenewalSuccessful decision
    
    RenewalSuccessful -->|Yes| ExtendSubscription[Extend Subscription]
    class ExtendSubscription process
    
    RenewalSuccessful -->|No, after retries| CancelSubscription[Cancel Subscription]
    class CancelSubscription process
    
    ExtendSubscription --> ScheduleRenewal
    
    CancelSubscription --> UserSubscriptionCancelled[Publish UserSubscriptionCancelled Event]
    class UserSubscriptionCancelled event
    
    UserSubscriptionCancelled --> End([End Subscription Process])
```

## Detailed Data Flow Examples

### Customer Order Flow

The following diagram shows the data flow when a customer places an order:

```mermaid
sequenceDiagram
    participant Customer
    participant Web/Mobile App
    participant API Gateway
    participant OrdersService
    participant InventoryService
    participant PaymentService
    participant ShippingService
    participant NotificationService
    participant EventBus

    Customer->>Web/Mobile App: Add items to cart
    Customer->>Web/Mobile App: Proceed to checkout
    Web/Mobile App->>API Gateway: POST /orders
    API Gateway->>OrdersService: Create order request
    
    OrdersService->>InventoryService: Check inventory availability
    InventoryService-->>OrdersService: Inventory status
    
    OrdersService->>PaymentService: Process payment
    PaymentService-->>OrdersService: Payment result
    
    alt Order Successful
        OrdersService->>EventBus: Publish OrderConfirmed
        EventBus->>InventoryService: OrderConfirmed
        InventoryService->>EventBus: Publish InventoryAdjusted
        EventBus->>ShippingService: OrderConfirmed
        ShippingService->>EventBus: Publish ShipmentCreated
        EventBus->>NotificationService: OrderConfirmed
        NotificationService->>Customer: Send order confirmation
    else Order Failed
        OrdersService->>EventBus: Publish OrderFailed
        EventBus->>NotificationService: OrderFailed
        NotificationService->>Customer: Send failure notification
    end
```

### Product Return Flow

The following diagram shows the data flow when a customer returns a product:

```mermaid
sequenceDiagram
    participant Customer
    participant Web/Mobile App
    participant API Gateway
    participant OrdersService
    participant ShippingService
    participant InventoryService
    participant PaymentService
    participant NotificationService
    participant EventBus

    Customer->>Web/Mobile App: Request return
    Web/Mobile App->>API Gateway: POST /returns
    API Gateway->>OrdersService: Create return request
    OrdersService->>ShippingService: Generate return label
    
    ShippingService->>EventBus: Publish ReturnInitiated
    EventBus->>NotificationService: ReturnInitiated
    NotificationService->>Customer: Send return instructions
    
    Note over Customer,ShippingService: Customer ships the item back
    
    ShippingService->>EventBus: Publish ReturnReceived
    EventBus->>InventoryService: ReturnReceived
    InventoryService->>EventBus: Publish InventoryAdjusted
    
    EventBus->>PaymentService: ReturnReceived
    PaymentService->>EventBus: Publish RefundIssued
    
    EventBus->>NotificationService: RefundIssued
    NotificationService->>Customer: Send refund confirmation
```

## Data Storage Overview

The following diagram provides a high-level overview of the data storage architecture:

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ SUBSCRIPTION : subscribes
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER ||--|| SHIPMENT : fulfilled-by
    ORDER ||--|| PAYMENT : paid-by
    PRODUCT ||--o{ ORDER_ITEM : included-in
    PRODUCT ||--o{ INVENTORY : stocked-as
    WAREHOUSE ||--o{ INVENTORY : holds
    SUBSCRIPTION ||--o{ SUBSCRIPTION_PAYMENT : generates
    
    CUSTOMER {
        string id PK
        string firstName
        string lastName
        string email
        string phone
        datetime createdAt
    }
    
    ORDER {
        string id PK
        string customerId FK
        string status
        decimal totalAmount
        datetime orderDate
    }
    
    ORDER_ITEM {
        string id PK
        string orderId FK
        string productId FK
        int quantity
        decimal unitPrice
    }
    
    PRODUCT {
        string id PK
        string name
        string description
        decimal price
        string category
    }
    
    INVENTORY {
        string id PK
        string productId FK
        string warehouseId FK
        int quantity
        int reserved
    }
    
    WAREHOUSE {
        string id PK
        string name
        string location
    }
    
    SHIPMENT {
        string id PK
        string orderId FK
        string status
        string trackingNumber
        datetime shippedDate
    }
    
    PAYMENT {
        string id PK
        string orderId FK
        decimal amount
        string paymentMethod
        string status
        datetime paymentDate
    }
    
    SUBSCRIPTION {
        string id PK
        string customerId FK
        string status
        string plan
        date startDate
        date endDate
        string billingCycle
    }
    
    SUBSCRIPTION_PAYMENT {
        string id PK
        string subscriptionId FK
        decimal amount
        datetime paymentDate
        string status
    }
```

## Event Flow and Message Schema

The following diagram shows a sample of our event structure and flow:

```mermaid
graph TD
    classDef publisher fill:#d1e0f0,stroke:#6c8ebf
    classDef event fill:#f8cecc,stroke:#b85450
    classDef consumer fill:#d5e8d4,stroke:#82b366

    OrdersService[Orders Service]:::publisher --> OrderConfirmed[OrderConfirmed Event]:::event
    
    subgraph OrderConfirmedSchema[ ]
        direction TB
        OrderConfirmedMessage["OrderConfirmed Schema
        {
          orderId: string,
          userId: string,
          orderItems: [
            {
              productId: string,
              quantity: number,
              unitPrice: number
            }
          ],
          totalAmount: number,
          timestamp: datetime
        }"]
    end
    
    OrderConfirmed --- OrderConfirmedSchema
    
    OrderConfirmed --> InventoryService[Inventory Service]:::consumer
    OrderConfirmed --> ShippingService[Shipping Service]:::consumer
    
    InventoryService --> InventoryAdjusted[InventoryAdjusted Event]:::event
    
    subgraph InventoryAdjustedSchema[ ]
        direction TB
        InventoryAdjustedMessage["InventoryAdjusted Schema
        {
          productId: string,
          warehouseId: string,
          quantityChanged: number,
          newQuantity: number,
          timestamp: datetime
        }"]
    end
    
    InventoryAdjusted --- InventoryAdjustedSchema
    
    InventoryAdjusted --> OrdersService:::consumer
    InventoryAdjusted --> NotificationService[Notification Service]:::consumer
```

## Conclusion

This document has provided an in-depth view of the data flows within the FlowMart e-commerce platform. By understanding these flows, developers and stakeholders can better comprehend how data moves through the system and how different components interact with each other.

For more details on specific architecture components, refer to:
- [High-Level System Overview](./01-high-level-system-overview.mdx)
- [Domain-Level Architecture](./02-domain-level-architecture.mdx)
- [Service-Level Architecture](./03-service-level-architecture.mdx) 
---
title: CI/CD and Deployment Strategy
summary: Architectural decision record for continuous integration, delivery and deployment approach for the FlowMart e-commerce platform
sidebar:
    label: CI/CD Strategy
    order: 2
---

# DRAFT - NOT YET APPROVED

:::warning
This is a draft ADR. It is not yet approved and should not be used as a reference.
:::

## ADR-008: CI/CD and Deployment Strategy for FlowMart E-commerce Platform

### Status

Draft (Last Updated: 2024-10-05)

### Context

As we transition to a microservices architecture with dozens of independently deployable services, our current deployment approach presents several challenges:

1. **Manual Deployment Processes**: Deployments are largely manual, requiring significant coordination and causing deployment anxiety.

2. **Environment Inconsistency**: Configuration differences between environments lead to environment-specific bugs and "works on my machine" issues.

3. **Long Lead Times**: The process from code commit to production deployment takes days or weeks due to manual testing and approval gates.

4. **Deployment Coupling**: Services must be deployed together in coordinated releases, slowing down the delivery of all features.

5. **Limited Testing Automation**: Insufficient automated testing leads to quality issues discovered late in the delivery process.

6. **Configuration Management**: Configuration is managed inconsistently across environments and services.

7. **Deployment Visibility**: Limited visibility into deployment status, history, and metrics.

8. **Rollback Challenges**: Rolling back problematic deployments is difficult and error-prone.

Our current approach does not support the rapid, independent delivery of microservices that is essential for our new architecture. We need a comprehensive CI/CD and deployment strategy that enables teams to deliver high-quality services with velocity and confidence.

### Decision

We will implement a **GitOps-based CI/CD and deployment strategy** with **continuous deployment to production** for our microservices architecture. Key aspects of this strategy include:

1. **Trunk-Based Development Model**:
   - Short-lived feature branches merged frequently to main/trunk
   - Feature toggles for in-progress work
   - Automated code quality checks and linting on pull requests
   - Main branch always deployable

2. **Continuous Integration Pipeline**:
   - Automated builds triggered on every commit
   - Comprehensive automated testing suite
   - Security scanning (SAST, SCA, secrets scanning)
   - Container image building and signing
   - Test environments provisioned on demand for PR validation

3. **GitOps Deployment Approach**:
   - Declarative infrastructure and application configuration in Git
   - ArgoCD as primary GitOps operator
   - Environment-specific configuration via Kustomize overlays
   - Git as single source of truth for deployed state
   - Automatic drift detection and remediation

4. **Deployment Progression Strategy**:
   - Automated deployments through dev and test environments
   - Production deployments with optional approval (human in the loop)
   - Environment promotion rather than rebuilding artifacts
   - Canary deployments for high-risk services
   - Blue/green deployments for critical components

5. **Configuration Management**:
   - Externalized configuration in Git repositories
   - Kubernetes ConfigMaps and Secrets for application configuration
   - Sealed Secrets for sensitive information
   - HashiCorp Vault for secrets rotation and dynamic credentials
   - Environment-specific configuration via layered overlays

6. **Deployment Safety Mechanisms**:
   - Progressive delivery with canary deployments
   - Automated pre-deployment validation
   - Automated post-deployment testing
   - Automated rollback on failure
   - Circuit breakers for dependent services

7. **Release Coordination**:
   - API versioning and backwards compatibility requirements
   - Service-level dependency management
   - Deployment sequencing for interdependent services
   - Deployment windows for critical services

8. **Deployment Metrics and Observability**:
   - Deployment frequency tracking
   - Change lead time measurement
   - Mean time to recovery monitoring
   - Change failure rate tracking
   - Deployment health dashboards

### Technology Stack

| Component | Primary Technology | Alternative/Backup | Purpose |
|-----------|-------------------|-------------------|---------|
| Source Control | GitHub | GitLab | Version control and collaboration |
| CI Pipeline | GitHub Actions | Jenkins | Build, test, and validation |
| Artifact Registry | AWS ECR | GitHub Packages | Container image storage |
| GitOps Operator | ArgoCD | Flux | Kubernetes-based deployment automation |
| Secrets Management | Sealed Secrets + Vault | AWS Secrets Manager | Secure configuration management |
| Deployment Orchestration | ArgoCD + Argo Rollouts | Spinnaker | Controlled deployment progression |
| Feature Flags | LaunchDarkly | Flagsmith | Runtime feature enablement/disablement |
| Testing Framework | Jest, Cypress, k6 | Various | Automated testing across layers |
| Deployment Monitoring | Prometheus + Grafana | Datadog | Deployment metrics and alerting |

### Consequences

#### Positive

1. **Accelerated Delivery**: Reduced lead time from commit to production deployment.

2. **Improved Quality**: Comprehensive automated testing and validation.

3. **Increased Deployment Frequency**: Teams can deploy independently at their own pace.

4. **Enhanced Reliability**: Consistent, repeatable deployment processes with automated rollbacks.

5. **Better Visibility**: Clear audit trail and status of all deployments.

6. **Reduced Coordination Overhead**: Less need for cross-team deployment coordination.

7. **Improved Developer Experience**: Self-service deployments with rapid feedback.

8. **Environment Consistency**: Reproducible environments with minimal drift.

#### Negative

1. **Learning Curve**: Teams need to adapt to new tools and processes.

2. **Initial Setup Complexity**: Significant effort to establish the complete CI/CD pipeline.

3. **Infrastructure Requirements**: Additional infrastructure to support the CI/CD toolchain.

4. **Potential Deployment Sprawl**: Multiple services deploying independently can create coordination challenges.

5. **Testing Complexity**: Comprehensive testing across distributed services is challenging.

6. **Feature Flag Management**: Complexity of managing feature flags across services.

7. **Observability Requirements**: Need for sophisticated monitoring to detect deployment issues.

### Mitigation Strategies

1. **Platform Team Support**:
   - Create a dedicated platform engineering team focused on CI/CD
   - Provide standardized pipeline templates and documentation
   - Enable self-service capabilities with guardrails

2. **Phased Implementation**:
   - Start with less critical services
   - Gradually increase automation and reduce manual gates
   - Measure and demonstrate improved outcomes

3. **Developer Enablement**:
   - Comprehensive documentation and examples
   - Regular training sessions and office hours
   - Inner-source model for pipeline improvements

4. **Testing Strategy**:
   - Standard test libraries and frameworks
   - Service virtualization for dependencies
   - Comprehensive end-to-end testing strategy

5. **Change Management**:
   - Clear communication about process changes
   - Regular retrospectives and continuous improvement
   - Celebrate success stories and share lessons learned

### Implementation Details

#### Phase 1: Foundation (Q4 2024)

1. Establish CI pipeline standardization
2. Implement container build and security scanning
3. Set up artifact repositories and image signing
4. Deploy ArgoCD and initial GitOps workflows
5. Implement trunk-based development practices

#### Phase 2: Advanced Delivery (Q1 2025)

1. Enable canary and blue/green deployments
2. Implement comprehensive automated testing
3. Set up feature flag management
4. Deploy secrets management solution
5. Create deployment metrics dashboards

#### Phase 3: Continuous Deployment (Q2 2025)

1. Implement continuous deployment to production
2. Enable automated rollbacks and circuit breakers
3. Set up deployment SLOs and monitoring
4. Implement sophisticated deployment strategies
5. Optimize deployment performance and efficiency

### Deployment Process Flow

The following outlines our target deployment process flow from code commit to production:

1. **Code Commit & PR**:
   - Developer creates branch and commits changes
   - Pull request created with automated linting and checks
   - CI pipeline validates build, tests, and security

2. **CI Verification**:
   - Automated unit and integration tests
   - Security scanning (SAST, SCA, container scanning)
   - Code quality metrics and coverage checks
   - On-demand test environment provisioning

3. **Artifact Creation**:
   - Container images built and tagged
   - Images signed and pushed to registry
   - Deployment manifests generated
   - Configuration updates prepared

4. **Development Deployment**:
   - Automatic deployment to development environment
   - Post-deployment testing and validation
   - Integration testing with other services
   - Performance and security validation

5. **Staging Deployment**:
   - Promotion of verified artifacts to staging
   - Environment-specific configuration applied
   - System-level testing and validation
   - Performance testing against production-like load

6. **Production Deployment**:
   - Optional approval gate for high-risk services
   - Canary or blue/green deployment strategy
   - Incremental traffic shifting
   - Health check verification at each step

7. **Post-Deployment Validation**:
   - Automated smoke tests
   - Synthetic transaction monitoring
   - Key metric monitoring and alerting
   - Automated rollback if metrics deviate

### Considered Alternatives

#### 1. Traditional Release-Based Deployment Model

**Pros**: Familiar approach, coordinated releases, comprehensive testing cycles  
**Cons**: Slow delivery, limited independence, large batch sizes increasing risk

This approach would not provide the delivery velocity required for our business needs and would limit the benefits of our microservices architecture.

#### 2. Pure Environment Promotion Model

**Pros**: Artifact consistency, simplified promotion process, reduced build time  
**Cons**: Limited environment-specific customization, potential configuration complexity

While we adopt aspects of this approach, we need the flexibility of environment-specific configuration that a pure promotion model limits.

#### 3. Central Deployment Team

**Pros**: Standardized processes, specialized expertise, controlled deployments  
**Cons**: Potential bottleneck, reduced team autonomy, slower feedback loops

This approach would create a deployment bottleneck and reduce the ownership and autonomy of our product teams.

#### 4. Fully Automated No-Approval Deployments

**Pros**: Maximum velocity, reduced human intervention, forced quality automation  
**Cons**: Increased risk for critical systems, cultural resistance, advanced testing requirements

While this is our long-term goal, we need to balance velocity with appropriate controls, especially for critical payment and order processing systems.

### References

1. Forsgren, N., Humble, J., & Kim, G. "Accelerate: The Science of Lean Software and DevOps" (IT Revolution Press)
2. Humble, J. & Farley, D. "Continuous Delivery" (Addison-Wesley)
3. [GitOps Working Group](https://github.com/gitops-working-group/gitops-working-group)
4. [Argo CD Documentation](https://argo-cd.readthedocs.io/)
5. [Kubernetes Deployment Strategies](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy)
6. [Trunk Based Development](https://trunkbaseddevelopment.com/)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-09-28 | 0.1 | Initial draft | Jason Miller |
| 2024-10-03 | 0.2 | Added implementation phases and deployment flow | Thomas Wong |
| 2024-10-05 | 0.3 | Incorporated feedback from DevOps and development teams | David Boyne |
| TBD | 1.0 | Pending approval | Architecture Board |

## Appendix A: CI/CD Pipeline Architecture

```mermaid
flowchart TB
    subgraph "Developer Workflow"
        dev[Developer]
        ide[IDE]
        local[Local Testing]
        
        dev --> ide
        ide --> local
    end
    
    subgraph "Source Control"
        branch[Feature Branch]
        pr[Pull Request]
        trunk[Main Branch]
        
        local --> branch
        branch --> pr
        pr --> trunk
    end
    
    subgraph "Continuous Integration"
        build[Build & Test]
        security[Security Scan]
        quality[Quality Gates]
        artifact[Create Artifacts]
        
        trunk --> build
        build --> security
        security --> quality
        quality --> artifact
    end
    
    subgraph "Artifact Management"
        registry[Container Registry]
        config[Config Repository]
        
        artifact --> registry
        artifact --> config
    end
    
    subgraph "GitOps Deployment"
        argo[ArgoCD]
        dev_env[Development]
        stage_env[Staging]
        prod_env[Production]
        
        config --> argo
        argo --> dev_env
        argo --> stage_env
        argo --> prod_env
    end
    
    subgraph "Deployment Strategies"
        canary[Canary]
        blue_green[Blue/Green]
        
        prod_env --> canary
        prod_env --> blue_green
    end
    
    subgraph "Observability"
        metrics[Deployment Metrics]
        alerts[Deployment Alerts]
        dash[Deployment Dashboard]
        
        canary --> metrics
        blue_green --> metrics
        metrics --> alerts
        metrics --> dash
    end
```

## Appendix B: Deployment Pipeline Flow

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Git as GitHub
    participant CI as CI Pipeline
    participant Reg as Container Registry
    participant Config as Config Repository
    participant ArgoCD as ArgoCD
    participant Env as Environments
    participant Monitor as Monitoring
    
    Dev->>Git: Commit Code
    Git->>CI: Trigger Pipeline
    
    CI->>CI: Build & Test
    CI->>CI: Security Scan
    CI->>CI: Quality Gates
    
    CI->>Reg: Push Image
    CI->>Config: Update Manifests
    
    Config->>ArgoCD: Detected Changes
    ArgoCD->>Env: Deploy to Dev
    
    ArgoCD->>Env: Post-Deployment Tests
    Env->>Monitor: Collect Metrics
    
    alt Tests Pass
        ArgoCD->>Env: Deploy to Staging
        Env->>Monitor: Collect Metrics
        
        alt Staging Healthy
            ArgoCD->>Env: Deploy Canary to Production
            Env->>Monitor: Collect Metrics
            
            alt Canary Healthy
                ArgoCD->>Env: Complete Production Rollout
            else Canary Unhealthy
                ArgoCD->>Env: Rollback Canary
            end
        else Staging Unhealthy
            ArgoCD->>Env: Rollback Staging
        end
    else Tests Fail
        ArgoCD->>Env: Rollback Dev
    end
    
    Monitor->>Dev: Deployment Status & Metrics
```

## Appendix C: Environment Configuration Strategy

```mermaid
flowchart LR
    subgraph "Git Repositories"
        app[Application Code]
        infra[Infrastructure Code]
        config[Configuration]
    end
    
    subgraph "Configuration Layers"
        base[Base Configuration]
        env[Environment Overlays]
        service[Service-Specific Config]
    end
    
    subgraph "Secret Management"
        sealed[Sealed Secrets]
        vault[HashiCorp Vault]
        esm[External Secrets Manager]
    end
    
    subgraph "Kubernetes Resources"
        cm[ConfigMaps]
        secrets[Secrets]
        pods[Deployments]
    end
    
    app --> build{Build Process}
    infra --> terraform{Terraform}
    
    config --> base
    base --> kustomize{Kustomize}
    env --> kustomize
    service --> kustomize
    
    sealed --> kustomize
    vault --> esm
    esm --> secrets
    
    kustomize --> cm
    kustomize --> secrets
    
    build --> pods
    terraform --> platform[Platform Resources]
    cm --> pods
    secrets --> pods
``` 
---
title: API Management and Governance
summary: Architectural decision record for our API management and governance approach for the FlowMart e-commerce platform
sidebar:
    label: API Management
    order: 3
---

# DRAFT - NOT YET APPROVED

## ADR-009: API Management and Governance Strategy

### Status

Draft (Last Updated: 2024-10-07)

### Context

As we expand our microservices architecture for the FlowMart e-commerce platform, we need a comprehensive approach to API management and governance. We are facing several challenges with our current approach to APIs:

1. **Proliferation of APIs**: With our transition to microservices, we anticipate having 50+ internal APIs and multiple external-facing APIs within the next year.

2. **Inconsistent Design Patterns**: Teams are implementing APIs with inconsistent patterns, naming conventions, error handling, and response formats.

3. **Documentation Gaps**: API documentation is inconsistent, often outdated, and frequently exists only in code comments or team wikis.

4. **Discoverability Issues**: Developers struggle to find existing APIs, leading to duplication of functionality.

5. **Security Concerns**: APIs lack consistent security controls, authentication mechanisms, and authorization models.

6. **Version Management**: No clear strategy for versioning APIs, handling breaking changes, or maintaining backward compatibility.

7. **Performance Visibility**: Limited visibility into API performance, usage patterns, and availability.

8. **Cross-Cutting Concerns**: Features like rate limiting, caching, and observability are implemented inconsistently across services.

9. **Developer Experience**: Onboarding to consume APIs is complex and time-consuming, both for internal teams and external partners.

FlowMart is transitioning from a monolithic architecture to microservices, with a growing ecosystem of APIs. We need a cohesive approach to ensure these APIs are secure, discoverable, consistent, and manageable at scale.

### Decision

We will implement a comprehensive **API Management and Governance Strategy** with the following key components:

1. **API Gateway Architecture**:
   - Implement Kong as our primary API gateway for both internal and external APIs
   - Deploy separate gateway instances for external, internal, and partner traffic
   - Utilize a mesh pattern for internal service-to-service communication
   - Implement a Backend for Frontend (BFF) pattern for frontend-specific aggregation

2. **API Design Standards**:
   - Adopt OpenAPI (formerly Swagger) as our API specification standard
   - Establish comprehensive REST API design guidelines
   - Implement a design-first approach for all new APIs
   - Define standard patterns for resource naming, query parameters, pagination, filtering, and error responses
   - Standardize on JSON:API specification for response formatting

3. **API Lifecycle Management**:
   - Define clear stages: Design → Review → Development → Testing → Deployment → Deprecation → Retirement
   - Implement automated API contract testing in CI/CD pipelines
   - Require specification update for any API changes
   - Establish deprecation and sunsetting policies with clear timelines

4. **API Governance Model**:
   - Create an API Guild with representatives from each team
   - Establish an API review process for all new APIs and significant changes
   - Implement automated linting and compliance checking against standards
   - Define metrics for API quality and compliance
   - Regular review of API portfolio for duplication and consolidation opportunities

5. **API Documentation and Discovery**:
   - Deploy a central API developer portal using Backstage
   - Ensure all APIs have OpenAPI specifications
   - Implement automated documentation generation from OpenAPI specs
   - Create a searchable API catalog with metadata, ownership, and usage examples
   - Develop interactive API playground environments

6. **API Security Framework**:
   - Standardize on OAuth 2.0 and OpenID Connect for authentication
   - Implement role-based and attribute-based access control
   - Deploy centralized API key management
   - Establish security scanning and penetration testing for APIs
   - Implement API request validation based on schemas

7. **API Monitoring and Analytics**:
   - Deploy comprehensive API metrics collection
   - Create dashboards for performance, availability, and usage
   - Implement distributed tracing for end-to-end request flows
   - Set up alerting on API SLOs and error rates
   - Establish usage analytics for product and developer experience improvement

8. **API Versioning Strategy**:
   - Adopt semantic versioning (major.minor.patch) for all APIs
   - Support at least one previous major version for backward compatibility
   - Use URI versioning for major versions (/v1/, /v2/)
   - Implement feature flags for progressive rollout of API changes
   - Establish clear communication channels for API changes

### Technology Stack

| Component | Primary Technology | Alternative/Backup | Purpose |
|-----------|-------------------|-------------------|---------|
| API Gateway | Kong | Apigee, Amazon API Gateway | Traffic management, routing, policies |
| API Specification | OpenAPI 3.0 | AsyncAPI (for event-driven) | API contract and documentation |
| Developer Portal | Backstage | SwaggerHub, Readme.io | Discovery, documentation, onboarding |
| Identity Provider | Auth0 | Keycloak, AWS Cognito | Authentication and authorization |
| API Testing | Postman + Newman | SoapUI, Karate | Automated API testing |
| API Monitoring | Datadog | New Relic, Prometheus | Observability and analytics |
| Contract Testing | Pact | Spring Cloud Contract | Consumer-driven contract testing |
| GraphQL Federation | Apollo Federation | Netflix DGS | GraphQL implementation |
| API Design Tooling | Stoplight Studio | SwaggerHub, Insomnia | Design-first workflow |

### Consequences

#### Positive

1. **Improved Developer Experience**: Consistent, well-documented APIs accelerate development.

2. **Enhanced Security**: Standardized authentication and authorization patterns.

3. **Better Visibility**: Comprehensive monitoring and analytics of API usage and performance.

4. **Reduced Duplication**: Central catalog prevents redundant API implementations.

5. **Faster Integration**: Partners and internal teams can onboard more quickly.

6. **Higher Quality**: Standardized design patterns and automated testing improve quality.

7. **Future-Proofing**: Versioning strategy ensures backward compatibility.

8. **Operational Efficiency**: Centralized management of cross-cutting concerns.

#### Negative

1. **Initial Overhead**: Additional processes and governance may slow initial development.

2. **Learning Curve**: Teams need to adapt to new standards and practices.

3. **Migration Effort**: Existing APIs need to be refactored to meet new standards.

4. **Tooling Investment**: Significant investment in API management infrastructure.

5. **Governance Challenges**: Maintaining compliance across teams requires persistent effort.

6. **Potential Bottlenecks**: API review processes could become a bottleneck if not well-designed.

7. **Operational Complexity**: Additional infrastructure components to maintain.

### Mitigation Strategies

1. **Phased Implementation**:
   - Start with high-priority, externally facing APIs
   - Gradually implement standards for internal APIs
   - Provide flexible transition periods for existing APIs

2. **Developer Enablement**:
   - Create comprehensive training materials and workshops
   - Develop starter templates and code generators
   - Provide API design consultation services
   - Create self-service tools for standards compliance

3. **Governance Optimization**:
   - Implement automated compliance checking
   - Create lightweight review processes for low-risk changes
   - Empower teams with self-service validation tools
   - Focus governance on enablement rather than control

4. **Migration Support**:
   - Develop clear migration guidelines and timelines
   - Provide tooling to assist with API migrations
   - Allow grandfathering of legacy APIs with clear deprecation plans
   - Prioritize high-value, high-impact APIs for migration

5. **Platform Team Support**:
   - Create a dedicated API platform team
   - Offer consulting services to teams implementing or consuming APIs
   - Develop reusable components for common API patterns
   - Continuously evolve standards based on feedback

### Implementation Details

#### Phase 1: Foundation (Q4 2024)

1. Establish API design standards and guidelines
2. Deploy API gateway for external-facing services
3. Implement initial developer portal
4. Create API governance process and guild
5. Define API security standards

#### Phase 2: Expansion (Q1 2025)

1. Extend API gateway to internal services
2. Implement comprehensive monitoring and analytics
3. Deploy automated compliance checking
4. Develop API versioning framework
5. Create self-service API documentation tooling

#### Phase 3: Optimization (Q2 2025)

1. Implement advanced BFF patterns
2. Deploy GraphQL federation for complex client needs
3. Establish API performance optimization framework
4. Create advanced analytics and business insights
5. Develop partner API developer experiences

### API Design Principles

Our API design will adhere to the following principles:

1. **Resource-Oriented Design**: Model APIs around business resources rather than operations.

2. **Consistency**: APIs should behave consistently across the platform.

3. **Least Privilege**: APIs should request only the permissions they need.

4. **Robustness**: APIs should handle error cases gracefully and provide clear error messages.

5. **Forward Compatibility**: Design APIs to be extended without breaking existing clients.

6. **Discoverability**: APIs should be self-documenting and easily discoverable.

7. **Performance**: APIs should be designed with performance considerations in mind.

8. **Security by Design**: Security should be considered at every stage of the API lifecycle.

### API Governance Model

Our API governance model follows these principles:

1. **Federated Ownership**: Teams own their APIs but follow central standards.

2. **Standards over Rules**: Prefer guidance and patterns over strict enforcement.

3. **Automated Compliance**: Automate standards checking wherever possible.

4. **Continuous Improvement**: Regularly review and refine standards based on feedback.

5. **Value-Driven**: Focus governance efforts on high-value, high-risk APIs.

6. **Developer Experience**: Prioritize developer experience in governance decisions.

7. **Transparency**: Make governance processes and decisions transparent to all teams.

### Considered Alternatives

#### 1. Decentralized API Management

**Pros**: Maximum team autonomy, reduced coordination overhead  
**Cons**: Inconsistent developer experience, potential security gaps, duplicated effort

This approach would give teams complete freedom but would result in an inconsistent and potentially insecure API landscape that would be difficult to navigate and maintain.

#### 2. Centralized API Development Team

**Pros**: Maximum consistency, specialized expertise, controlled quality  
**Cons**: Development bottleneck, reduced team ownership, slower delivery

While this would ensure consistency, it would create bottlenecks and reduce the autonomy and ownership of our product teams, contradicting our microservices philosophy.

#### 3. Multiple API Gateways by Domain

**Pros**: Domain isolation, reduced blast radius, team autonomy  
**Cons**: Management complexity, potential inconsistencies, higher operational overhead

This approach offers benefits for large organizations but introduces unnecessary complexity for our current scale. We may revisit this approach as we grow.

#### 4. GraphQL-First Approach

**Pros**: Flexible client queries, reduced over-fetching, schema registry  
**Cons**: Learning curve, performance concerns for some use cases, security complexity

GraphQL offers benefits for certain use cases, but we believe a REST-first approach with GraphQL for specific complex client needs provides a better balance for our organization.

### References

1. "Web API Design: The Missing Link" by API Academy
2. "REST API Design Rulebook" by Mark Masse
3. [Google API Design Guide](https://cloud.google.com/apis/design)
4. [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md)
5. [JSON:API Specification](https://jsonapi.org/)
6. [API Governance: What, Why, and How](https://swagger.io/resources/articles/api-governance-what-why-how/)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-09-30 | 0.1 | Initial draft | Sarah Johnson |
| 2024-10-04 | 0.2 | Added governance model and phasing | Michael Chen |
| 2024-10-07 | 0.3 | Incorporated feedback from API Guild | David Boyne |
| TBD | 1.0 | Pending approval | Architecture Board |

## Appendix A: API Governance Process

```mermaid
flowchart TB
    subgraph "API Lifecycle"
        design[Design Phase]
        review[Review Phase]
        develop[Development Phase]
        test[Testing Phase]
        deploy[Deployment Phase]
        monitor[Monitoring Phase]
        deprecate[Deprecation Phase]
        
        design --> review
        review --> develop
        develop --> test
        test --> deploy
        deploy --> monitor
        monitor --> deprecate
    end
    
    subgraph "Governance Touchpoints"
        standards[Standards & Guidelines]
        templates[API Templates]
        linting[Automated Linting]
        reviews[Peer Reviews]
        testing[Contract Testing]
        security[Security Scanning]
        analytics[Usage Analytics]
        
        standards --> design
        templates --> design
        linting --> review
        reviews --> review
        testing --> test
        security --> test
        analytics --> monitor
    end
    
    subgraph "Key Roles"
        guild[API Guild]
        owners[API Owners]
        platform[Platform Team]
        consumers[API Consumers]
        
        guild --> standards
        owners --> design
        platform --> templates
        consumers --> analytics
    end
    
    subgraph "Artifacts"
        spec[OpenAPI Specification]
        docs[Documentation]
        portal[Developer Portal]
        metrics[Metrics Dashboard]
        
        design --> spec
        spec --> docs
        docs --> portal
        monitor --> metrics
    end
```

## Appendix B: API Management Architecture

```mermaid
flowchart TB
    subgraph "Clients"
        web[Web Clients]
        mobile[Mobile Clients]
        partners[Partner Systems]
        internal[Internal Services]
    end
    
    subgraph "API Gateways"
        public[Public API Gateway]
        partner[Partner API Gateway]
        internal_gw[Internal API Gateway]
    end
    
    subgraph "BFF Layer"
        web_bff[Web BFF]
        mobile_bff[Mobile BFF]
    end
    
    subgraph "API Services"
        products[Product APIs]
        orders[Order APIs]
        customers[Customer APIs]
        payments[Payment APIs]
        inventory[Inventory APIs]
    end
    
    subgraph "Cross-Cutting Concerns"
        auth[Authentication]
        rate[Rate Limiting]
        cache[Caching]
        logging[Logging]
        analytics[Analytics]
    end
    
    web --> web_bff
    mobile --> mobile_bff
    partners --> partner
    internal --> internal_gw
    
    web_bff --> public
    mobile_bff --> public
    
    public --> products
    public --> orders
    public --> customers
    partner --> products
    partner --> orders
    internal_gw --> products
    internal_gw --> orders
    internal_gw --> customers
    internal_gw --> payments
    internal_gw --> inventory
    
    auth --> public
    auth --> partner
    auth --> internal_gw
    rate --> public
    rate --> partner
    cache --> public
    cache --> partner
    cache --> internal_gw
    logging --> public
    logging --> partner
    logging --> internal_gw
    analytics --> public
    analytics --> partner
    analytics --> internal_gw
```

## Appendix C: API Developer Portal Architecture

```mermaid
flowchart LR
    subgraph "API Developer Portal"
        catalog[API Catalog]
        docs[API Documentation]
        playground[API Playground]
        analytics[Usage Analytics]
        sandbox[Sandbox Environment]
        support[Developer Support]
    end
    
    subgraph "API Sources"
        openapi[OpenAPI Specifications]
        asyncapi[AsyncAPI Specifications]
        graphql[GraphQL Schemas]
        code[Source Code]
    end
    
    subgraph "Developer Tools"
        cli[CLI Tools]
        sdks[Client SDKs]
        ci[CI/CD Integration]
        codegen[Code Generators]
    end
    
    subgraph "Governance Tools"
        standards[Standards Library]
        linting[Linting Tools]
        testing[Testing Framework]
        workflow[Approval Workflows]
    end
    
    openapi --> catalog
    asyncapi --> catalog
    graphql --> catalog
    code --> docs
    
    catalog --> playground
    catalog --> analytics
    catalog --> sdks
    catalog --> codegen
    
    playground --> sandbox
    sandbox --> support
    
    standards --> linting
    linting --> ci
    testing --> ci
    workflow --> ci
``` 
---
title: Service Mesh Adoption
summary: Architectural decision record for adopting a service mesh for TechNova's cloud platform
sidebar:
    label: Service Mesh Adoption
    order: 1
---

## ADR-2023-05: Service Mesh Adoption for TechNova Cloud Platform

### Status

Approved (2023-08-15)

### Context

TechNova's cloud platform has grown to include over 75 microservices developed and maintained by 12 different teams. As our platform has scaled, we've encountered several challenges:

1. **Service-to-Service Communication Complexity**: Managing service-to-service communication has become increasingly complex, with inconsistent implementation of patterns like circuit breaking, retries, and timeout handling.

2. **Security Concerns**: Service-to-service authentication and authorization is implemented inconsistently, creating potential security vulnerabilities.

3. **Observability Gaps**: Tracking request flows across services is difficult, making troubleshooting and performance optimization challenging.

4. **Traffic Management Challenges**: We lack sophisticated traffic control capabilities such as traffic splitting, canary deployments, and blue/green releases.

5. **Certificate Management**: Managing and rotating TLS certificates for service-to-service communication has become an operational burden.

6. **Network Policy Enforcement**: Network access controls are difficult to implement and maintain consistently across services.

Our engineering teams currently spend approximately 25% of their development effort on these cross-cutting concerns, diverting resources from building business functionality.

### Decision

We will adopt **Istio** as our service mesh solution for the TechNova Cloud Platform. Specifically:

1. **Sidecar Deployment Model**: We will deploy Istio using the sidecar proxy architecture to minimize disruption to existing services.

2. **Gradual Implementation**: We will introduce the service mesh incrementally, starting with non-critical services and gradually expanding to include all services.

3. **Standardized Patterns**: We will establish company-wide standards for:
   - Circuit breaking configurations
   - Retry policies
   - Timeout configurations
   - Mutual TLS implementation
   - Traffic management patterns
   - Observability integrations

4. **Platform Team Ownership**: A dedicated platform team will own the service mesh infrastructure, including:
   - Istio version management and upgrades
   - Performance monitoring and optimization
   - Security policy definition and enforcement
   - Training and documentation

5. **Integration with Existing Tooling**:
   - Prometheus and Grafana for metrics and dashboarding
   - Jaeger for distributed tracing
   - Kiali for service mesh visualization
   - Cert-Manager for certificate management

6. **Control Plane Configuration**: We will deploy Istio with:
   - High availability control plane (3 replicas)
   - Split along environment boundaries (separate control planes for production and non-production)
   - Regular automated backups of control plane configuration

### Consequences

#### Positive

1. **Simplified Service Code**: Application developers can focus on business logic rather than communication concerns.

2. **Enhanced Security**: Consistent mTLS implementation will improve our security posture.

3. **Improved Observability**: End-to-end request tracing and detailed service metrics will enhance troubleshooting.

4. **Advanced Traffic Management**: Capabilities for canary deployments and traffic steering will reduce deployment risk.

5. **Certificate Automation**: Automated certificate management will reduce operational overhead.

6. **Standardized Networking Policies**: Centralized network policy enforcement will improve security and compliance.

#### Negative

1. **Increased Complexity**: Service mesh adds architectural complexity and new failure modes.

2. **Resource Overhead**: Sidecar proxies consume additional CPU and memory resources (~10-15% based on POC testing).

3. **Learning Curve**: Teams will need to learn new concepts, tooling, and debugging approaches.

4. **Deployment Changes**: CI/CD pipelines will need updates to accommodate service mesh configuration.

5. **Potential Performance Impact**: Additional network hops may increase latency (observed ~5-10ms per hop in testing).

6. **Operational Changes**: Incident response and troubleshooting procedures will need updates.

### Mitigation Strategies

1. **Comprehensive Education Program**:
   - Create internal training curriculum for all engineering teams
   - Schedule hands-on workshops focusing on practical use cases
   - Develop troubleshooting playbooks and runbooks

2. **Gradual Rollout Plan**:
   - Phase 1 (Q3 2023): Deploy to non-critical services and gather metrics
   - Phase 2 (Q4 2023): Expand to backend services with low customer impact
   - Phase 3 (Q1 2024): Roll out to critical customer-facing services

3. **Resource Optimization**:
   - Tune proxy resource requests based on actual usage patterns
   - Implement horizontal pod autoscaling for proxies
   - Monitor and optimize control plane resource utilization

4. **Performance Monitoring**:
   - Establish baseline performance metrics before service mesh adoption
   - Implement detailed performance monitoring dashboards
   - Set alerting on latency increases beyond acceptable thresholds

5. **Escape Hatch Mechanisms**:
   - Document procedures for temporarily bypassing the service mesh if issues arise
   - Create fast rollback capabilities for service mesh configurations

### Implementation Details

#### Phase 1: Foundation (Q3 2023)

1. Deploy Istio control plane in non-production environments
2. Implement mTLS for a subset of non-critical services
3. Set up integration with observability stack
4. Develop initial training materials and documentation
5. Create standard Istio configuration templates

#### Phase 2: Expansion (Q4 2023)

1. Deploy production control plane
2. Expand to backend services
3. Implement traffic management capabilities
4. Develop automated testing for service mesh configurations
5. Integrate service mesh configurations into CI/CD pipelines

#### Phase 3: Completion (Q1 2024)

1. Roll out to remaining services
2. Implement advanced security policies
3. Complete comprehensive monitoring and alerting
4. Finalize operational procedures and runbooks
5. Document lessons learned and best practices

### Considered Alternatives

#### 1. Linkerd

**Pros**: Lighter weight, simpler operations, lower resource overhead  
**Cons**: Fewer features, smaller community, less integration with enterprise tools

While Linkerd offers a more lightweight approach, we found that its limited feature set would not address all our requirements, particularly around sophisticated traffic management and extensibility.

#### 2. AWS App Mesh

**Pros**: Native AWS integration, managed control plane, simplified operations  
**Cons**: AWS-specific, limited feature set compared to Istio, less community support

AWS App Mesh would align well with our AWS infrastructure but lacks some advanced features we require and would limit our multi-cloud flexibility.

#### 3. Custom Solution with Envoy

**Pros**: Tailored to our exact needs, potentially lower overhead  
**Cons**: High development and maintenance cost, lack of community support, reinventing the wheel

Building our own solution would require significant engineering resources and ongoing maintenance, which would outweigh the benefits of customization.

#### 4. No Service Mesh (Status Quo)

**Pros**: No additional complexity or overhead, familiar patterns  
**Cons**: Continued inconsistency across services, growing technical debt, security risks

Maintaining the status quo would fail to address our current challenges and would further increase technical debt as our platform continues to grow.

### References

1. [Istio Documentation](https://istio.io/latest/docs/)
2. "The Service Mesh Era" - Cloud Native Computing Foundation Whitepaper
3. Internal POC Report: "Service Mesh Performance and Compatibility Testing" (TechNova Engineering, June 2023)
4. [CNCF Service Mesh Comparison](https://servicemesh.es/)
5. [Envoy Proxy Documentation](https://www.envoyproxy.io/docs/envoy/latest/)
6. "Production Istio" - O'Reilly Media, 2022

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2023-05-10 | 0.1 | Initial draft | Alexander Chen, Principal Architect |
| 2023-06-22 | 0.2 | Updated based on POC results | Sophia Rodriguez, Platform Engineering |
| 2023-07-15 | 0.3 | Added phased implementation plan | Marcus Johnson, Engineering Director |
| 2023-08-15 | 1.0 | Approved by Architecture Review Board | TechNova ARB |

## Appendix A: Service Mesh Architecture

```mermaid
flowchart TB
    subgraph "Control Plane"
        istiod[Istiod]
        config[Configuration API]
        certs[Certificate Authority]
    end
    
    subgraph "Ingress/Egress"
        ingress[Ingress Gateway]
        egress[Egress Gateway]
    end
    
    subgraph "Observability"
        prom[Prometheus]
        grafana[Grafana]
        jaeger[Jaeger]
        kiali[Kiali]
    end
    
    subgraph "Kubernetes Cluster"
        subgraph "Service A"
            svcA[Service A]
            proxyA[Envoy Proxy]
        end
        
        subgraph "Service B"
            svcB[Service B]
            proxyB[Envoy Proxy]
        end
        
        subgraph "Service C"
            svcC[Service C]
            proxyC[Envoy Proxy]
        end
    end
    
    client[Client] --> ingress
    ingress --> proxyA
    proxyA --> svcA
    proxyA --> proxyB
    proxyB --> svcB
    proxyB --> proxyC
    proxyC --> svcC
    proxyC --> egress
    egress --> external[External Services]
    
    istiod --> proxyA
    istiod --> proxyB
    istiod --> proxyC
    istiod --> ingress
    istiod --> egress
    
    config --> istiod
    certs --> istiod
    
    proxyA --> prom
    proxyB --> prom
    proxyC --> prom
    prom --> grafana
    proxyA --> jaeger
    proxyB --> jaeger
    proxyC --> jaeger
    prom --> kiali
    jaeger --> kiali
    config --> kiali
```

## Appendix B: Service Mesh Implementation Timeline

```mermaid
gantt
    title TechNova Service Mesh Implementation
    dateFormat  YYYY-MM-DD
    
    section Planning
    Initial Research           :done, 2023-03-01, 2023-04-15
    Proof of Concept           :done, 2023-04-16, 2023-06-15
    Architecture Decision      :done, 2023-06-16, 2023-08-15
    
    section Phase 1: Foundation
    Control Plane Setup        :active, 2023-08-16, 2023-09-15
    Observability Integration  :active, 2023-09-01, 2023-09-30
    Initial Service Onboarding :2023-09-15, 2023-10-15
    Training & Documentation   :2023-09-01, 2023-10-31
    
    section Phase 2: Expansion
    Production Control Plane   :2023-11-01, 2023-11-30
    Backend Service Onboarding :2023-11-15, 2024-01-15
    CI/CD Integration          :2023-12-01, 2024-01-31
    Advanced Traffic Management:2024-01-01, 2024-02-15
    
    section Phase 3: Completion
    Remaining Service Onboarding :2024-02-01, 2024-03-31
    Security Policy Implementation:2024-02-15, 2024-03-31
    Finalize Operations Procedures:2024-03-01, 2024-04-15
    Performance Optimization     :2024-03-15, 2024-04-30
    Project Completion          :milestone, 2024-04-30
```

## Appendix C: Estimated Resource Requirements

| Component | CPU Request | Memory Request | Replicas | Environment | Notes |
|-----------|-------------|---------------|----------|-------------|-------|
| Istiod | 500m | 2Gi | 3 | Production | HA configuration |
| Istiod | 500m | 2Gi | 1 | Non-Production | Single replica |
| Ingress Gateway | 500m | 1Gi | 3 | Production | External traffic entry |
| Ingress Gateway | 200m | 512Mi | 1 | Non-Production | Development testing |
| Egress Gateway | 500m | 1Gi | 2 | Production | External service access |
| Envoy Proxy | 100m | 256Mi | 1 per pod | All | Sidecar containers |
| Prometheus | 1000m | 8Gi | 2 | Production | Metric collection |
| Grafana | 200m | 1Gi | 2 | Production | Dashboarding |
| Jaeger | 500m | 4Gi | 2 | Production | Distributed tracing |
| Kiali | 200m | 1Gi | 2 | Production | Mesh visualization |

*Note: These values are initial estimates based on our proof of concept and may be adjusted based on actual usage patterns.* 
---
title: Data Platform Strategy
summary: Architectural decision record for adopting a modern data platform at FinSecure
sidebar:
    label: Data Platform Strategy
    order: 2
---

## ADR-2023-12: Modern Data Platform Strategy for FinSecure

### Status

Approved (2023-12-18)

### Context

FinSecure is experiencing significant challenges with our current data architecture:

1. **Data Silos**: Customer, transaction, and risk data are siloed across multiple legacy systems with inconsistent data models.

2. **Limited Analytics Capabilities**: Rigid data warehousing solutions limit our ability to perform advanced analytics and machine learning.

3. **Scalability Constraints**: Current data processing infrastructure is struggling to handle increasing data volumes (now exceeding 5TB daily).

4. **Compliance Complexity**: Meeting GDPR, CCPA, and financial regulatory requirements across fragmented data systems is increasingly difficult.

5. **Slow Time-to-Insight**: Business teams wait 2-3 weeks for new analytics dashboards or data models to be developed.

6. **Technical Debt**: Legacy ETL processes are complex, brittle, and expensive to maintain.

7. **Limited Real-time Capabilities**: Current architecture is primarily batch-oriented with limited ability to process streaming data for fraud detection and real-time decisioning.

8. **Data Quality Issues**: Inconsistent data quality across systems impacts business decisions and customer experience.

These challenges are limiting our ability to leverage data as a strategic asset and inhibiting our digital transformation initiatives aimed at enhancing customer experiences and operational efficiency.

### Decision

We will implement a **modern, cloud-based data platform** with a **lakehouse architecture**. Key components include:

1. **Data Lake Foundation**:
   - Azure Data Lake Storage Gen2 as the foundation for our data lake
   - Databricks Delta Lake for ACID transactions and data reliability
   - Structured organization with bronze (raw), silver (refined), and gold (business) layers

2. **Data Ingestion and Processing**:
   - Azure Data Factory for orchestration and batch data movement
   - Kafka and Azure Event Hubs for real-time data ingestion
   - Databricks for large-scale data processing
   - Stream processing with Spark Structured Streaming

3. **Semantic Layer and Data Serving**:
   - Databricks SQL Warehouses for analytics workloads
   - Azure Synapse Analytics for enterprise data warehousing needs
   - Power BI as primary business intelligence tool
   - REST APIs for serving data to applications

4. **Data Governance and Security**:
   - Azure Purview for data catalog and lineage
   - Column-level encryption for sensitive data
   - Role-based access control aligned with data classification
   - Automated data retention and purging based on policies

5. **Machine Learning Platform**:
   - MLflow for experiment tracking and model registry
   - Databricks ML for model development and deployment
   - Model monitoring and retraining pipelines
   - Feature store for reusable feature engineering

6. **DataOps and Automation**:
   - Infrastructure as Code using Terraform
   - CI/CD pipelines for data pipelines and transformations
   - Automated testing for data quality and pipeline integrity
   - Comprehensive monitoring and alerting

### Platform Architecture by Domain

| Domain | Data Types | Primary Tools | Access Patterns | Special Requirements |
|--------|------------|--------------|-----------------|----------------------|
| Customer 360 | Customer profiles, interactions, preferences | Delta Lake, Databricks SQL | Batch analytics, Real-time lookups | GDPR compliance, Entity resolution |
| Transaction Processing | Payment transactions, transfers, statements | Kafka, Delta Lake, Azure Synapse | Real-time streaming, Batch reporting | PCI-DSS compliance, 7-year retention |
| Risk Management | Credit scores, market data, exposure calculations | Databricks, Delta Lake, ML models | Batch processing, Model inference | Auditability, Model governance |
| Fraud Detection | Transaction patterns, behavioral signals | Kafka, Spark Streaming, ML models | Real-time streaming, Low-latency scoring | Sub-second latency, High availability |
| Regulatory Reporting | Aggregated financial data, compliance metrics | Azure Synapse, Power BI | Scheduled batch, Ad-hoc analysis | Immutability, Approval workflows |
| Marketing Analytics | Campaign data, customer segments, attribution | Databricks, Delta Lake, Power BI | Interactive queries, ML-based segmentation | Identity resolution, Attribution models |

### Consequences

#### Positive

1. **Unified Data Access**: Single platform for accessing enterprise data with consistent governance.

2. **Enhanced Analytical Capabilities**: Support for advanced analytics, machine learning, and AI initiatives.

3. **Improved Scalability**: Cloud-native architecture can scale to handle growing data volumes.

4. **Reduced Time-to-Insight**: Self-service capabilities and streamlined data pipelines reduce time to deliver insights.

5. **Better Data Governance**: Centralized data catalog, lineage tracking, and security controls.

6. **Real-time Capabilities**: Support for both batch and real-time processing using the same platform.

7. **Cost Optimization**: Pay-for-use cloud model with ability to scale resources as needed.

8. **Regulatory Compliance**: Improved ability to implement and demonstrate regulatory compliance.

#### Negative

1. **Implementation Complexity**: Significant effort required to migrate from legacy systems.

2. **Skills Gap**: New technologies require reskilling of existing teams.

3. **Initial Cost Increase**: Short-term investment in new technology and parallel running of systems.

4. **Data Migration Challenges**: Data quality and mapping issues during migration.

5. **Operational Changes**: New operational procedures and support models needed.

6. **Integration Complexity**: Connecting legacy systems to new platform requires careful planning.

7. **Organization Change Management**: New workflows and responsibilities across business and technical teams.

### Mitigation Strategies

1. **Phased Implementation Approach**:
   - Start with highest-value, least-critical data domains
   - Implement foundational capabilities before complex use cases
   - Run legacy and new systems in parallel during transition
   - Create clear success criteria for each phase

2. **Talent and Skill Development**:
   - Develop comprehensive training program for existing staff
   - Strategic hiring for key specialized roles
   - Partner with platform vendors for enablement
   - Create centers of excellence for key technologies

3. **Modern Data Governance**:
   - Establish data governance council with cross-functional representation
   - Define clear data ownership and stewardship model
   - Implement automated data quality monitoring
   - Create comprehensive data classification framework

4. **Financial Management**:
   - Detailed cloud cost monitoring and optimization
   - Business-aligned chargeback model
   - Clear ROI tracking for data initiatives
   - Regular cost optimization reviews

5. **Change Management Program**:
   - Executive sponsorship and visible leadership
   - Regular communication and success stories
   - Early involvement of business stakeholders
   - Incentives aligned with adoption goals

### Implementation Details

#### Phase 1: Foundation (Q1-Q2 2024)

1. Establish cloud environment and core infrastructure
2. Implement data lake foundation with initial data domains
3. Deploy data catalog and basic governance tools
4. Migrate first non-critical data workloads
5. Establish DataOps practices and pipelines

#### Phase 2: Expansion (Q3-Q4 2024)

1. Migrate core analytical workloads to the platform
2. Implement real-time data processing capabilities
3. Deploy self-service analytics for business users
4. Enhance data quality frameworks and monitoring
5. Develop initial ML use cases on the platform

#### Phase 3: Advanced Capabilities (Q1-Q2 2025)

1. Full enterprise adoption across all data domains
2. Advanced ML capabilities and feature store
3. Comprehensive data governance implementation
4. Legacy system decommissioning
5. Advanced real-time analytics and decisioning

### Considered Alternatives

#### 1. Modernize Existing Data Warehouse

**Pros**: Lower initial disruption, familiar technology, focused scope  
**Cons**: Limited flexibility, higher long-term costs, limited real-time capabilities

This approach would not address our fundamental needs for real-time processing, advanced analytics, and managing unstructured data.

#### 2. Traditional Data Lake Architecture

**Pros**: Lower cost storage, support for varied data types, scalability  
**Cons**: Complexity in ensuring data quality, limited transactional support, governance challenges

A traditional data lake without the lakehouse capabilities would create significant challenges for data reliability, performance, and governance.

#### 3. Multiple Purpose-Built Systems

**Pros**: Optimized solutions for specific use cases, potentially best-in-class capabilities  
**Cons**: Increased integration complexity, data duplication, inconsistent governance

This approach would perpetuate our data silo issues and create ongoing integration and consistency challenges.

#### 4. Maintain and Incrementally Improve Current Systems

**Pros**: Minimal disruption, lower initial investment, familiar technology  
**Cons**: Perpetuates technical debt, limited capability improvement, increasing maintenance costs

This would fail to address our fundamental challenges and put us at a competitive disadvantage as data volumes and complexity increase.

### References

1. "Designing Data-Intensive Applications" by Martin Kleppmann
2. [Databricks Lakehouse Platform Documentation](https://docs.databricks.com/lakehouse/index.html)
3. [Azure Data Factory Documentation](https://docs.microsoft.com/en-us/azure/data-factory/)
4. "Data Mesh: Delivering Data-Driven Value at Scale" by Zhamak Dehghani
5. FinSecure Internal Report: "Data Platform Requirements Analysis" (October 2023)
6. [DAMA Data Management Body of Knowledge](https://www.dama.org/cpages/body-of-knowledge)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2023-10-15 | 0.1 | Initial draft | Jennifer Wu, Chief Data Officer |
| 2023-11-08 | 0.2 | Updated based on technical review | Raj Patel, Data Engineering Lead |
| 2023-12-02 | 0.3 | Added implementation phases and cost estimates | Michael Torres, Enterprise Architect |
| 2023-12-18 | 1.0 | Approved by Executive Technology Committee | FinSecure ETC |

## Appendix A: Data Platform Architecture

```mermaid
flowchart TB
    subgraph "Data Sources"
        core[Core Banking Systems]
        crm[CRM Systems]
        channels[Digital Channels]
        market[Market Data Feeds]
        apps[Applications]
        ext[External Partners]
    end
    
    subgraph "Data Ingestion"
        batch[Batch Processing]
        stream[Stream Processing]
        cdc[Change Data Capture]
        api[API Integration]
    end
    
    subgraph "Data Storage"
        subgraph "Data Lake"
            bronze[Bronze Layer<br>Raw Data]
            silver[Silver Layer<br>Cleansed & Conformed]
            gold[Gold Layer<br>Business Aggregates]
        end
        
        dw[Enterprise Data Warehouse]
        fs[Feature Store]
    end
    
    subgraph "Processing & Analytics"
        etl[ETL/ELT Processes]
        bi[Business Intelligence]
        ml[Machine Learning]
        ad[Advanced Analytics]
        realtime[Real-time Analytics]
    end
    
    subgraph "Data Consumption"
        reports[Reports & Dashboards]
        apps2[Applications]
        apis[APIs & Services]
        exports[Exports & Feeds]
        ml_svc[ML Services]
    end
    
    subgraph "Governance & Operations"
        catalog[Data Catalog]
        quality[Data Quality]
        lineage[Data Lineage]
        security[Security & Privacy]
        lifecycle[Data Lifecycle]
    end
    
    core --> batch
    crm --> batch
    channels --> stream
    market --> stream
    apps --> cdc
    ext --> api
    
    batch --> bronze
    stream --> bronze
    cdc --> bronze
    api --> bronze
    
    bronze --> etl
    etl --> silver
    silver --> etl
    etl --> gold
    etl --> dw
    gold --> dw
    silver --> fs
    
    dw --> bi
    gold --> bi
    silver --> ml
    gold --> ml
    fs --> ml
    silver --> ad
    bronze --> realtime
    silver --> realtime
    
    bi --> reports
    ml --> ml_svc
    ad --> apis
    realtime --> apps2
    dw --> exports
    
    catalog --> bronze
    catalog --> silver
    catalog --> gold
    catalog --> dw
    
    quality --> silver
    lineage --> etl
    security --> dw
    lifecycle --> bronze
```

## Appendix B: Data Platform Implementation Timeline

```mermaid
gantt
    title FinSecure Data Platform Implementation
    dateFormat  YYYY-MM-DD
    
    section Strategy & Planning
    Requirements Analysis       :done, 2023-08-01, 2023-10-15
    Vendor Evaluation           :done, 2023-09-15, 2023-11-15
    Architecture Design         :done, 2023-10-01, 2023-12-15
    
    section Phase 1: Foundation
    Core Infrastructure Setup   :active, 2024-01-15, 2024-02-28
    Data Lake Implementation    :2024-02-01, 2024-03-31
    Governance Framework        :2024-02-15, 2024-04-15
    Initial Data Migration      :2024-03-01, 2024-05-31
    DataOps Implementation      :2024-04-01, 2024-06-30
    
    section Phase 2: Expansion
    Advanced Analytics Platform :2024-07-01, 2024-09-30
    Streaming Data Processing   :2024-08-01, 2024-10-31
    Self-service Analytics      :2024-09-01, 2024-11-30
    Data Quality Framework      :2024-10-01, 2024-12-15
    ML Platform Deployment      :2024-10-15, 2025-01-31
    
    section Phase 3: Advanced
    Enterprise-wide Adoption    :2025-02-01, 2025-04-30
    Legacy System Decomm        :2025-03-01, 2025-06-30
    Advanced Governance         :2025-04-01, 2025-06-30
    Real-time Decisioning       :2025-05-01, 2025-07-31
    Program Completion          :milestone, 2025-07-31
```

## Appendix C: Target State Data Flow - Customer 360 Example

```mermaid
sequenceDiagram
    participant Source as Source Systems
    participant Ingest as Data Ingestion
    participant Bronze as Bronze Layer
    participant Process as Data Processing
    participant Silver as Silver Layer
    participant Gold as Gold Layer
    participant Consume as Data Consumption
    
    Source->>Ingest: Customer Data<br>(Core Banking, CRM, Channels)
    Ingest->>Bronze: Raw Data Ingestion<br>(Batch & Streaming)
    
    Bronze->>Process: Validation & Cleansing
    Process->>Process: Data Quality Checks
    Process->>Process: Deduplication
    Process->>Process: Standardization
    Process->>Silver: Refined Customer Records
    
    Silver->>Process: Entity Resolution
    Process->>Process: Customer Attribute Generation
    Process->>Process: Relationship Mapping
    Process->>Process: History Processing
    Process->>Gold: Unified Customer Profiles
    
    Gold->>Consume: Customer 360 Views
    Gold->>Consume: Segmentation Models
    Gold->>Consume: Marketing Analytics
    Gold->>Consume: Risk Assessment
    Gold->>Consume: Real-time Personalization
    
    Note over Bronze,Gold: Data Governance<br>- Lineage Tracking<br>- Privacy Controls<br>- Data Classification<br>- Quality Monitoring
```

## Appendix D: Key Performance Indicators

| KPI | Current State | Target (2025) | Measurement Method |
|-----|---------------|---------------|-------------------|
| Data Integration Cycle Time | 7-14 days | &lt;24 hours | Average time from source change to data availability |
| Self-service BI Adoption | 15% of business users | &gt;60% of business users | Monthly active users in self-service tools |
| Data Quality Score | ~75% | &gt;95% | Composite score from automated quality checks |
| Cost per TB of Analytics Storage | $2,500/TB | &lt;$500/TB | Total cost of ownership / storage volume |
| Time to New Analytics | 2-3 weeks | &lt;3 days | Time from request to dashboard availability |
| Data Platform Availability | 99.5% | 99.95% | Measured service uptime |
| Regulatory Report Production Time | 10-15 days | 1-2 days | Time to produce monthly regulatory reports |
| Real-time Decision Latency | Not available | &lt;250ms | Response time for real-time decision APIs |
| ML Model Deployment Time | 4-6 weeks | &lt;1 week | Time from model approval to production deployment |
| Data Engineer Productivity | ~30% on new features | &gt;70% on new features | Time allocation analysis |

*Note: Metrics will be tracked quarterly and reported to the Data Governance Council.* 
---
title: API Gateway Pattern Adoption
summary: Architectural decision record for implementing an API Gateway for the FlowMart e-commerce platform
sidebar:
    label: API Gateway Pattern
    order: 1
---

## ADR-001: Adoption of API Gateway Pattern for FlowMart E-commerce Platform

### Status

Approved (2024-06-10)

### Context

As we migrate to a microservices-based architecture for our e-commerce platform, we face several challenges in managing API endpoints:

1. **API Proliferation**: Each microservice exposes its own APIs, leading to a large number of endpoints that clients need to interact with.
2. **Cross-cutting Concerns**: Common functionality like authentication, logging, and rate limiting needs to be implemented consistently across all services.
3. **Client Complexity**: Mobile apps, web frontends, and third-party integrations would need to understand the topology of our microservices ecosystem.
4. **Protocol Diversity**: Some internal services may use protocols (gRPC, AMQP) that aren't suitable for direct client consumption.
5. **Network Performance**: Multiple direct client-to-service calls increase network overhead, especially on mobile networks.
6. **Security Exposure**: Direct exposure of microservices increases the attack surface of our platform.

We need a solution that simplifies our API landscape while maintaining the benefits of our microservices architecture.

### Decision

We will implement an **API Gateway Pattern** as the primary entry point for all client applications interacting with the FlowMart e-commerce platform. Specifically:

1. **Gateway Implementation**: We will use **Kong API Gateway** as our primary implementation due to its robust plugin ecosystem, performance characteristics, and open-source foundation.

2. **Gateway Responsibilities**:
   - **Request Routing**: Directing requests to appropriate backend services
   - **Authentication & Authorization**: Validating user identity and permissions
   - **Rate Limiting**: Protecting services from excessive load
   - **Request/Response Transformation**: Adapting data formats between clients and services
   - **Caching**: Reducing backend load for frequently requested data
   - **Logging & Monitoring**: Centralized request tracking
   - **Circuit Breaking**: Preventing cascading failures
   - **Protocol Translation**: Supporting REST, GraphQL, and gRPC as needed

3. **Gateway Topology**:
   - **Edge Gateway**: A public-facing gateway for all external clients
   - **Internal Gateway**: For service-to-service communication within our private network

4. **API Composition**: The gateway will aggregate responses from multiple services when needed to reduce client-side complexity.

5. **Backend-for-Frontend (BFF) Pattern**: We will implement specific gateway configurations for different client platforms (web, mobile iOS, mobile Android) to optimize payloads and calls.

6. **API Versioning**: The gateway will support multiple API versions to enable graceful evolution of our services.

### Consequences

#### Positive

1. **Simplified Client Development**: Clients only need to know about a single entry point rather than multiple service endpoints.

2. **Consistent Security Enforcement**: Authentication, authorization, and other security controls can be implemented uniformly.

3. **Operational Visibility**: Centralized logging and monitoring of all API traffic.

4. **Performance Optimization**: Opportunity for response caching, request collapsing, and other optimizations.

5. **Flexible Evolution**: Backend services can be refactored, replaced, or decomposed without changing client implementations.

6. **Traffic Control**: Ability to throttle, prioritize, or redirect traffic based on various conditions.

#### Negative

1. **Potential Single Point of Failure**: The gateway becomes critical infrastructure that must be highly available.

2. **Increased Latency**: Adding another network hop introduces some additional latency.

3. **Gateway Complexity**: The gateway configuration grows in complexity as the number of services increases.

4. **Operational Overhead**: Additional infrastructure to monitor, maintain, and scale.

5. **Deployment Coupling**: Gateway configuration changes may need coordination with service deployments.

6. **Performance Bottleneck Risk**: Without proper scaling, the gateway could become a bottleneck under high load.

### Mitigation Strategies

1. **High Availability**: Deploy the API Gateway in a redundant, auto-scaling configuration across multiple availability zones.

2. **Performance Optimization**: Implement efficient caching strategies and regular performance testing.

3. **Circuit Breakers**: Implement circuit breakers to prevent cascading failures if backend services are unavailable.

4. **Automated Configuration**: Use infrastructure as code to manage gateway configuration, with automated testing.

5. **API Governance**: Establish clear ownership and review processes for gateway configuration changes.

6. **Observability**: Implement comprehensive monitoring and alerting specifically for the gateway.

### Implementation Details

#### Phase 1: Core Infrastructure (Q2 2024)

1. Deploy Kong API Gateway in development and staging environments
2. Implement basic routing for 2-3 core services
3. Set up authentication and authorization
4. Establish monitoring and logging
5. Create CI/CD pipeline for gateway configuration

#### Phase 2: Feature Expansion (Q3 2024)

1. Migrate all existing APIs to the gateway
2. Implement rate limiting and circuit breaking
3. Add response caching for appropriate endpoints
4. Develop BFF configurations for web and mobile
5. Implement comprehensive end-to-end testing

#### Phase 3: Advanced Capabilities (Q4 2024)

1. Implement GraphQL support for specific use cases
2. Add advanced analytics and API usage dashboards
3. Integrate with service mesh for internal service communication
4. Implement advanced security features (WAF, etc.)
5. Optimize for global performance

### Considered Alternatives

#### 1. Direct Client-to-Microservice Communication

**Pros**: Simplicity, no additional network hop, no central bottleneck  
**Cons**: Client complexity, inconsistent policy enforcement, security challenges

This approach would expose our internal service architecture directly to clients, creating significant complexity and security concerns.

#### 2. Service Mesh Only (no API Gateway)

**Pros**: Great for service-to-service communication, built-in resilience  
**Cons**: Not designed for edge traffic, less focus on client-specific concerns

While we plan to use a service mesh for internal communication, it doesn't address the client-facing concerns that an API Gateway solves.

#### 3. Bespoke API Gateway

**Pros**: Custom-built for our exact needs, no license costs  
**Cons**: Development and maintenance overhead, feature gaps, opportunity cost

Building our own gateway would divert significant resources from our core business and likely result in a less robust solution than established products.

#### 4. Alternative Gateway Products (Apigee, AWS API Gateway)

**Pros**: Managed services (reduced operational burden), rich feature sets  
**Cons**: Higher costs, potential vendor lock-in, less customization

These were viable alternatives, but Kong offered the best balance of features, flexibility, and cost for our requirements.

### References

1. Richardson, Chris. "Pattern: API Gateway / Backends for Frontends." [Microservices.io](https://microservices.io/patterns/apigateway.html)
2. Fowler, Martin. "BFF: Backend for Frontend." [martinfowler.com](https://martinfowler.com/articles/gateway-pattern.html)
3. [Kong API Gateway Documentation](https://docs.konghq.com/)
4. Newman, Sam. Building Microservices (O'Reilly)
5. API Gateway Pattern, Microsoft Azure Architecture Center. [Microsoft Docs](https://docs.microsoft.com/en-us/azure/architecture/microservices/design/gateway)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-05-15 | 0.1 | Initial draft | James Wilson |
| 2024-05-25 | 0.2 | Added implementation phases and alternatives | Sarah Chen |
| 2024-06-05 | 0.3 | Incorporated feedback from architecture review | David Boyne |
| 2024-06-10 | 1.0 | Approved by Architecture Board | Architecture Board |

## Appendix A: API Gateway Architecture

```mermaid
flowchart TB
    subgraph "External Clients"
        web[Web Application]
        mobile[Mobile Apps]
        partners[Partner Systems]
    end

    subgraph "API Layer"
        gateway[Kong API Gateway]
        style gateway fill:#b9e0a5,stroke:#333,stroke-width:2px
        auth[Auth Service]
        gateway <--> auth
    end

    subgraph "Backend Services"
        products[Product Service]
        orders[Order Service]
        inventory[Inventory Service]
        pricing[Pricing Service]
        users[User Service]
        recommendations[Recommendation Service]
    end

    web --> gateway
    mobile --> gateway
    partners --> gateway
    
    gateway --> products
    gateway --> orders
    gateway --> inventory
    gateway --> pricing
    gateway --> users
    gateway --> recommendations
```

## Appendix B: Gateway Policy Application Flow

```mermaid
sequenceDiagram
    participant Client
    participant Gateway as API Gateway
    participant Auth as Authentication Service
    participant Service as Backend Service
    
    Client->>Gateway: API Request
    
    Gateway->>Gateway: Apply Rate Limiting
    Note over Gateway: Check quota and rate limits
    
    Gateway->>Auth: Validate Token
    Auth-->>Gateway: Token Valid/Invalid
    
    alt Token Valid
        Gateway->>Gateway: Apply Request Transformation
        Gateway->>Service: Forward Request
        Service-->>Gateway: Service Response
        Gateway->>Gateway: Apply Response Transformation
        Gateway->>Gateway: Apply Caching Headers
        Gateway-->>Client: Transformed Response
    else Token Invalid
        Gateway-->>Client: 401 Unauthorized
    end
```

## Appendix C: Gateway Feature Rollout

| Feature | Target Date | Priority | Dependencies | Owner |
|---------|-------------|----------|--------------|-------|
| Basic Routing | Q2 2024 | Critical | Gateway Infrastructure | DevOps Team |
| Authentication | Q2 2024 | Critical | Auth Service | Security Team |
| Monitoring & Logging | Q2 2024 | High | Observability Platform | DevOps Team |
| Rate Limiting | Q3 2024 | High | None | Platform Team |
| Request/Response Transformation | Q3 2024 | Medium | API Standards | API Team |
| Circuit Breaking | Q3 2024 | Medium | Service Health Metrics | Platform Team |
| Caching | Q3 2024 | Medium | Cache Invalidation Strategy | Performance Team |
| GraphQL Support | Q4 2024 | Low | GraphQL Schema | API Team |
| Advanced Analytics | Q4 2024 | Low | Data Platform | Data Team | 
---
title: Event-driven architecture adoption
summary: A document that captures important architectural decisions and their context
sidebar:
    label: EDA Adoption
    order: 2
---

## ADR-001: Adoption of Event-Driven Architecture for FlowMart E-commerce Platform

### Status

Approved (2024-07-15)

### Context

FlowMart is building a new e-commerce platform to replace our legacy monolithic application. The current system faces several challenges:

1. **Scalability Issues**: During peak shopping periods (e.g., Black Friday, holiday season), the system struggles to handle increased traffic, resulting in degraded performance and occasional outages.
2. **Maintenance Complexity**: Adding new features or modifying existing ones requires extensive regression testing and often leads to unexpected side effects.
3. **Technology Constraints**: The monolithic architecture limits our ability to adopt new technologies or update components independently.
4. **Data Consistency**: Ensuring data consistency across different parts of the application has become increasingly difficult.
5. **Team Independence**: Multiple development teams working on different aspects of the application frequently block each other.

We need an architecture that addresses these challenges while enabling rapid innovation and scaling to meet our projected growth over the next 3-5 years.

### Decision

We will adopt an **Event-Driven Architecture (EDA)** using a microservices approach for the new FlowMart e-commerce platform. Specifically:

1. **Domain-Driven Design (DDD)**: We will organize our services around business domains (Orders, Inventory, Payment, Shipping, etc.) with clearly defined bounded contexts.

2. **Event Sourcing**: Critical business transactions will be stored as a sequence of immutable events that can be used to reconstruct the system state at any point in time.

3. **Command Query Responsibility Segregation (CQRS)**: We will separate read and write operations where appropriate to optimize for different performance and scaling requirements.

4. **Apache Kafka** will serve as our primary event streaming platform for asynchronous communication between services.

5. **Eventual Consistency Model**: We acknowledge that the system will prioritize availability and partition tolerance over immediate consistency (following the CAP theorem), with mechanisms to ensure eventual consistency.

6. **Service Autonomy**: Each service will:
   - Have its own database
   - Be independently deployable
   - Have well-defined APIs and event contracts
   - Be responsible for publishing domain events when state changes occur

7. **Choreography Over Orchestration**: Services will primarily react to events rather than being orchestrated by a central coordinator, though we will use orchestration for complex workflows when necessary.

### Consequences

#### Positive

1. **Improved Scalability**: Individual services can scale independently based on demand, allowing us to allocate resources more efficiently.

2. **Better Fault Isolation**: Failures in one service are less likely to cascade across the entire system, improving overall reliability.

3. **Technology Flexibility**: Teams can choose the most appropriate technologies for their specific domains, allowing for incremental adoption of new technologies.

4. **Team Autonomy**: Domain-aligned teams can develop, test, and deploy their services independently, reducing cross-team dependencies.

5. **Enhanced Auditability**: Event sourcing provides a complete audit trail of all system changes, which is valuable for debugging, compliance, and business analytics.

6. **Improved Extensibility**: New capabilities can be added by creating new consumers of existing events without modifying the original producers.

#### Negative

1. **Increased Complexity**: Distributed systems are inherently more complex to develop, test, debug, and operate compared to monolithic applications.

2. **Learning Curve**: The team will need to learn new patterns, technologies, and operational practices, which may slow initial development.

3. **Eventual Consistency Challenges**: Business operations and UI design must account for data that might not be immediately consistent across services.

4. **Operational Overhead**: Managing multiple services, event streams, and databases requires more sophisticated monitoring, deployment, and operational tools.

5. **Transaction Management**: Ensuring transactional integrity across service boundaries requires careful design and implementation of compensation patterns.

6. **Testing Complexity**: End-to-end testing becomes more challenging, requiring new testing strategies and tools.

### Compliance Requirements

Our implementation must adhere to the following requirements:

1. **Data Privacy**: Personal customer data must be handled in compliance with GDPR, CCPA, and other applicable regulations.

2. **PCI DSS**: Payment processing components must comply with Payment Card Industry Data Security Standards.

3. **Audit Trail**: All critical business transactions must be traceable and auditable for a minimum of 7 years.

4. **Security**: Authentication, authorization, and data encryption standards must be consistently applied across all services.

### Implementation Details

#### Phase 1: Core Domain Decomposition (Q3 2024)

1. Identify and define core domain boundaries
2. Establish event schemas and contracts
3. Implement Kafka infrastructure and operational tooling
4. Migrate the first domain (Orders) to the new architecture
5. Set up CI/CD pipelines and monitoring

#### Phase 2: Domain Expansion (Q4 2024)

1. Migrate Inventory and Payment domains
2. Implement event sourcing for critical domains
3. Develop read models for reporting and analytics
4. Establish cross-domain consistency patterns

#### Phase 3: Legacy Decommissioning (Q1-Q2 2025)

1. Migrate remaining domains
2. Implement advanced monitoring and alerting
3. Gradually decommission legacy system components
4. Complete performance tuning and optimization

### Considered Alternatives

#### 1. Modular Monolith

**Pros**: Simpler development model, transactional integrity, easier testing  
**Cons**: Limited independent scaling, technology constraints, deployment coupling

This approach would address some concerns (maintainability, modularity) but would not solve our scalability and team independence challenges.

#### 2. Microservices with REST-only Communication

**Pros**: Well-understood patterns, synchronous communication simplicity  
**Cons**: Tighter coupling, limited resilience, cascading failures

This approach would improve modularity but would not adequately address resilience and scalability concerns.

#### 3. Serverless Architecture

**Pros**: Minimal infrastructure management, high elasticity, pay-per-use model  
**Cons**: Vendor lock-in, cold start latency, limited control over infrastructure

While appealing for certain scenarios, this approach would not provide the control and predictability needed for our core business functions.

### References

1. Building Event-Driven Microservices (Adam Bellemare, O'Reilly)
2. Domain-Driven Design (Eric Evans, Addison-Wesley)
3. Enterprise Integration Patterns (Gregor Hohpe, Bobby Woolf, Addison-Wesley)
4. [Kafka Documentation](https://kafka.apache.org/documentation/)
5. [CQRS Pattern](https://martinfowler.com/bliki/CQRS.html) (Martin Fowler)
6. [Event Sourcing Pattern](https://martinfowler.com/eaaDev/EventSourcing.html) (Martin Fowler)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-06-22 | 0.1 | Initial draft | David Boyne |
| 2024-06-30 | 0.2 | Incorporate feedback from architecture review | Amy Smith |
| 2024-07-10 | 0.3 | Added implementation phasing and compliance requirements | Kiran Patel |
| 2024-07-15 | 1.0 | Approved by Architecture Board | Architecture Board |

## Appendix A: High-Level Architecture Diagram

```mermaid
flowchart TB
    subgraph "API Gateway"
        gw[API Gateway]
    end

    subgraph "Customer Domain"
        cust[Customer Service]
        auth[Authentication Service]
    end

    subgraph "Order Domain"
        order[Order Service]
        orderhist[Order History Service]
    end

    subgraph "Inventory Domain"
        inv[Inventory Service]
        stock[Stock Management]
    end

    subgraph "Payment Domain"
        payment[Payment Service]
        refund[Refund Service]
    end

    subgraph "Shipping Domain"
        ship[Shipping Service]
        track[Tracking Service]
    end

    subgraph "Event Backbone"
        kafka[Apache Kafka]
    end

    gw --> order
    gw --> cust
    gw --> auth
    gw --> inv
    gw --> payment
    gw --> ship
    gw --> track

    order --> kafka
    cust --> kafka
    inv --> kafka
    payment --> kafka
    ship --> kafka
    track --> kafka

    kafka --> orderhist
    kafka --> stock
    kafka --> refund
```

## Appendix B: Key Event Flows

### Order Placement Flow

```mermaid
sequenceDiagram
    participant C as Customer
    participant OS as Order Service
    participant IS as Inventory Service
    participant PS as Payment Service
    participant SS as Shipping Service
    participant NS as Notification Service

    C->>OS: Place Order
    OS->>IS: Check Inventory
    IS-->>OS: Inventory Available
    OS->>PS: Process Payment
    PS-->>OS: Payment Approved
    OS->>OS: Create Order
    OS->>+kafka: Publish OrderCreated
    kafka->>IS: OrderCreated
    IS->>IS: Reserve Inventory
    IS->>kafka: Publish InventoryReserved
    kafka->>SS: InventoryReserved
    SS->>SS: Create Shipment
    SS->>kafka: Publish ShipmentCreated
    kafka->>NS: ShipmentCreated
    NS->>C: Send Order Confirmation
```

### Out-of-Stock Handling Flow

```mermaid
sequenceDiagram
    participant IS as Inventory Service
    participant K as Kafka
    participant NS as Notification Service
    participant RS as Replenishment Service
    participant OS as Order Service
    participant CS as Customer

    IS->>IS: Stock level check
    IS->>+K: Publish OutOfStockEvent
    K->>NS: OutOfStockEvent
    K->>RS: OutOfStockEvent
    K->>OS: OutOfStockEvent
    
    NS->>CS: Send out-of-stock notification
    RS->>RS: Create replenishment order
    RS->>+K: Publish ReplenishmentOrderedEvent
    OS->>OS: Update product availability
    OS->>CS: Show "Notify when available" option

    note over RS,IS: After stock is replenished
    RS->>IS: Restock inventory
    IS->>+K: Publish InventoryRestockedEvent
    K->>NS: InventoryRestockedEvent
    K->>OS: InventoryRestockedEvent
    
    NS->>CS: Send back-in-stock notification
    OS->>OS: Update product availability
```

## Appendix C: Service Ownership

| Domain | Service | Team |
|--------|---------|------|
| Customer | Customer Service | Full Stack Team |
| Customer | Authentication Service | Security Team |
| Order | Order Service | Order Management Team |
| Order | Order History Service | Order Management Team |
| Inventory | Inventory Service | Full Stack Team |
| Inventory | Stock Management | Full Stack Team |
| Payment | Payment Service | Payment Team |
| Payment | Refund Service | Payment Team |
| Shipping | Shipping Service | Logistics Team |
| Shipping | Tracking Service | Logistics Team |


---
title: Authentication and Authorization Strategy
summary: Architectural decision record for implementing authentication and authorization for the FlowMart e-commerce platform
sidebar:
    label: Auth Strategy
    order: 3
---

## ADR-003: Authentication and Authorization Strategy for FlowMart E-commerce Platform

### Status

Approved (2024-08-01)

### Context

As we move to a microservices architecture for our e-commerce platform, we need a robust, scalable, and secure approach to authentication and authorization. The current monolithic application uses a custom auth solution with session-based authentication, which presents several challenges in a distributed environment:

1. **Session Stickiness**: Requires load balancer configuration to route users to the same server.
2. **Scalability Constraints**: Session state storage becomes challenging as we scale horizontally.
3. **Cross-Service Authentication**: No standardized way for services to validate user identity and permissions.
4. **Partner and Third-Party Integration**: Difficult to securely expose APIs to external systems.
5. **Multiple Authentication Factors**: Need to support various authentication methods (passwords, social logins, biometrics).
6. **Varying Authorization Requirements**: Different resources require different permission models.
7. **Compliance Requirements**: GDPR, PCI-DSS, and industry regulations impose strict requirements on handling authentication data.

We need an authentication and authorization strategy that works effectively in a distributed microservices environment while maintaining high security standards.

### Decision

We will implement a token-based authentication and authorization strategy using **OAuth 2.0** and **OpenID Connect (OIDC)** standards with **Auth0** as our identity provider. Specifically:

1. **Authentication Pattern**:
   - **JWT (JSON Web Tokens)** for representing claims between parties
   - **Stateless authentication** where possible to improve scalability
   - **OAuth 2.0 Authorization Code Flow with PKCE** for web applications
   - **OAuth 2.0 Resource Owner Password Grant** (limited to legacy/internal applications)
   - **OAuth 2.0 Client Credentials Grant** for service-to-service communication

2. **Authorization Pattern**:
   - **Role-Based Access Control (RBAC)** as the primary mechanism for coarse-grained permissions
   - **Attribute-Based Access Control (ABAC)** for fine-grained access decisions
   - **Policy Enforcement Points (PEP)** implemented at the API Gateway level for common policies
   - **Service-level authorization** for domain-specific access control

3. **User Management**:
   - Centralized user directory in Auth0
   - Self-service user registration and profile management
   - Admin-managed role assignments and permissions
   - Progressive profiling to collect user information gradually

4. **Multi-Factor Authentication (MFA)**:
   - Required for administrative accounts and sensitive operations
   - Optional but encouraged for standard user accounts
   - Risk-based authentication triggers (unusual location, device, behavior)

5. **Service-to-Service Authentication**:
   - Mutual TLS (mTLS) for service mesh communication
   - Client credentials OAuth flow with short-lived tokens for cross-boundary requests

6. **API Security**:
   - Token validation at the API Gateway
   - Scoped access tokens for limiting API permissions
   - Token introspection for high-security operations

### Consequences

#### Positive

1. **Improved Scalability**: Stateless authentication allows for better horizontal scaling without session replication.

2. **Standardized Security**: Using established security protocols (OAuth 2.0/OIDC) provides well-tested security patterns.

3. **Reduced Development Burden**: Auth0 handles many security concerns (token issuance, validation, revocation, etc.).

4. **Flexible Integration**: Easier to integrate with third-party systems and identity providers.

5. **Centralized Policy Management**: Authorization policies can be managed centrally and applied consistently.

6. **Enhanced User Experience**: Support for modern authentication patterns (social login, passwordless, etc.).

7. **Compliance Support**: Built-in features for consent management, audit logging, and other compliance requirements.

#### Negative

1. **Increased Complexity**: More moving parts in the authentication flow compared to simple session-based auth.

2. **Token Management Overhead**: Need to handle token lifecycle, refresh, and invalidation carefully.

3. **External Dependency**: Reliance on Auth0 as a critical service and potential single point of failure.

4. **Performance Considerations**: Token validation and policy evaluation add some latency to requests.

5. **Cost**: Subscription fees for Auth0 based on active users and features used.

6. **Learning Curve**: Team needs to understand OAuth 2.0 flows and token-based authentication patterns.

### Mitigation Strategies

1. **Caching and Performance Optimization**:
   - Implement efficient token validation with local caching
   - Use token introspection only when necessary
   - Optimize policy evaluation paths

2. **Resilience Planning**:
   - Implement graceful degradation if Auth0 is temporarily unavailable
   - Consider a multi-region Auth0 deployment for critical workloads
   - Regular disaster recovery testing

3. **Security Hardening**:
   - Set appropriate token lifetimes (shorter for sensitive operations)
   - Implement proper token storage in clients (secure cookies, encrypted storage)
   - Regular security reviews and penetration testing

4. **Developer Experience**:
   - Create SDKs and libraries to abstract authentication complexity
   - Comprehensive documentation and training
   - Authentication dev sandbox environment

### Implementation Details

#### Phase 1: Core Authentication Infrastructure (Q3 2024)

1. Set up Auth0 tenant and configure core settings
2. Implement login, registration, and password reset flows
3. Migrate existing user accounts (passwords securely hashed)
4. Integrate with API Gateway for token validation
5. Set up basic roles and permissions

#### Phase 2: Advanced Authorization (Q4 2024)

1. Implement fine-grained ABAC policies
2. Develop centralized policy management tools
3. Set up delegated administration capabilities
4. Implement audit logging and monitoring
5. Configure MFA for administrative accounts

#### Phase 3: Partner and Integration Capabilities (Q1 2025)

1. Implement client credentials for service-to-service
2. Set up partner authentication portal
3. Configure rate limiting and throttling
4. Implement token exchange capabilities
5. Set up public developer documentation

### Considered Alternatives

#### 1. Custom Authentication Solution

**Pros**: Complete control, no external dependencies, potentially lower direct costs  
**Cons**: Development time, security risks, maintenance burden, limited features

Building our own solution would require significant security expertise and ongoing maintenance, with higher risk of vulnerabilities.

#### 2. Keycloak (Open Source Identity Provider)

**Pros**: Open source, flexible, no subscription fees, self-hosted control  
**Cons**: Operational overhead, scalability challenges, fewer integrations

Keycloak would reduce subscription costs but increase operational complexity and require more internal expertise.

#### 3. AWS Cognito

**Pros**: Tight AWS integration, managed service, good scalability  
**Cons**: Less flexible than Auth0, fewer enterprise features, AWS lock-in

Cognito would be suitable if we were fully committed to AWS, but we needed more flexibility for our multi-cloud strategy.

#### 4. Session-Based Authentication with Distributed Cache

**Pros**: Simpler architecture, familiar pattern, less paradigm shift  
**Cons**: Scalability challenges, higher operational complexity, less standardized

This would maintain our current approach but with scalability improvements, though it wouldn't address many of our requirements.

### Standards Compliance

Our implementation will comply with the following standards and regulations:

1. **OAuth 2.0 (RFC 6749)**: The authorization framework
2. **OpenID Connect 1.0**: Identity layer on top of OAuth 2.0
3. **JWT (RFC 7519)**: Compact token format
4. **GDPR**: For EU user data protection
5. **PCI-DSS**: For payment-related authentication
6. **NIST 800-63B**: Digital Identity Guidelines

### References

1. [OAuth 2.0 RFC 6749](https://tools.ietf.org/html/rfc6749)
2. [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
3. [Auth0 Architecture Scenarios](https://auth0.com/docs/architecture-scenarios)
4. [JWT Introduction](https://jwt.io/introduction)
5. Nate Barbettini, "OAuth 2.0 and OpenID Connect in Plain English" ([YouTube](https://www.youtube.com/watch?v=996OiexHze0))
6. "API Security in Action" by Neil Madden (Manning Publications)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-07-01 | 0.1 | Initial draft | Elena Rodriguez |
| 2024-07-15 | 0.2 | Added implementation phases and alternatives | Michael Chang |
| 2024-07-25 | 0.3 | Incorporated security team feedback | Sarah Chen |
| 2024-08-01 | 1.0 | Approved by Architecture and Security Boards | Architecture Board |

## Appendix A: Authentication Flows

```mermaid
sequenceDiagram
    participant User
    participant Client as Web/Mobile App
    participant API as API Gateway
    participant Auth0 as Auth0
    participant Service as Microservice

    %% Login Flow
    User->>Client: Initiates Login
    Client->>Auth0: Redirect to Auth0 (/authorize)
    Auth0->>User: Present Login UI
    User->>Auth0: Enter Credentials
    opt MFA Triggered
        Auth0->>User: Request Second Factor
        User->>Auth0: Provide Second Factor
    end
    Auth0->>Client: Authorization Code
    Client->>Auth0: Exchange Code for Tokens
    Auth0->>Client: Access Token, ID Token, Refresh Token
    
    %% API Access Flow
    Client->>API: Request with Access Token
    API->>API: Validate Token
    API->>Service: Forward Request + Claims
    Service->>Service: Check Authorization
    Service->>API: Response
    API->>Client: Response
    
    %% Token Refresh
    Note over Client: When Access Token Expires
    Client->>Auth0: Request with Refresh Token
    Auth0->>Client: New Access Token
```

## Appendix B: Authorization Model

```mermaid
flowchart TB
    subgraph "Authorization Layers"
        direction TB
        
        subgraph "Layer 1: Authentication"
            auth[User Authentication]
            token[Token Issuance]
        end
        
        subgraph "Layer 2: Coarse Authorization"
            rbac[Role-Based Access Control]
            scopes[OAuth Scopes]
        end
        
        subgraph "Layer 3: Fine Authorization"
            abac[Attribute-Based Policies]
            biz[Business Rules]
        end
    end
    
    subgraph "Enforcement Points"
        gateway[API Gateway]
        services[Microservices]
    end
    
    auth --> token
    token --> rbac
    token --> scopes
    rbac --> abac
    scopes --> abac
    abac --> biz
    
    rbac --> gateway
    scopes --> gateway
    abac --> gateway
    biz --> services
    
    gateway --> services
```

## Appendix C: Role and Permission Mapping

| Role | Description | Permissions | MFA Required |
|------|-------------|------------|--------------|
| Anonymous | Unauthenticated user | Browse catalog, View public content | No |
| Customer | Registered shopper | Place orders, Manage profile, Write reviews | Optional |
| Premium Customer | Paid tier customer | Customer + Early access, Special discounts | Optional |
| Customer Service | Support staff | View orders, Issue refunds, Update customer info | Yes |
| Store Manager | Retail location manager | Customer Service + Inventory management, Staff management | Yes |
| Admin | System administrator | All permissions | Yes |
| API Partner | External system | Specific API access based on agreement | No (mTLS) |
| Service Account | Internal service | Specific service-to-service communication | No (mTLS) | 
---
title: Database Strategy for Microservices
summary: Architectural decision record for database selection and data management in the FlowMart e-commerce platform
sidebar:
    label: Database Strategy
    order: 4
---

## ADR-004: Database Strategy for Microservices in FlowMart E-commerce Platform

### Status

Approved (2024-08-20)

### Context

Our transition from a monolithic architecture to microservices necessitates a reassessment of our database strategy. The existing monolithic application uses a centralized Oracle database with hundreds of tables spanning multiple business domains. This approach has created several challenges:

1. **Schema Coupling**: Changes to database schemas require careful coordination across teams to avoid breaking dependent services.
2. **Scalability Limitations**: The relational database becomes a bottleneck during high-traffic periods, affecting all application features.
3. **One-Size-Fits-All Approach**: Different data access patterns are all forced into the same relational model, leading to suboptimal performance.
4. **Operational Overhead**: Database administration is complex due to competing requirements from different application components.
5. **Development Bottlenecks**: Teams must coordinate database changes, slowing down development velocity.
6. **Cost Efficiency**: The enterprise database licensing model is expensive and doesn't scale cost-effectively with our varying workloads.

As we decompose our application into microservices, we need a database strategy that promotes service autonomy while ensuring data consistency, performance, and operational efficiency.

### Decision

We will adopt a **polyglot persistence strategy** for our microservices architecture, following the principle of "right database for the right job." Key aspects of this strategy include:

1. **Database-per-Service Pattern**:
   - Each microservice will own and exclusively manage its database
   - No direct database access from other services
   - Services interact via well-defined APIs, not shared databases

2. **Primary Database Technologies**:
   - **PostgreSQL**: Primary relational database for services with complex transactional requirements
   - **MongoDB**: Document database for services with flexible schema requirements and read-heavy workloads
   - **Redis**: In-memory data store for caching, session management, and real-time features
   - **Elasticsearch**: Search engine for product catalog and content search
   - **Apache Cassandra**: Wide-column store for high-volume time-series data and analytics
   - **Amazon DynamoDB**: Managed NoSQL for highly scalable microservices with predictable access patterns

3. **Data Consistency Patterns**:
   - **Saga Pattern**: For coordinating transactions across multiple services
   - **Event Sourcing**: For critical business domains requiring complete audit trails
   - **CQRS**: For services with asymmetric read/write loads
   - **Outbox Pattern**: For reliable event publishing during state changes

4. **Data Migration and Evolution**:
   - Versioned database schemas
   - Backward-compatible schema changes
   - Blue/green deployment for database changes
   - Incremental data migration approach

5. **Data Governance**:
   - Centralized data catalog and lineage tracking
   - Common data models for shared business entities
   - Standard approach to master data management
   - Automated data quality monitoring

6. **Operational Excellence**:
   - Infrastructure as Code (IaC) for all database resources
   - Automated backup and recovery procedures
   - Standardized monitoring and alerting
   - Database reliability engineering practices

### Database Selection Criteria by Domain

| Domain | Database Type | Primary Factors | Secondary Considerations |
|--------|---------------|-----------------|--------------------------|
| Product Catalog | MongoDB + Elasticsearch | Schema flexibility, Search capabilities | High read-to-write ratio, Caching |
| Order Management | PostgreSQL | ACID transactions, Complex queries | Event sourcing for audit trail |
| Customer Profile | PostgreSQL | Data consistency, Relational integrity | Privacy compliance, Scalable reads |
| Inventory | MongoDB | Frequent schema evolution, High write throughput | Eventual consistency model |
| Cart & Checkout | Redis + PostgreSQL | Low latency, High availability | Transaction support for checkout |
| Payment Processing | PostgreSQL | Strong consistency, Transaction support | Compliance requirements, Security |
| Analytics | Cassandra | High write throughput, Time-series data | Analytical query patterns |
| Recommendations | Redis + MongoDB | Low latency reads, Flexible data model | Machine learning feature support |
| User Sessions | Redis | Ultra-low latency, Expiration support | High availability, Cross-region replication |
| Content Management | MongoDB | Flexible schema, Document structure | Full-text search capability |

### Consequences

#### Positive

1. **Service Autonomy**: Teams can independently select, optimize, and evolve their databases without cross-team coordination.

2. **Optimized Performance**: Each service can use a database technology optimized for its specific data access patterns.

3. **Independent Scaling**: Database resources can be scaled according to the specific needs of each service.

4. **Improved Resilience**: Database failures are isolated to specific services rather than affecting the entire system.

5. **Fit-for-Purpose Solutions**: Different data models (relational, document, key-value, etc.) can be applied where most appropriate.

6. **Cost Optimization**: Resources can be allocated based on the specific needs of each service.

7. **Incremental Adoption**: New database technologies can be introduced for new services without migrating legacy data.

#### Negative

1. **Increased Operational Complexity**: Managing multiple database technologies requires broader expertise and more sophisticated tooling.

2. **Data Consistency Challenges**: Maintaining consistency across service boundaries requires careful design and implementation.

3. **Learning Curve**: Development teams need to learn multiple database technologies and data access patterns.

4. **Distributed Transactions**: Business processes spanning multiple services require more complex transaction management.

5. **Increased Infrastructure Costs**: Running and maintaining multiple database systems may increase overall infrastructure costs.

6. **Data Duplication**: Some data may need to be duplicated across services, creating synchronization challenges.

7. **Monitoring and Troubleshooting Complexity**: Different databases require different monitoring approaches and expertise.

### Mitigation Strategies

1. **Platform Database Service**:
   - Create an internal platform team that provides database-as-a-service capabilities
   - Standardize on a limited set of supported database technologies
   - Provide automated provisioning, backup, and monitoring

2. **Data Access Layer Pattern**:
   - Create standardized libraries for common database access patterns
   - Abstract database-specific details behind consistent interfaces
   - Implement retry logic, circuit breakers, and observability

3. **Data Synchronization Framework**:
   - Implement a standardized approach to CDC (Change Data Capture)
   - Create reusable components for the Outbox Pattern
   - Develop standard data synchronization workflows

4. **Database Reliability Engineering**:
   - Establish dedicated database reliability engineers
   - Create runbooks for common database operations
   - Implement chaos engineering practices for database failure testing

5. **Developer Training and Support**:
   - Comprehensive training program for supported database technologies
   - Internal knowledge base and best practice documentation
   - Database design review process for new services

### Implementation Details

#### Phase 1: Foundation (Q3-Q4 2024)

1. Establish database platform team and core services
2. Set up standard PostgreSQL and MongoDB offerings
3. Implement database CI/CD pipelines
4. Develop initial monitoring and alerting
5. Create database provisioning automation

#### Phase 2: Expansion (Q1-Q2 2025)

1. Add Redis and Elasticsearch to supported offerings
2. Implement data synchronization framework
3. Develop CQRS and Event Sourcing patterns
4. Create data governance tooling
5. Expand monitoring capabilities

#### Phase 3: Advanced Capabilities (Q3-Q4 2025)

1. Add Cassandra and specialized databases
2. Implement advanced high availability features
3. Develop cross-region replication capabilities
4. Create advanced analytics integration
5. Implement predictive scaling and optimization

### Considered Alternatives

#### 1. Shared Database Approach

**Pros**: Simplicity, familiar model, transactional integrity, easier reporting  
**Cons**: Tight coupling, scalability limitations, schema coordination challenges

This approach would minimize short-term changes but would recreate many of the current issues in our new architecture.

#### 2. Single Database Technology (PostgreSQL Only)

**Pros**: Operational simplicity, consistent expertise, familiar tooling  
**Cons**: Not optimal for all workloads, potential performance compromises

While PostgreSQL is versatile, it isn't the best choice for all our diverse data requirements.

#### 3. Database-as-a-Service Only (e.g., AWS RDS/DynamoDB)

**Pros**: Reduced operational overhead, managed scaling, built-in high availability  
**Cons**: Vendor lock-in, potential cost concerns, less flexibility

While we'll use managed services where appropriate, we need the flexibility to run certain databases on our own infrastructure.

#### 4. Fully Centralized Data Lake Approach

**Pros**: Centralized analytics, simplified data governance, consistent data model  
**Cons**: Complex real-time synchronization, potential performance issues, development overhead

This approach works well for analytics but isn't suitable for operational data needs.

### References

1. Kleppmann, Martin. "Designing Data-Intensive Applications" (O'Reilly Media)
2. Vernon, Vaughn. "Implementing Domain-Driven Design" (Addison-Wesley)
3. Fowler, Martin. "PolyglotPersistence" [martinfowler.com](https://martinfowler.com/bliki/PolyglotPersistence.html)
4. Richardson, Chris. "Microservices Patterns" (Manning Publications)
5. [Database per Service Pattern](https://microservices.io/patterns/data/database-per-service.html)
6. [Saga Pattern](https://microservices.io/patterns/data/saga.html)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-07-20 | 0.1 | Initial draft | Robert Kim |
| 2024-08-02 | 0.2 | Added domain-specific database recommendations | Maria Garcia |
| 2024-08-15 | 0.3 | Incorporated feedback from architecture review | David Boyne |
| 2024-08-20 | 1.0 | Approved by Architecture Board | Architecture Board |

## Appendix A: Database Architecture Overview

```mermaid
flowchart TB
    subgraph "Service Domains"
        subgraph "Product Domain"
            pc[Product Catalog]
            ps[Product Search]
            pc --- MongoDB
            ps --- Elasticsearch
        end
        
        subgraph "Order Domain"
            om[Order Management]
            oh[Order History]
            om --- PostgreSQL
            oh --- MongoDB
        end
        
        subgraph "Customer Domain"
            cp[Customer Profile]
            auth[Authentication]
            sess[Sessions]
            cp --- PostgreSQL
            auth --- PostgreSQL
            sess --- Redis
        end
        
        subgraph "Inventory Domain"
            inv[Inventory Management]
            stk[Stock Tracking]
            inv --- MongoDB
            stk --- MongoDB
        end
        
        subgraph "Payment Domain"
            pay[Payment Processing]
            tx[Transaction Ledger]
            pay --- PostgreSQL
            tx --- PostgreSQL
        end
        
        subgraph "Analytics Domain"
            metrics[Metrics Collection]
            reports[Reporting]
            metrics --- Cassandra
            reports --- Elasticsearch
        end
    end
    
    subgraph "Data Integration"
        ksql[KSQL]
        cdc[CDC Connectors]
        etl[ETL Processes]
        
        Kafka --> ksql
        cdc --> Kafka
        ksql --> etl
    end
    
    MongoDB --> cdc
    PostgreSQL --> cdc
    Cassandra --> cdc
    
    etl --> DataLake
```

## Appendix B: Data Consistency Patterns by Service Type

```mermaid
flowchart TB
    subgraph "Data Consistency Patterns"
        direction TB
        
        subgraph "Transactional Services"
            saga[Saga Pattern]
            tcc[Try-Confirm/Cancel Pattern]
            2pc[Two-Phase Commit]
        end
        
        subgraph "Event-Driven Services"
            es[Event Sourcing]
            cqrs[CQRS]
            outbox[Outbox Pattern]
        end
        
        subgraph "Caching Patterns"
            cache[Cache-Aside]
            writeBehind[Write-Behind]
            readThrough[Read-Through]
        end
    end
    
    subgraph "Service Examples"
        checkout[Checkout Service]
        inventory[Inventory Service]
        catalog[Product Catalog]
        recommendations[Recommendations]
    end
    
    checkout --> saga
    checkout --> 2pc
    inventory --> es
    inventory --> outbox
    catalog --> cqrs
    catalog --> cache
    recommendations --> readThrough
```

## Appendix C: Database Migration Strategy

```mermaid
sequenceDiagram
    participant Legacy as Legacy Database
    participant Middleware as Migration Middleware
    participant New as New Service Databases
    participant CDC as Change Data Capture
    participant Events as Event Bus
    
    Note over Legacy, Events: Phase 1: Shadow Reading
    
    Legacy->>Middleware: Original Data Access
    Middleware->>New: Shadow Writes
    
    Note over Legacy, Events: Phase 2: Dual Write
    
    Legacy->>Middleware: Original Data Access
    Middleware->>Legacy: Write to Legacy
    Middleware->>New: Write to New System
    
    Note over Legacy, Events: Phase 3: CDC Migration
    
    Legacy->>CDC: Capture Changes
    CDC->>Events: Publish Change Events
    Events->>New: Update New System
    
    Note over Legacy, Events: Phase 4: Reverse Flow
    
    New->>Middleware: Primary Data Access
    Middleware->>Legacy: Synchronize for Legacy Systems
    
    Note over Legacy, Events: Phase 5: Legacy Retirement
    
    New->>New: Fully Migrated Operations
``` 
---
title: Frontend Architecture
summary: Architectural decision record for frontend architecture of the FlowMart e-commerce platform
sidebar:
    label: Frontend Architecture
    order: 5
---

## ADR-005: Frontend Architecture for FlowMart E-commerce Platform

### Status

Approved (2024-09-05)

### Context

The frontend of our current monolithic e-commerce application faces numerous challenges:

1. **Performance Issues**: The current server-rendered application has slow page loads and poor mobile performance.
2. **Developer Productivity**: Shared frontend codebase creates development bottlenecks and team dependencies.
3. **Inconsistent User Experience**: Different parts of the application have divergent design patterns and interaction models.
4. **Limited Reusability**: Components are tightly coupled to specific pages, making code reuse difficult.
5. **Testing Challenges**: The current codebase has limited test coverage and is difficult to test effectively.
6. **Technology Constraints**: Outdated technology stack limits our ability to leverage modern frontend capabilities.
7. **Scalability Concerns**: Our current approach doesn't scale well with increasing development team size.
8. **Mobile Experience**: The responsive web approach doesn't deliver optimal mobile experiences.

As we transition to a microservices backend architecture, we need a complementary frontend strategy that addresses these challenges while supporting our business goals of improved customer experience, faster time-to-market, and technical agility.

### Decision

We will adopt a **modern, component-based frontend architecture** with the following key characteristics:

1. **Micro-Frontend Approach**:
   - Decompose the frontend into domain-aligned micro-frontends
   - Enable independent development and deployment of frontend components
   - Provide clear ownership boundaries aligned with backend microservices

2. **Core Technology Stack**:
   - **React**: Primary UI library for component development
   - **Next.js**: Framework for server-rendering and static generation
   - **TypeScript**: For type safety and improved developer experience
   - **Styled Components**: For component-scoped styling
   - **React Query**: For data fetching and state management
   - **Cypress & React Testing Library**: For testing

3. **Design System**:
   - Create a comprehensive design system with reusable UI components
   - Implement a living style guide and component documentation
   - Establish design tokens for consistent theming
   - Support multiple brands and white-labeling capabilities

4. **Architecture Patterns**:
   - **Module Federation**: For sharing components between micro-frontends
   - **Composition Layer**: Shell application for integrating micro-frontends
   - **BFF Pattern**: Backend-for-Frontend APIs for optimized data access
   - **State Management**: Local state when possible, shared state when necessary
   - **Feature Flags**: For controlled feature rollout and A/B testing

5. **Performance Optimization**:
   - Server-side rendering for initial page load performance
   - Client-side rendering for rich interactive experiences
   - Code splitting and lazy loading for optimized bundle sizes
   - Aggressive caching strategies for static assets
   - Optimized media delivery with responsive images and lazy loading

6. **Mobile Strategy**:
   - Progressive Web App (PWA) capabilities for mobile web
   - Responsive design with mobile-first approach
   - Native app shell with React Native for iOS/Android applications
   - Shared business logic between web and native through abstraction layers

### Frontend Domain Decomposition

| Domain | Micro-Frontend | Primary Responsibilities | Team |
|--------|---------------|--------------------------|------|
| Product Discovery | product-browser | Product listing, search, filtering, recommendations | Catalog Team |
| Product Details | product-details | Product information, options, reviews, related items | Catalog Team |
| Shopping Cart | cart-experience | Cart management, saved items, quick checkout | Checkout Team |
| Checkout | checkout-flow | Multi-step checkout, address management, payment | Checkout Team |
| User Account | account-portal | Profile management, preferences, order history | Customer Team |
| Content | content-pages | CMS-managed content, landing pages, promotional content | Marketing Team |
| Store Locator | store-finder | Store search, maps integration, store details | Location Team |
| Order Management | order-tracker | Order status, tracking, returns management | Order Team |

### Consequences

#### Positive

1. **Improved Development Velocity**: Teams can work independently on their domains without blocking each other.

2. **Better Performance**: Optimized loading strategies and modern frontend practices will improve user experience.

3. **Enhanced Reusability**: Shared component library and design system enable consistent, reusable UI elements.

4. **Independent Deployments**: Micro-frontends can be deployed independently, reducing release coordination.

5. **Technology Flexibility**: Different domains can adopt new technologies at their own pace.

6. **Better Testing**: Smaller, more focused codebases are easier to test thoroughly.

7. **Improved User Experience**: Consistent design language and optimized interactions improve customer satisfaction.

8. **Team Autonomy**: Clear ownership boundaries enable teams to take full responsibility for their domains.

#### Negative

1. **Increased Complexity**: Micro-frontend architectures add operational and integration complexity.

2. **Learning Curve**: Teams need to adapt to new patterns and technologies.

3. **Potential Duplication**: Without careful governance, similar solutions may be implemented multiple times.

4. **Integration Challenges**: Ensuring consistent behavior across micro-frontends requires careful coordination.

5. **Performance Overhead**: Micro-frontend composition can introduce additional runtime overhead if not carefully managed.

6. **Increased Infrastructure Needs**: More sophisticated build, deployment, and monitoring infrastructure required.

7. **Governance Challenges**: Balancing team autonomy with architectural consistency requires active governance.

### Mitigation Strategies

1. **Frontend Platform Team**:
   - Create a dedicated platform team to provide shared infrastructure and tools
   - Develop reusable patterns and documentation for micro-frontend implementation
   - Provide developer tooling and simplified local development experience

2. **Comprehensive Design System**:
   - Invest in a robust design system with clear guidelines and components
   - Create automated tools for design compliance checking
   - Regular design system sessions to ensure alignment across teams

3. **Performance Budgeting**:
   - Establish clear performance metrics and budgets for each micro-frontend
   - Automated performance testing in CI/CD pipeline
   - Regular performance reviews and optimization workshops

4. **Developer Experience**:
   - Create standardized templates and generators for new micro-frontends
   - Provide comprehensive documentation and internal training
   - Establish frontend community of practice for knowledge sharing

5. **Governance Model**:
   - Create a frontend architecture council with representatives from each team
   - Regular architecture reviews and pattern sharing
   - Clear guidelines for when to share vs. create new components

### Implementation Details

#### Phase 1: Foundation (Q4 2024)

1. Create core design system and component library
2. Establish micro-frontend shell architecture
3. Develop initial build and deployment pipeline
4. Implement authentication and session management
5. Create developer documentation and examples

#### Phase 2: Domain Migration (Q1-Q2 2025)

1. Migrate high-priority domains to micro-frontend architecture
2. Implement analytics and monitoring strategy
3. Develop advanced patterns for cross-domain interaction
4. Enhance performance optimization capabilities
5. Create specialized mobile experiences

#### Phase 3: Advanced Capabilities (Q3-Q4 2025)

1. Implement personalization framework
2. Develop advanced A/B testing capabilities
3. Enhance internationalization and localization
4. Create specialized native experiences
5. Implement advanced analytics and behavior tracking

### Considered Alternatives

#### 1. Monolithic Single-Page Application (SPA)

**Pros**: Simpler architecture, unified codebase, shared state management  
**Cons**: Development bottlenecks, scaling challenges, larger bundle sizes

This approach would be simpler initially but would recreate many of our current scaling challenges.

#### 2. Server-Side Rendering Only

**Pros**: Simpler technology stack, better SEO by default, reduced client-side JavaScript  
**Cons**: Limited interactivity, slower subsequent navigation, poorer offline capabilities

While this would improve initial load performance, it would limit our ability to create rich interactive experiences.

#### 3. Native Mobile Apps Only for Mobile

**Pros**: Optimal mobile experience, full native capabilities, offline functionality  
**Cons**: Development cost, platform duplication, release friction

This would deliver better mobile experiences but at significantly higher development and maintenance costs.

#### 4. Framework-Agnostic Approach

**Pros**: Maximum team autonomy, best-tool-for-job flexibility  
**Cons**: Duplication of efforts, inconsistent experiences, integration challenges

While offering maximum flexibility, this would lead to significant inconsistency and integration challenges.

### References

1. [Micro Frontends](https://martinfowler.com/articles/micro-frontends.html) (Martin Fowler)
2. [Module Federation](https://webpack.js.org/concepts/module-federation/) (Webpack Documentation)
3. ["Building Micro-Frontends" by Luca Mezzalira](https://www.oreilly.com/library/view/building-micro-frontends/9781492082989/)
4. [Frontend Design Systems](https://designsystemsrepo.com/design-systems)
5. [Atomic Design](https://atomicdesign.bradfrost.com/) by Brad Frost
6. [React Documentation](https://reactjs.org/docs/getting-started.html)
7. [Next.js Documentation](https://nextjs.org/docs)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-08-10 | 0.1 | Initial draft | Jennifer Lee |
| 2024-08-20 | 0.2 | Added implementation phases and domain decomposition | Alex Johnson |
| 2024-08-30 | 0.3 | Incorporated feedback from UX and frontend teams | Sarah Chen |
| 2024-09-05 | 1.0 | Approved by Architecture and UX Boards | Architecture Board |

## Appendix A: Frontend Architecture Overview

```mermaid
flowchart TB
    subgraph "Client Applications"
        web[Web Browser]
        ios[iOS App]
        android[Android App]
    end
    
    subgraph "Micro-Frontend Shell"
        shell[Shell Application]
        router[Routing Layer]
        auth[Auth Module]
    end
    
    subgraph "Micro-Frontends"
        product[Product Experience]
        cart[Cart & Checkout]
        account[User Account]
        content[Content Pages]
        order[Order Management]
    end
    
    subgraph "Shared Foundation"
        design[Design System]
        core[Core Components]
        utils[Utility Functions]
        hooks[React Hooks]
    end
    
    subgraph "Backend Integration"
        bff[BFF Layer]
        api[API Gateway]
    end
    
    web --> shell
    ios --> shell
    android --> shell
    
    shell --> router
    shell --> auth
    
    router --> product
    router --> cart
    router --> account
    router --> content
    router --> order
    
    product --> design
    cart --> design
    account --> design
    content --> design
    order --> design
    
    product --> core
    cart --> core
    account --> core
    content --> core
    order --> core
    
    product --> bff
    cart --> bff
    account --> bff
    content --> bff
    order --> bff
    
    bff --> api
```

## Appendix B: Component Development Workflow

```mermaid
sequenceDiagram
    participant Designer
    participant Dev as Developer
    participant PR as Pull Request
    participant CI as CI/CD Pipeline
    participant DS as Design System
    participant App as Application
    
    Designer->>Designer: Create Component Design
    Designer->>Dev: Handoff Design Specs
    
    Dev->>Dev: Develop Component
    Dev->>Dev: Write Component Tests
    Dev->>Dev: Document Component
    
    Dev->>PR: Submit Pull Request
    PR->>CI: Trigger CI Pipeline
    
    CI->>CI: Lint Check
    CI->>CI: Type Check
    CI->>CI: Unit Tests
    CI->>CI: Visual Regression Tests
    CI->>CI: Bundle Size Analysis
    CI->>CI: Accessibility Tests
    
    CI->>PR: Report Results
    PR->>DS: Merge to Design System
    
    DS->>App: Component Available for Use
    App->>App: Integrate Component
```

## Appendix C: Micro-Frontend Integration Patterns

```mermaid
flowchart TB
    subgraph "Integration Approaches"
        direction TB
        
        subgraph "Build-Time Integration"
            npm[NPM Dependencies]
            mono[Monorepo Packages]
        end
        
        subgraph "Run-Time Integration"
            fed[Module Federation]
            iframes[IFrames]
            web[Web Components]
        end
        
        subgraph "Edge-Side Integration"
            esi[Edge Side Includes]
            ssi[Server Side Includes]
        end
    end
    
    subgraph "Implementation Patterns"
        direction TB
        
        subgraph "Horizontal Split"
            domains[By Domain/Business Function]
        end
        
        subgraph "Vertical Split"
            pages[Page-Based Composition]
        end
        
        subgraph "Hybrid Approach"
            shell[Shell + Domain Modules]
        end
    end
    
    fed --> shell
    domains --> fed
    pages --> iframes
    shell --> web
``` 
---
title: Observability Strategy
summary: Architectural decision record for implementing observability in the FlowMart e-commerce platform
sidebar:
    label: Observability Strategy
    order: 6
---

## ADR-006: Observability Strategy for FlowMart E-commerce Platform

### Status

Approved (2024-09-15)

### Context

As we transition from a monolithic architecture to a distributed microservices-based e-commerce platform, traditional monitoring approaches are no longer sufficient. The increased complexity of our architecture introduces several challenges:

1. **Distributed Systems Complexity**: With dozens of microservices communicating asynchronously, understanding system behavior becomes significantly more difficult.

2. **Increased Failure Points**: A distributed architecture introduces more potential failure points and complex failure modes.

3. **Service Interdependencies**: Issues in one service can cascade to others, making root cause analysis challenging.

4. **Multiple Technologies**: Different services use different languages, frameworks, and datastores, requiring diverse instrumentation approaches.

5. **Deployment Frequency**: With continuous deployment across multiple services, correlating issues with specific changes becomes more complex.

6. **Performance Bottlenecks**: Identifying performance bottlenecks in a distributed system requires end-to-end visibility.

7. **Cross-Team Collaboration**: Multiple teams own different services, requiring a common observability approach and shared understanding.

8. **Business Impact Correlation**: Need to connect technical metrics with business outcomes to prioritize improvements.

Our current monitoring strategy is primarily focused on infrastructure metrics and basic application health checks, which is insufficient for effectively operating our new architecture.

### Decision

We will implement a comprehensive **observability strategy** based on the "three pillars" approach (metrics, logs, and traces) with distributed tracing as a foundational element. Key components of this strategy include:

1. **Observability Stack**:
   - **Metrics**: Prometheus for metrics collection and alerting
   - **Logs**: Elasticsearch, Logstash, and Kibana (ELK) for log aggregation and analysis
   - **Traces**: Jaeger for distributed tracing
   - **Dashboard**: Grafana for unified visualization and dashboarding
   - **Alerting**: Prometheus Alertmanager with PagerDuty integration

2. **Instrumentation Standards**:
   - **Distributed Tracing**: OpenTelemetry as the standard instrumentation framework
   - **Structured Logging**: JSON-formatted logs with standardized fields across all services
   - **Metrics Naming**: Consistent metrics naming convention following Prometheus best practices
   - **Service Level Objectives (SLOs)**: Defined for all critical user journeys
   - **Error Budgets**: Established for each service and user journey

3. **Core Observability Capabilities**:
   - **Request Tracing**: End-to-end tracing for all user-initiated actions
   - **Dependency Monitoring**: Monitoring of all external dependencies and services
   - **Business Metrics**: Tracking of key business metrics alongside technical metrics
   - **Synthetic Monitoring**: Regular testing of critical user journeys
   - **Real User Monitoring (RUM)**: Frontend performance and error tracking
   - **Anomaly Detection**: Automated detection of abnormal system behavior
   - **Correlation Engine**: Tools to correlate metrics, logs, and traces during investigation

4. **Data Retention and Sampling**:
   - Critical business transaction traces retained for 30 days
   - High-cardinality metrics sampled at appropriate rates
   - Error logs retained for 90 days
   - Regular logs retained for 30 days
   - Aggregated metrics retained for 13 months for year-over-year analysis

5. **Implementation Approach**:
   - Platform team creates and maintains observability infrastructure
   - Standardized libraries and SDKs for each supported language/framework
   - Observability as code, with instrumentation verified in CI/CD pipelines
   - Service templates with pre-configured observability components
   - Progressive enhancement of observability capabilities

### Observability Requirements by Domain

| Domain | Key Metrics | Special Requirements | SLO Targets |
|--------|------------|----------------------|-------------|
| Product Catalog | Search latency, Cache hit rate | High cardinality data handling | 99.9% availability, p95 < 300ms |
| Order Processing | Order volume, Processing time, Error rate | Comprehensive transaction tracing | 99.95% availability, p95 < 500ms |
| Payment | Transaction volume, Success rate, Fraud detection rate | PCI compliance in logging | 99.99% availability, p95 < 800ms |
| Inventory | Stock level changes, Reservation rate, Stockout events | Event-sourcing visibility | 99.9% availability, p95 < 400ms |
| User Authentication | Login volume, Success rate, MFA usage | Security-focused monitoring | 99.99% availability, p95 < 250ms |
| Checkout | Cart conversion rate, Abandonment points, Session duration | User journey analysis | 99.95% availability, p95 < 600ms |
| Shipping | Fulfillment time, Carrier performance, Tracking accuracy | Third-party integration monitoring | 99.9% availability, p95 < 350ms |
| Content Delivery | Cache hit ratio, Origin fetch time, Asset size | CDN performance visibility | 99.9% availability, p95 < 200ms |

### Consequences

#### Positive

1. **Improved Troubleshooting**: Faster identification and resolution of issues through correlated observability data.

2. **Proactive Detection**: Ability to detect potential issues before they impact users through anomaly detection and trend analysis.

3. **Enhanced Understanding**: Better understanding of system behavior, dependencies, and performance characteristics.

4. **Data-Driven Optimization**: Ability to make targeted performance improvements based on actual usage patterns.

5. **Cross-Team Collaboration**: Common observability platform enables better collaboration during incident response.

6. **Business Alignment**: Correlation between technical metrics and business outcomes helps prioritize technical work.

7. **Resilience Verification**: Ability to verify that resilience mechanisms (circuit breakers, retries, etc.) function properly.

8. **Capacity Planning**: Better data for capacity planning and scaling decisions.

#### Negative

1. **Implementation Overhead**: Adding comprehensive instrumentation requires additional development effort.

2. **Data Volume Challenges**: Managing the volume of observability data requires careful planning and potential sampling.

3. **Performance Impact**: Instrumentation adds some overhead to application performance, which must be managed.

4. **Complexity**: A sophisticated observability stack adds operational complexity and maintenance requirements.

5. **Learning Curve**: Teams need to learn new tools, concepts, and practices for effective use of observability data.

6. **Cost Considerations**: Storage and processing of observability data has significant cost implications at scale.

7. **Privacy and Security**: Observability data may contain sensitive information requiring appropriate controls.

### Mitigation Strategies

1. **Automated Instrumentation**:
   - Use auto-instrumentation agents where possible
   - Create starter templates with instrumentation pre-configured
   - Build instrumentation verification into CI/CD pipelines

2. **Data Management**:
   - Implement appropriate sampling strategies for high-volume data
   - Utilize data compression and aggregation techniques
   - Define appropriate retention policies based on data criticality

3. **Operating Model**:
   - Create an observability platform team to manage the core infrastructure
   - Establish observability champions within each service team
   - Regular observability review and enhancement sessions

4. **Knowledge Sharing**:
   - Comprehensive documentation and training on observability tools
   - Regular workshops on effective use of observability data
   - Shared dashboards and runbooks for common scenarios

5. **Security and Privacy**:
   - Automated PII detection and redaction in logs and traces
   - Role-based access control for observability data
   - Regular audits of observability data for sensitive information

### Implementation Details

#### Phase 1: Foundation (Q4 2024)

1. Deploy core observability infrastructure (Prometheus, ELK, Jaeger, Grafana)
2. Implement standardized logging format and collection pipeline
3. Create initial service dashboards and alerting
4. Develop instrumentation libraries for primary service frameworks
5. Establish basic SLOs for critical services

#### Phase 2: Enhanced Capabilities (Q1 2025)

1. Implement distributed tracing across all critical user journeys
2. Create business metrics dashboards correlated with technical metrics
3. Develop anomaly detection for key system behaviors
4. Implement synthetic monitoring for critical paths
5. Create runbooks integrated with observability tools

#### Phase 3: Advanced Observability (Q2-Q3 2025)

1. Implement ML-based anomaly detection and prediction
2. Create self-service observability platform capabilities
3. Develop advanced correlation between metrics, logs, and traces
4. Implement automated performance testing with observability verification
5. Develop capacity planning and forecasting based on observability data

### Considered Alternatives

#### 1. Commercial APM Solution Only (e.g., Dynatrace, New Relic)

**Pros**: Comprehensive out-of-the-box capabilities, reduced implementation effort, integrated platform  
**Cons**: High cost at scale, reduced flexibility, potential vendor lock-in

While commercial APM tools provide excellent capabilities, we chose an open-source approach for cost flexibility and customization ability. We will reevaluate this decision as our needs evolve.

#### 2. Minimal Custom Instrumentation

**Pros**: Reduced development overhead, simplicity, lower initial investment  
**Cons**: Limited visibility, reactive troubleshooting, challenges scaling observability with system growth

This approach would not provide the depth of insight needed for effective operation of our distributed system.

#### 3. Service Mesh-Based Observability

**Pros**: Reduced application instrumentation, consistent approach, network-level visibility  
**Cons**: Limited application-level context, additional infrastructure complexity, potential performance impact

While we will leverage service mesh observability capabilities, we need application-level instrumentation for complete visibility.

#### 4. Multiple Independent Monitoring Systems

**Pros**: Specialized tools for each domain, team autonomy in tooling decisions  
**Cons**: Fragmented visibility, integration challenges, inconsistent practices

This approach would create silos and make cross-service troubleshooting significantly more difficult.

### References

1. Charity Majors, Liz Fong-Jones, George Miranda, "Observability Engineering" (O'Reilly)
2. Cindy Sridharan, "Distributed Systems Observability" (O'Reilly)
3. [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
4. [Google SRE Book - Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
5. [Prometheus Best Practices](https://prometheus.io/docs/practices/naming/)
6. [Grafana Observability Strategy](https://grafana.com/blog/2019/10/21/whats-next-for-observability/)

### Decision Record History

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2024-08-20 | 0.1 | Initial draft | Kevin Zhang |
| 2024-09-01 | 0.2 | Added implementation phases and domain details | Rachel Williams |
| 2024-09-10 | 0.3 | Incorporated feedback from SRE and platform teams | David Boyne |
| 2024-09-15 | 1.0 | Approved by Architecture and Operations Boards | Architecture Board |

## Appendix A: Observability Architecture

```mermaid
flowchart TB
    subgraph "Data Sources"
        apps[Applications]
        infra[Infrastructure]
        db[Databases]
        net[Network]
        fe[Frontend]
    end
    
    subgraph "Collection Layer"
        prom[Prometheus]
        fluent[FluentBit]
        otel[OpenTelemetry Collector]
        beats[Beats]
    end
    
    subgraph "Storage Layer"
        tsdb[Prometheus TSDB]
        es[Elasticsearch]
        jaeger_db[Jaeger Storage]
        loki[Loki]
    end
    
    subgraph "Processing Layer"
        alerts[Alertmanager]
        anom[Anomaly Detection]
        corr[Correlation Engine]
        agg[Log Aggregation]
    end
    
    subgraph "Visualization Layer"
        grafana[Grafana]
        kibana[Kibana]
        jaeger_ui[Jaeger UI]
        dashboards[Custom Dashboards]
    end
    
    subgraph "Notification Layer"
        pd[PagerDuty]
        slack[Slack]
        email[Email]
        webhook[Webhooks]
    end
    
    apps --> otel
    apps --> fluent
    apps --> prom
    infra --> beats
    infra --> prom
    db --> prom
    db --> beats
    net --> prom
    net --> beats
    fe --> otel
    
    otel --> jaeger_db
    otel --> loki
    otel --> tsdb
    fluent --> es
    beats --> es
    prom --> tsdb
    
    tsdb --> alerts
    tsdb --> anom
    es --> agg
    es --> corr
    jaeger_db --> corr
    loki --> corr
    
    tsdb --> grafana
    es --> kibana
    es --> grafana
    jaeger_db --> jaeger_ui
    jaeger_db --> grafana
    corr --> dashboards
    agg --> dashboards
    
    alerts --> pd
    alerts --> slack
    alerts --> email
    alerts --> webhook
```

## Appendix B: Observability Data Flow

```mermaid
sequenceDiagram
    participant User
    participant Service1 as Service A
    participant Service2 as Service B
    participant Service3 as Service C
    participant OTel as OpenTelemetry
    participant Logs as Log System
    participant Metrics as Metrics System
    participant Traces as Tracing System
    participant Dashboard as Dashboard
    participant Alerts as Alert System
    
    User->>Service1: Request
    
    Service1->>OTel: Generate Span 1
    Service1->>Logs: Log Request Details
    Service1->>Metrics: Update Request Counter
    
    Service1->>Service2: Internal Request
    Service2->>OTel: Generate Span 2 (child of Span 1)
    Service2->>Logs: Log Processing Details
    Service2->>Metrics: Update Processing Metrics
    
    Service2->>Service3: Database Query
    Service3->>OTel: Generate Span 3 (child of Span 2)
    Service3->>Logs: Log Query Details
    Service3->>Metrics: Update Query Metrics
    
    Service3-->>Service2: Query Result
    Service2-->>Service1: Internal Response
    Service1-->>User: Response
    
    Service1->>OTel: Complete Span 1
    Service1->>Metrics: Update Response Time
    
    OTel->>Traces: Store Complete Trace
    
    Logs->>Dashboard: Visualize Logs
    Metrics->>Dashboard: Visualize Metrics
    Traces->>Dashboard: Visualize Traces
    
    Metrics->>Alerts: Trigger Alerts (if threshold exceeded)
    Alerts->>Dashboard: Display Alert Status
```

## Appendix C: Service Level Objectives (SLOs) Framework

```mermaid
flowchart TB
    subgraph "SLO Definition Process"
        direction TB
        
        subgraph "1. Identify Critical User Journeys"
            journey1[Product Search]
            journey2[Add to Cart]
            journey3[Checkout]
            journey4[Order Status]
        end
        
        subgraph "2. Define Service Level Indicators (SLIs)"
            availability[Availability %]
            latency[Latency (p50, p95, p99)]
            errors[Error Rate %]
            saturation[Resource Saturation]
        end
        
        subgraph "3. Set Target Objectives"
            slo1[99.9% Availability]
            slo2[p95 < 300ms]
            slo3[Error Rate < 0.1%]
        end
        
        subgraph "4. Establish Error Budgets"
            monthly[Monthly Budget]
            quarterly[Quarterly Budget]
            policy[Error Budget Policy]
        end
    end
    
    subgraph "SLO Monitoring & Reporting"
        direction TB
        
        subgraph "Real-time Dashboards"
            current[Current Status]
            trends[Burn Rate]
            history[Historical Performance]
        end
        
        subgraph "Alerting Strategy"
            warning[Budget Warning (50%)]
            critical[Budget Critical (75%)]
            depleted[Budget Depleted (90%)]
        end
        
        subgraph "Continuous Improvement"
            retro[SLO Reviews]
            adjust[Target Adjustments]
            prioritize[Reliability Work]
        end
    end
    
    journey1 --> availability
    journey1 --> latency
    journey2 --> availability
    journey2 --> latency
    journey3 --> errors
    journey3 --> availability
    journey4 --> latency
    
    availability --> slo1
    latency --> slo2
    errors --> slo3
    
    slo1 --> monthly
    slo2 --> monthly
    slo3 --> monthly
    
    monthly --> current
    monthly --> warning
    
    current --> retro
    warning --> prioritize
``` 