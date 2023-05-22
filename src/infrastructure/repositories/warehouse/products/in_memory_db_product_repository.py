# from typing import Any, Type
# from injectable import injectable, autowired, Autowired
# from src.buses.events.ports.consumer import Consumer
# from src.buses.events.ports.producer import Producer

# from src.application.shared.queries.domain.query_handler import QueryHandler

# from src.application.warehouse.products.services.get_product_stock.get_product_stock_query import (
#     GetProductQuery,
# )
# from src.infrastructure.repositories.in_memory_db import in_memory_db

# AutowiredProducer: Type[Producer[Any]] = Autowired(Producer)
# AutowiredConsumer: Type[Consumer[Any]] = Autowired(Consumer)


# @injectable(singleton=True)  # type: ignore
# class InMemoryDBProductRepository(QueryHandler[GetProductStockQuery]):
#     @autowired
#     def __init__(
#         self, producer: AutowiredProducer, consumer: AutowiredConsumer
#     ) -> None:
#         self._producer = producer
#         self._consumer = consumer
#         print("Infraestructure: subscribing to topic-query-i")
#         consumer.subscribe("topic-query-i", self.handle)

#     def handle(self, query: GetProductStockQuery) -> None:
#         product = in_memory_db.get("products", query.uuid)
#         self._producer.publish("topic-query-i-response", product)
