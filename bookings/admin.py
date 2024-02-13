from django.contrib import admin

from bookings.models import Booking, BookingItem



class OrderItemTabulareAdmin(admin.TabularInline):
    model = BookingItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(BookingItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "booking", "product", "name", "price", "quantity"
    search_fields = (
        "booking",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Booking
    fields = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Booking)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "id",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
    )
    inlines = (OrderItemTabulareAdmin,)
